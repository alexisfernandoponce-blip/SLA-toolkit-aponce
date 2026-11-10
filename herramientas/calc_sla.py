
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SLA TOOLKIT PRO
Motor de verificación de acuerdos de nivel de servicio.

Entradas:
  - objetivos.yaml
  - mediciones.csv

Salidas:
  - Reporte técnico en consola
  - JSON para la aplicación web
  - Archivo JSON opcional

Instalación:
  pip install pyyaml

Ejecución:
  python herramientas/calc_sla.py \
    -o herramientas/objetivos.yaml \
    -m datos/mediciones-ejemplo.csv

  python herramientas/calc_sla.py \
    -o herramientas/objetivos.yaml \
    -m datos/mediciones-ejemplo.csv \
    --json

Formato CSV:
  tipo,id,metrica,valor,muestras,esperadas,dias_cubiertos,
  valido,metodo,punto,origen,fecha,inicio,fin,
  apertura,respuesta,aviso,causa

Tipos admitidos:
  medicion, evento, ticket

Reglas:
  - No se inventan mediciones faltantes.
  - Se comprueba el punto y método contractual.
  - Se aplican exclusiones de disponibilidad.
  - Se evalúan tickets individualmente.
  - Se exige cobertura válida cuando corresponde.
  - Se aplican los créditos y el tope contractual.
