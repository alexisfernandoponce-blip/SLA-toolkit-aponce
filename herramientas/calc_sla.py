
#!/usr/bin/env python3
"""
SLA Toolkit Pro
Motor de evaluación de acuerdos de nivel de servicio.

Uso:
    python herramientas/calc_sla.py \
        -o objetivos.yaml -m mediciones.csv

Requiere:
    pip install pyyaml
"""

import argparse
import csv
import json
import operator
from pathlib import Path

import yaml


OPERADORES = {
    ">=": operator.ge,
    "<=": operator.le,
    ">": operator.gt,
    "<": operator.lt,
    "==": operator.eq,
}

NOMBRES = {
    "disponibilidad": "Disponibilidad",
    "latencia": "Latencia RTT",
    "jitter": "Jitter",
    "perdida": "Pérdida de paquetes",
    "throughput": "Throughput",
    "respuesta": "Tiempo de respuesta",
    "mttr": "Tiempo de reparación",
}


def numero(valor, nombre):
    try:
        return float(str(valor).replace(",", "."))
    except (ValueError, TypeError):
        raise ValueError(
            f"Valor numérico inválido en {nombre}: {valor}"
        )


def cargar_objetivos(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        datos = yaml.safe_load(archivo)

    if not isinstance(datos, dict):
        raise ValueError("El archivo YAML debe contener un objeto.")

    if "metricas" not in datos:
        raise ValueError("Falta la sección 'metricas' en YAML.")

    return datos


def cargar_mediciones(ruta):
    with open(ruta, "r", encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo)

        requeridas = {"metrica", "valor"}
        columnas = set(lector.fieldnames or [])

        if not requeridas.issubset(columnas):
            raise ValueError(
                "El CSV requiere las columnas: metrica, valor. "
                "Admite además muestras, cobertura y valido."
            )

        return list(lector)


def es_valida(fila):
    valor = str(fila.get("valido", "si")).strip().lower()
    return valor not in ("no", "false", "0", "excluido")


def promedio_ponderado(filas):
    total = 0.0
    muestras_totales = 0.0

    for fila in filas:
        muestras = numero(
            fila.get("muestras") or 1, "muestras"
        )
        if muestras <= 0:
            raise ValueError("Las muestras deben ser positivas.")

        valor = numero(fila["valor"], "valor")
        total += valor * muestras
        muestras_totales += muestras

    if not muestras_totales:
        return None

    return total / muestras_totales


def calcular_disponibilidad(config, filas):
    periodo = numero(
        config["periodo_minutos"], "periodo_minutos"
    )
    if periodo <= 0:
        raise ValueError("El período debe ser positivo.")

    indisponibilidad = sum(
        numero(fila["valor"], "minutos de caída")
        for fila in filas
    )

    if indisponibilidad < 0 or indisponibilidad > periodo:
        raise ValueError("Tiempo de caída fuera del período.")

    disponibilidad = (
        (periodo - indisponibilidad) / periodo
    ) * 100

    return disponibilidad


def obtener_cobertura(filas, config):
    coberturas = [
        numero(fila["cobertura"], "cobertura")
        for fila in filas
        if fila.get("cobertura", "").strip()
    ]

    if coberturas:
        if len(coberturas) != len(filas):
            return None
        if any(c < 0 or c > 100 for c in coberturas):
            raise ValueError("Cobertura fuera de 0 a 100.")
        return min(coberturas)

    if "cobertura" in config:
        cobertura = numero(config["cobertura"], "cobertura")
        if not 0 <= cobertura <= 100:
            raise ValueError("Cobertura fuera de 0 a 100.")
        return cobertura

    return None


def calcular_credito_disponibilidad(valor, tramos):
    for tramo in tramos:
        minimo = numero(
            tramo.get("desde", 0), "desde"
        )
        maximo = numero(
            tramo.get("hasta", 100), "hasta"
        )

        if minimo <= valor < maximo:
            return numero(
                tramo["credito"], "credito"
            )

    return 0.0


def evaluar_metrica(nombre, config, filas, general):
    validas = [fila for fila in filas if es_valida(fila)]

    resultado = {
        "metrica": nombre,
        "nombre": NOMBRES.get(nombre, nombre.title()),
        "objetivo": config["objetivo"],
        "operador": config["operador"],
        "unidad": config.get("unidad", ""),
        "medido": None,
        "cobertura": None,
        "veredicto": "evidencia insuficiente",
        "credito_porcentaje": 0.0,
        "observacion": "",
    }

    if not validas:
        resultado["observacion"] = "No existen mediciones válidas."
        return resultado

    cobertura = obtener_cobertura(validas, config)
    resultado["cobertura"] = cobertura

    minimo = numero(
        config.get(
            "cobertura_minima",
            general.get("cobertura_minima", 90)
        ),
        "cobertura_minima"
    )

    if cobertura is None:
        resultado["observacion"] = (
            "No se acreditó la cobertura de medición."
        )
        return resultado

    if cobertura < minimo:
        resultado["observacion"] = (
            f"Cobertura {cobertura:.2f}% inferior "
            f"al mínimo {minimo:.2f}%."
        )
        return resultado

    if nombre == "disponibilidad":
        valor = calcular_disponibilidad(config, validas)
    elif config.get("estadistico", "promedio") == "maximo":
        valor = max(
            numero(fila["valor"], "valor")
            for fila in validas
        )
    else:
        valor = promedio_ponderado(validas)

    resultado["medido"] = round(valor, 4)

    op = config["operador"]
    if op not in OPERADORES:
        raise ValueError(f"Operador no admitido: {op}")

    objetivo = numero(config["objetivo"], "objetivo")
    cumple = OPERADORES[op](valor, objetivo)

    if cumple:
        resultado["veredicto"] = "cumple"
        resultado["observacion"] = (
            "Resultado dentro del objetivo contractual."
        )
        return resultado

    resultado["veredicto"] = "no cumple"
    resultado["observacion"] = (
        "Resultado fuera del objetivo contractual."
    )

    if nombre == "disponibilidad":
        resultado["credito_porcentaje"] = (
            calcular_credito_disponibilidad(
                valor,
                general.get("tramos_disponibilidad", [])
            )
        )
    else:
        resultado["credito_porcentaje"] = numero(
            config.get("credito", 0), "credito"
        )

    return resultado


def evaluar(objetivos, mediciones):
    general = objetivos.get("contrato", {})
    configuraciones = objetivos["metricas"]

    agrupadas = {}

    for fila in mediciones:
        nombre = fila["metrica"].strip().lower()
        agrupadas.setdefault(nombre, []).append(fila)

    resultados = []

    for nombre, config in configuraciones.items():
        filas = agrupadas.get(nombre, [])
        resultados.append(
            evaluar_metrica(nombre, config, filas, general)
        )

    credito_suma = sum(
        item["credito_porcentaje"]
        for item in resultados
    )

    tope = numero(
        general.get("tope_credito", 50), "tope_credito"
    )
    cargo = numero(
        general.get("cargo_mensual", 0), "cargo_mensual"
    )

    credito_final = min(credito_suma, tope)
    monto = cargo * credito_final / 100

    estados = {
        "cumple": 0,
        "no cumple": 0,
        "evidencia insuficiente": 0,
    }

    for item in resultados:
        estados[item["veredicto"]] += 1

    return {
        "plataforma": "SLA Toolkit Pro",
        "cliente": general.get("cliente", ""),
        "proveedor": general.get("proveedor", ""),
        "periodo": general.get("periodo", ""),
        "resultados": resultados,
        "resumen": estados,
        "credito": {
            "cargo_mensual": cargo,
            "porcentaje_acumulado": round(credito_suma, 2),
            "tope_porcentaje": tope,
            "porcentaje_aplicable": round(credito_final, 2),
            "monto_clp": round(monto),
        },
    }


def mostrar_reporte(reporte):
    print("=" * 58)
    print("              SLA TOOLKIT PRO")
    print("        Evaluación de cumplimiento SLA")
    print("=" * 58)
    print(f"Cliente: {reporte['cliente']}")
    print(f"Proveedor: {reporte['proveedor']}")
    print(f"Período: {reporte['periodo']}")
    print("-" * 58)

    for item in reporte["resultados"]:
        print(f"\n{item['nombre']}")
        print(
            f"Objetivo: {item['operador']} "
            f"{item['objetivo']} {item['unidad']}"
        )
        print(f"Medido: {item['medido']}")
        print(f"Cobertura: {item['cobertura']}")
        print(f"Veredicto: {item['veredicto'].upper()}")
        print(f"Observación: {item['observacion']}")

    credito = reporte["credito"]

    print("\n" + "=" * 58)
    print("CRÉDITOS DE SERVICIO")
    print(
        f"Porcentaje aplicable: "
        f"{credito['porcentaje_aplicable']:.2f}%"
    )
    print(f"Monto: ${credito['monto_clp']:,.0f} CLP")
    print("=" * 58)


def main():
    parser = argparse.ArgumentParser(
        description="Calculadora de cumplimiento SLA"
    )
    parser.add_argument(
        "-o", "--objetivos", required=True,
        help="Archivo YAML con objetivos contractuales"
    )
    parser.add_argument(
        "-m", "--mediciones", required=True,
        help="Archivo CSV con mediciones"
    )
    parser.add_argument(
        "--json", action="store_true",
        help="Mostrar resultados en formato JSON"
    )
    parser.add_argument(
        "--salida", help="Guardar resultados en archivo JSON"
    )

    args = parser.parse_args()

    objetivos = cargar_objetivos(args.objetivos)
    mediciones = cargar_mediciones(args.mediciones)
    reporte = evaluar(objetivos, mediciones)

    if args.salida:
        Path(args.salida).write_text(
            json.dumps(
                reporte, ensure_ascii=False, indent=2
            ),
            encoding="utf-8"
        )

    if args.json:
        print(json.dumps(
            reporte, ensure_ascii=False, indent=2
        ))
    else:
        mostrar_reporte(reporte)


if __name__ == "__main__":
    main()