"""

import argparse
import csv
import json
import operator
import sys
from collections import defaultdict
from datetime import datetime
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

ESTADOS = (
    "cumple",
    "no cumple",
    "evidencia insuficiente",
)


def numero(valor, nombre="valor"):
    if valor is None or str(valor).strip() == "":
        raise ValueError(f"Falta el valor de {nombre}")

    try:
        return float(str(valor).replace(",", "."))
    except (ValueError, TypeError) as exc:
        raise ValueError(
            f"Valor numérico inválido en {nombre}: {valor}"
        ) from exc


def opcional(valor, defecto=None):
    if valor is None or str(valor).strip() == "":
        return defecto
    return numero(valor)


def fecha_hora(valor):
    if not valor:
        return None

    valor = str(valor).strip()

    formatos = (
        "%Y-%m-%d %H:%M",
        "%Y-%m-%dT%H:%M",
        "%d-%m-%Y %H:%M",
    )

    for formato in formatos:
        try:
            return datetime.strptime(valor, formato)
        except ValueError:
            pass

    raise ValueError(f"Fecha u hora inválida: {valor}")


def minutos_entre(inicio, fin):
    a = fecha_hora(inicio)
    b = fecha_hora(fin)

    if a is None or b is None:
        return None

    minutos = (b - a).total_seconds() / 60

    if minutos < 0:
        raise ValueError(
            f"El término es anterior al inicio: {inicio} / {fin}"
        )

    return minutos


def cargar_objetivos(ruta):
    with open(ruta, encoding="utf-8") as archivo:
        datos = yaml.safe_load(archivo)

    if not isinstance(datos, dict):
        raise ValueError("El YAML debe contener un objeto.")

    if "contrato" not in datos or "metricas" not in datos:
        raise ValueError(
            "El YAML requiere 'contrato' y 'metricas'."
        )

    return datos


def cargar_mediciones(ruta):
    with open(
        ruta, encoding="utf-8-sig", newline=""
    ) as archivo:
        lector = csv.DictReader(archivo)

        columnas = set(lector.fieldnames or [])

        if not {"tipo", "metrica", "valor"}.issubset(columnas):
            raise ValueError(
                "El CSV requiere las columnas "
                "'tipo', 'metrica' y 'valor'."
            )

        return [
            {
                clave: (valor or "").strip()
                for clave, valor in fila.items()
                if clave is not None
            }
            for fila in lector
        ]


def campo(fila, nombre, defecto=""):
    return str(fila.get(nombre, defecto) or defecto).strip()


def es_valida(fila):
    return campo(fila, "valido", "si").lower() not in (
        "no", "false", "0", "excluido"
    )


def resultado_base(nombre, config):
    return {
        "metrica": nombre,
        "nombre": NOMBRES.get(nombre, nombre.title()),
        "objetivo": config.get("objetivo"),
        "operador": config.get("operador"),
        "unidad": config.get("unidad", ""),
        "medido": None,
        "cobertura": None,
        "veredicto": "evidencia insuficiente",
        "credito_porcentaje": 0,
        "clausula": config.get("clausula", ""),
        "observacion": "",
        "detalle": [],
    }


def comparar(valor, config):
    op = config["operador"]

    if op not in OPERADORES:
        raise ValueError(f"Operador no válido: {op}")

    return OPERADORES[op](
        valor,
        numero(config["objetivo"], "objetivo")
    )


def cobertura(muestras_validas, muestras_esperadas):
    if muestras_esperadas is None or muestras_esperadas <= 0:
        return None

    valor = 100 * muestras_validas / muestras_esperadas

    if valor < 0 or valor > 100.000001:
        raise ValueError("Cobertura fuera del rango 0-100 %")

    return min(100, valor)


def promedio(filas):
    valores = [numero(f["valor"]) for f in filas]
    return sum(valores) / len(valores)


def promedio_ponderado(filas):
    numerador = 0
    denominador = 0

    for fila in filas:
        cantidad = opcional(campo(fila, "muestras"), 1)

        if cantidad <= 0:
            raise ValueError("Muestras deben ser positivas.")

        numerador += numero(fila["valor"]) * cantidad
        denominador += cantidad

    return numerador / denominador


def credito_disponibilidad(valor, contrato):
    tramos = contrato.get("tramos_disponibilidad", [])

    for tramo in tramos:
        desde = numero(tramo["desde"])
        hasta = numero(tramo["hasta"])

        if desde <= valor < hasta:
            return numero(tramo["credito"])

    return 0


def verificar_fuente(fila, config):
    if not es_valida(fila):
        return False, "Registro marcado como inválido"

    metodo = campo(fila, "metodo").lower()
    esperado = str(config.get("herramienta", "")).lower()

    if esperado:
        if not metodo:
            return False, "No se indicó el método de medición"

        if esperado not in metodo:
            return False, "Método diferente al contratado"

    punto = campo(fila, "punto").lower()
    requerido = str(config.get("punto_medicion", "")).lower()

    if requerido:
        if not punto:
            return False, "No se indicó el punto de medición"

        # La equivalencia de puntos debe declararse
        # explícitamente, no suponerse.
        if punto != requerido:
            return False, "Punto de medición no acreditado"

    return True, "Fuente aceptada"


def evaluar_mediciones(nombre, config, filas, contrato):
    r = resultado_base(nombre, config)

    aceptadas = []

    for fila in filas:
        valida, motivo = verificar_fuente(fila, config)

        r["detalle"].append({
            "id": campo(fila, "id"),
            "aceptada": valida,
            "motivo": motivo,
        })

        if valida:
            aceptadas.append(fila)

    if not aceptadas:
        r["observacion"] = "Sin mediciones contractuales válidas."
        return r

    if nombre == "throughput":
        minimo = int(config.get("pruebas_minimas", 1))

        if len(aceptadas) < minimo:
            r["observacion"] = (
                f"Solo {len(aceptadas)} pruebas válidas; "
                f"se requieren {minimo}."
            )
            return r

        # La cantidad de pruebas se valida por separado:
        # no se exige un muestreo continuo a iperf3.
        valor = promedio(aceptadas)
        r["cobertura"] = 100.0

    else:
        if nombre == "perdida":
            dias = [
                opcional(campo(f, "dias_cubiertos"))
                for f in aceptadas
            ]

            if any(d is None for d in dias):
                r["observacion"] = (
                    "Faltan días de cobertura de pérdida."
                )
                return r

            cubiertos = sum(dias)
            esperados = numero(
                config.get("dias_periodo", 30)
            )

            porcentaje = cobertura(cubiertos, esperados)

        elif nombre == "jitter":
            dias = [
                opcional(campo(f, "dias_cubiertos"))
                for f in aceptadas
            ]

            if any(d is None for d in dias):
                r["observacion"] = (
                    "Faltan días de cobertura de jitter."
                )
                return r

            porcentaje = cobertura(
                sum(dias),
                numero(config.get("dias_periodo", 30))
            )

        else:
            esperadas = [
                opcional(campo(f, "esperadas"))
                for f in aceptadas
            ]

            muestras = [
                opcional(campo(f, "muestras"))
                for f in aceptadas
            ]

            if any(v is None for v in esperadas + muestras):
                r["observacion"] = (
                    "Faltan muestras válidas o esperadas."
                )
                return r

            porcentaje = cobertura(
                sum(muestras), sum(esperadas)
            )

        r["cobertura"] = round(porcentaje, 4)

        minimo = numero(
            config.get(
                "cobertura_minima",
                contrato.get("cobertura_minima", 90)
            )
        )

        if porcentaje < minimo:
            r["observacion"] = (
                f"Cobertura {porcentaje:.2f}% "
                f"inferior al mínimo {minimo:.2f}%."
            )
            return r

        estadistico = config.get("estadistico", "promedio")

        if estadistico == "promedio_ponderado":
            valor = promedio_ponderado(aceptadas)
        elif estadistico == "maximo":
            valor = max(numero(f["valor"]) for f in aceptadas)
        else:
            # Si hay muestras por intervalo, se pondera.
            if all(campo(f, "muestras") for f in aceptadas):
                valor = promedio_ponderado(aceptadas)
            else:
                valor = promedio(aceptadas)

    r["medido"] = round(valor, 4)

    if comparar(valor, config):
        r["veredicto"] = "cumple"
        r["observacion"] = "Cumple el objetivo contractual."
    else:
        r["veredicto"] = "no cumple"
        r["credito_porcentaje"] = numero(
            config.get("credito", 0)
        )
        r["observacion"] = "Incumplimiento acreditado."

    return r


def clasificar_eventos(filas, contrato):
    reglas = contrato.get("exclusiones", {})
    eventos = []
    mantenimiento_excluido = 0

    for fila in filas:
        inicio = campo(fila, "inicio")
        fin = campo(fila, "fin")

        duracion = minutos_entre(inicio, fin)

        if duracion is None:
            raise ValueError(
                f"Evento sin inicio o fin: {campo(fila, 'id')}"
            )

        causa = campo(fila, "causa").lower()
        origen = campo(fila, "origen").lower()
        aviso = campo(fila, "aviso")

        excluido = False
        motivo = ""
        clausula = ""

        if origen == "cliente" and reglas.get(
            "fallas_cliente", False
        ):
            excluido = True
            motivo = "Falla atribuible al cliente"
            clausula = "6.1.c"

        elif origen == "fuerza_mayor" and reglas.get(
            "fuerza_mayor_declarada", False
        ):
            excluido = True
            motivo = "Fuerza mayor declarada"
            clausula = "6.1.b"

        elif causa == "mantenimiento" and aviso:
            anticipacion = minutos_entre(aviso, inicio)

            minimo_aviso = numero(
                reglas.get("mantenimiento_aviso_horas", 72)
            ) * 60

            maximo = numero(
                reglas.get("mantenimiento_maximo_minutos", 240)
            )

            if (
                anticipacion >= minimo_aviso
                and mantenimiento_excluido + duracion <= maximo
            ):
                excluido = True
                mantenimiento_excluido += duracion
                motivo = "Mantenimiento programado válido"
                clausula = "6.1.a"
            else:
                motivo = (
                    "Mantenimiento sin requisitos de exclusión"
                )
                clausula = "6.1.a"

        else:
            motivo = "Indisponibilidad no excluida"
            clausula = "3.1 / 6.1"

        eventos.append({
            "id": campo(fila, "id"),
            "inicio": inicio,
            "fin": fin,
            "duracion_min": duracion,
            "origen": origen,
            "excluido": excluido,
            "motivo": motivo,
            "clausula": clausula,
        })

    return eventos


def evaluar_disponibilidad(config, eventos, contrato):
    r = resultado_base("disponibilidad", config)

    periodo = numero(
        config.get(
            "periodo_minutos",
            contrato.get("periodo_minutos")
        )
    )

    caida = sum(
        e["duracion_min"]
        for e in eventos
        if not e["excluido"]
    )

    excluido = sum(
        e["duracion_min"]
        for e in eventos
        if e["excluido"]
    )

    if caida > periodo:
        raise ValueError(
            "La indisponibilidad supera el período."
        )

    valor = (periodo - caida) / periodo * 100

    permitido = periodo * (
        1 - numero(config["objetivo"]) / 100
    )

    r["medido"] = round(valor, 4)
    r["cobertura"] = None

    r["detalle"] = eventos
    r["calculos"] = {
        "periodo_minutos": periodo,
        "indisponibilidad_atribuible_min": caida,
        "tiempo_excluido_min": excluido,
        "caida_permitida_min": round(permitido, 4),
        "exceso_min": round(max(0, caida - permitido), 4),
    }

    if not eventos:
        r["observacion"] = (
            "No se proporcionó registro de eventos ni "
            "evidencia de monitoreo completo."
        )
        return r

    # Los eventos entregados no prueban por sí solos
    # la cobertura completa del NMS. Se requiere
    # evidencia de integridad de registros.
    integridad = contrato.get(
        "registro_eventos_completo", False
    )

    if not integridad:
        r["observacion"] = (
            "Disponibilidad calculada con los eventos "
            "aportados; integridad del NMS no acreditada."
        )
        return r

    if comparar(valor, config):
        r["veredicto"] = "cumple"
        r["observacion"] = "Disponibilidad contractual cumplida."
    else:
        r["veredicto"] = "no cumple"
        r["credito_porcentaje"] = credito_disponibilidad(
            valor, contrato
        )
        r["observacion"] = (
            "Disponibilidad inferior al objetivo."
        )

    return r


def evaluar_tickets(nombre, config, tickets):
    r = resultado_base(nombre, config)

    if not tickets:
        r["observacion"] = "No se entregaron tickets."
        return r

    tiempos = []
    incompletos = 0

    for fila in tickets:
        origen = campo(fila, "origen").lower()

        if nombre == "mttr" and origen != "proveedor":
            continue

        if nombre == "respuesta":
            duracion = minutos_entre(
                campo(fila, "apertura"),
                campo(fila, "respuesta")
            )
            unidad = "min"
        else:
            duracion_min = minutos_entre(
                campo(fila, "inicio"),
                campo(fila, "fin")
            )
            duracion = (
                duracion_min / 60
                if duracion_min is not None
                else None
            )
            unidad = "h"

        if duracion is None:
            incompletos += 1
            r["detalle"].append({
                "id": campo(fila, "id"),
                "veredicto": "evidencia insuficiente",
            })
            continue

        tiempos.append(duracion)

        r["detalle"].append({
            "id": campo(fila, "id"),
            "tiempo": round(duracion, 4),
            "unidad": unidad,
            "veredicto": (
                "cumple"
                if comparar(duracion, config)
                else "no cumple"
            ),
        })

    if not tiempos:
        r["observacion"] = (
            "No existen tiempos válidos para evaluar."
        )
        return r

    r["medido"] = round(max(tiempos), 4)

    if incompletos:
        r["observacion"] = (
            f"{incompletos} ticket(s) sin datos suficientes."
        )
        return r

    if all(comparar(t, config) for t in tiempos):
        r["veredicto"] = "cumple"
        r["observacion"] = (
            "Todos los tickets evaluados cumplen."
        )
    else:
        r["veredicto"] = "no cumple"
        r["credito_porcentaje"] = numero(
            config.get("credito", 0)
        )
        r["observacion"] = (
            "Existe al menos un ticket fuera del objetivo."
        )

    return r


def disponibilidad_infraestructura(contrato):
    componentes = contrato.get("infraestructura", {})

    claves = ("cpe", "fibra", "pe", "backbone")

    if not all(k in componentes for k in claves):
        return None

    valores = {
        k: numero(componentes[k]) / 100
        for k in claves
    }

    serie = (
        valores["cpe"]
        * valores["fibra"]
        * valores["pe"]
        * valores["backbone"]
    )

    resultado = {
        "serie_porcentaje": round(serie * 100, 6),
    }

    if "radio" in componentes:
        radio = numero(componentes["radio"]) / 100

        acceso = 1 - (
            (1 - valores["fibra"]) * (1 - radio)
        )

        total = (
            valores["cpe"]
            * acceso
            * valores["pe"]
            * valores["backbone"]
        )

        resultado["acceso_redundante_porcentaje"] = round(
            acceso * 100, 6
        )
        resultado["total_con_respaldo_porcentaje"] = round(
            total * 100, 6
        )

    resultado["supuesto"] = (
        "Fallas independientes y respaldo operativo. "
        "Estimación, no medición contractual."
    )

    return resultado


def evaluar(objetivos, mediciones):
    contrato = objetivos["contrato"]
    metricas = objetivos["metricas"]

    grupos = defaultdict(list)

    for fila in mediciones:
        grupos[campo(fila, "tipo").lower()].append(fila)

    eventos = clasificar_eventos(
        grupos["evento"], contrato
    )

    resultados = []

    for nombre, config in metricas.items():
        if nombre == "disponibilidad":
            r = evaluar_disponibilidad(
                config, eventos, contrato
            )

        elif nombre in ("respuesta", "mttr"):
            r = evaluar_tickets(
                nombre, config, grupos["ticket"]
            )

        else:
            filas = [
                f for f in grupos["medicion"]
                if campo(f, "metrica").lower() == nombre
            ]

            r = evaluar_mediciones(
                nombre, config, filas, contrato
            )

        resultados.append(r)

    suma_creditos = sum(
        r["credito_porcentaje"] for r in resultados
    )

    tope = numero(contrato.get("tope_credito", 50))
    cargo = numero(contrato.get("cargo_mensual", 0))

    aplicable = min(suma_creditos, tope)

    estados = {
        estado: sum(
            r["veredicto"] == estado
            for r in resultados
        )
        for estado in ESTADOS
    }

    if estados["no cumple"]:
        global_estado = "no cumple"
    elif estados["evidencia insuficiente"]:
        global_estado = "evidencia insuficiente"
    else:
        global_estado = "cumple"

    return {
        "plataforma": "SLA Toolkit Pro",
        "cliente": contrato.get("cliente", ""),
        "proveedor": contrato.get("proveedor", ""),
        "servicio": contrato.get("servicio", ""),
        "periodo": contrato.get("periodo", ""),
        "veredicto_global": global_estado,
        "resultados": resultados,
        "resumen": estados,
        "infraestructura": disponibilidad_infraestructura(
            contrato
        ),
        "creditos": {
            "cargo_mensual_clp": cargo,
            "suma_porcentaje": suma_creditos,
            "tope_porcentaje": tope,
            "aplicable_porcentaje": aplicable,
            "monto_clp": round(cargo * aplicable / 100),
        },
        "advertencia": (
            "Los resultados dependen de la integridad "
            "y validez de la evidencia ingresada."
        ),
    }


def mostrar(reporte):
    print("=" * 64)
    print("                     SLA TOOLKIT PRO")
    print("               NETWORK ASSURANCE PLATFORM")
    print("=" * 64)

    print(f"Cliente:   {reporte['cliente']}")
    print(f"Proveedor: {reporte['proveedor']}")
    print(f"Servicio:  {reporte['servicio']}")
    print(f"Período:   {reporte['periodo']}")
    print("-" * 64)

    for r in reporte["resultados"]:
        print(f"\n{r['nombre'].upper()}")
        print(
            f"Objetivo: {r['operador']} "
            f"{r['objetivo']} {r['unidad']}"
        )
        print(f"Medido:   {r['medido']}")
        print(f"Cobertura: {r['cobertura']}")
        print(f"Estado:   {r['veredicto'].upper()}")
        print(f"Detalle:  {r['observacion']}")
        print(
            f"Crédito:  {r['credito_porcentaje']}%"
        )

    print("\n" + "=" * 64)
    print("RESULTADO GLOBAL")
    print(reporte["veredicto_global"].upper())

    credito = reporte["creditos"]

    print("\nCRÉDITOS DE SERVICIO")
    print(f"Suma: {credito['suma_porcentaje']:.2f}%")
    print(f"Tope: {credito['tope_porcentaje']:.2f}%")
    print(
        f"Aplicable: "
        f"{credito['aplicable_porcentaje']:.2f}%"
    )
    print(f"Monto: ${credito['monto_clp']:,.0f} CLP")

    print("=" * 64)


def main():
    parser = argparse.ArgumentParser(
        description="SLA Toolkit Pro - Evaluación SLA"
    )

    parser.add_argument(
        "-o", "--objetivos", required=True
    )
    parser.add_argument(
        "-m", "--mediciones", required=True
    )
    parser.add_argument(
        "--json", action="store_true"
    )
    parser.add_argument(
        "--salida", help="Guardar reporte JSON"
    )

    args = parser.parse_args()

    try:
        objetivos = cargar_objetivos(args.objetivos)
        mediciones = cargar_mediciones(args.mediciones)

        reporte = evaluar(objetivos, mediciones)

        if args.salida:
            Path(args.salida).write_text(
                json.dumps(
                    reporte,
                    ensure_ascii=False,
                    indent=2
                ),
                encoding="utf-8"
            )

        if args.json:
            print(json.dumps(
                reporte,
                ensure_ascii=False,
                indent=2
            ))
        else:
            mostrar(reporte)

    except (
        ValueError, KeyError, OSError, yaml.YAMLError
    ) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
