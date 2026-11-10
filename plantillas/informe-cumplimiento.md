# Informe técnico de verificación de SLA

## 01. Identificación

**Asignatura:** [Completar]

**Sección:** [Completar]

**Docente:** [Completar]

**Integrantes:** [Completar]

**Fecha:** [Completar]

**Repositorio GitHub:** [Enlace]

**Cliente:** [Completar]

**Proveedor:** [Completar]

**Servicio contratado:** [Completar]

**Período evaluado:** [Fecha inicial y final]

**Duración del período:** [Días y minutos]

**Punto de demarcación:** [Completar]

## 02. Resumen ejecutivo

[Redactar entre tres y cinco líneas con el resultado general de la evaluación. Indicar los indicadores incumplidos, los valores obtenidos, el crédito correspondiente en porcentaje y su monto en pesos.]

## 03. Alcance y referencias

La evaluación considera las condiciones establecidas en el contrato SLA y las mediciones correspondientes al período indicado.

**Cláusulas evaluadas:** [Identificar cláusulas de disponibilidad, rendimiento y atención de incidentes]

**Condiciones de validez:** [Indicar cláusula y cobertura mínima]

**Exclusiones:** [Indicar cláusulas aplicables]

**Créditos:** [Indicar tramos, porcentajes y límite contractual]

**Referencias técnicas:** ITU-T Y.1540, RFC 3393, RFC 5357 y RFC 6349, según corresponda al servicio.

## 04. Metodología

### 4.1 Indicadores y condiciones de medición

Para cada indicador registrar:

- Métrica y unidad.
- Operador de comparación y umbral contractual.
- Período evaluado.
- Punto de medición.
- Herramienta utilizada.
- Estadístico exigido por el contrato.

### 4.2 Revisión de evidencias

**Fuente:** [Identificar registro o anexo]

**Medición realizada:** [Completar]

**Validez:** [Aceptada o descartada]

**Fundamento:** [Explicar si cumple el punto, método, período y estadístico contratado]

Repetir la revisión para cada fuente utilizada.

### 4.3 Cobertura de mediciones

Cobertura (%) = (Muestras válidas / Muestras esperadas) x 100

**Muestras esperadas:** [Valor]

**Muestras válidas:** [Valor]

**Cálculo:** [Reemplazo de valores]

**Resultado:** [Porcentaje]

**Cobertura mínima contractual:** [Porcentaje]

**Conclusión:** [Válida o insuficiente]

### 4.4 Información faltante

Registrar los datos no disponibles, el indicador afectado y la evidencia necesaria para completar la evaluación.

## 05. Resultados

### 5.1 Clasificación de interrupciones

Para cada evento registrar:

**Evento:** [Identificador]

**Fecha:** [Completar]

**Inicio:** [Hora]

**Término:** [Hora]

**Duración:** [Minutos]

**Causa:** [Completar]

**Clasificación:** [Atribuible al proveedor o excluido]

**Cláusula aplicada:** [Completar]

**Fundamento:** [Completar]

### 5.2 Disponibilidad

**Tiempo total del período:** [Minutos]

**Tiempo de indisponibilidad atribuible:** [Minutos]

**Tiempo excluido:** [Minutos]

Disponibilidad (%) = ((Tiempo total - Indisponibilidad atribuible) / Tiempo total) x 100

**Reemplazo:** [Completar]

**Disponibilidad obtenida:** [Porcentaje]

**Objetivo contratado:** [Porcentaje]

**Caída máxima permitida:** [Minutos]

**Exceso de indisponibilidad:** [Minutos]

**Veredicto:** [Cumple / No cumple / Evidencia insuficiente]

### 5.3 Latencia

**Fuente:** [Completar]

**Método y punto de medición:** [Completar]

**Muestras esperadas:** [Valor]

**Muestras válidas:** [Valor]

**Cobertura:** [Porcentaje]

**RTT promedio:** [ms]

**Objetivo:** [ms]

**Veredicto:** [Completar]

### 5.4 Jitter

Cuando existan varios períodos con distinta cantidad de muestras, calcular el promedio ponderado.

Jitter promedio = Suma de (muestras válidas x jitter promedio del período) / Total de muestras válidas

**Datos utilizados:** [Indicar muestras y promedios por período]

**Reemplazo:** [Desarrollar operación]

**Resultado:** [ms]

**Objetivo:** [ms]

**Cobertura:** [Porcentaje]

**Veredicto:** [Completar]

### 5.5 Pérdida de paquetes

**Fuente:** [Completar]

**Pérdida registrada:** [%]

**Período cubierto:** [Completar]

**Cobertura:** [%]

**Objetivo:** [%]

**Validez de la evidencia:** [Completar]

**Veredicto:** [Completar]

### 5.6 Throughput

**Herramienta:** [Completar]

**Punto de medición:** [Completar]

**Cantidad de pruebas válidas:** [Valor]

Throughput promedio = Suma de resultados válidos / Número de pruebas válidas

**Reemplazo:** [Completar]

**Promedio obtenido:** [Mbps]

**Mínimo contratado:** [Mbps]

**Veredicto:** [Completar]

### 5.7 Tiempo de respuesta

Para cada ticket registrar la hora de apertura, la primera respuesta y el tiempo transcurrido en minutos.

Tiempo de respuesta = Hora de primera respuesta - Hora de apertura

**Objetivo contractual:** [Minutos]

**Resultado por ticket:** [Completar]

**Veredicto:** [Completar]

### 5.8 Tiempo de reparación

Para cada incidente atribuible al proveedor, determinar el tiempo de reparación según las condiciones del contrato y los registros disponibles.

**Incidente:** [Completar]

**Inicio:** [Completar]

**Restablecimiento:** [Completar]

**Duración:** [Horas y minutos]

**Límite contractual:** [Horas]

**Veredicto:** [Completar]

### 5.9 Resumen de cumplimiento

| Indicador | Objetivo | Resultado | Desviación | Fuente | Veredicto | Crédito |
|---|---|---|---|---|---|---|
| Disponibilidad | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Latencia | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Jitter | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Pérdida | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Throughput | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Tiempo de respuesta | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| MTTR | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

## 06. Análisis de incumplimientos

Para cada incumplimiento identificado, documentar:

**Indicador afectado:** [Completar]

**Fecha o período:** [Completar]

**Incumplimiento:** [Describir el valor obtenido y el límite contractual]

**Causa:** [Completar]

**Origen:** [Proveedor o cliente]

**Impacto operacional:** [Completar según los antecedentes disponibles]

**Evidencia:** [Anexo, ticket o registro]

**Cláusula:** [Completar]

## 07. Conclusiones técnicas

### 7.1 Veredicto

[Indicar el resultado global y distinguir indicadores cumplidos, incumplidos y aquellos que presentan evidencia insuficiente.]

### 7.2 Crédito de servicio

**Cargo mensual:** [$]

**Crédito por disponibilidad:** [%]

**Otros créditos aplicables:** [%]

**Suma de créditos:** [%]

**Tope contractual:** [%]

**Crédito final:** [%]

Crédito ($) = Cargo mensual x Porcentaje de crédito aplicable / 100

**Reemplazo:** [Completar]

**Monto final:** [$]

### 7.3 Viabilidad de la disponibilidad contratada

**Infraestructura actual:**

Disponibilidad en serie = A1 x A2 x ... x An

**Reemplazo:** [Completar]

**Resultado:** [%]

**Alternativa con respaldo:**

Disponibilidad en paralelo = 1 - (1 - A1) x (1 - A2)

**Reemplazo:** [Completar]

**Disponibilidad total de la alternativa:** [%]

**Evaluación:** [Comparar con el objetivo contratado e indicar las condiciones consideradas]

### 7.4 Respuesta al cliente

Revisar cada afirmación presentada por el cliente.

**Afirmación:** [Completar]

**Resultado de la revisión:** [Se sostiene / No se sostiene / No existe evidencia suficiente]

**Fundamento técnico:** [Indicar cálculo, cláusula y fuente]

## 08. Recomendaciones

| Hallazgo | Recomendación | Mejora esperada | Prioridad |
|---|---|---|---|
| [Completar] | [Completar] | [Completar] | [Alta/Media/Baja] |

Las recomendaciones deben estar relacionadas con los hallazgos comprobados durante la evaluación.

## 09. Automatización del proceso

### 9.1 Archivos utilizados

**Contrato:** `sla.md`

**Objetivos:** `objetivos.yaml`

**Mediciones:** `mediciones.csv`

**Calculadora:** `herramientas/calc_sla.py`

**Salida:** `salida_calc.txt`

**Informe:** `informe.md`

**PDF:** `informe.pdf`

### 9.2 Procedimiento

1. Registrar los objetivos contractuales en el archivo YAML.
2. Incorporar las mediciones del período en el CSV.
3. Ejecutar la calculadora de cumplimiento.
4. Revisar los veredictos y créditos obtenidos.
5. Documentar los cálculos que requieran desarrollo manual.
6. Completar el informe con los resultados verificados.
7. Generar el PDF y registrar la versión del repositorio.

### 9.3 Comandos de ejecución

Registrar los comandos utilizados para ejecutar la calculadora y generar el informe.

**Comando de cálculo:** [Completar]

**Comando de generación del informe:** [Completar]

**Comando de conversión a PDF:** [Completar]

**Versión del repositorio:** [Tag]

### 9.4 Uso de inteligencia artificial

**Herramienta utilizada:** [Completar si corresponde]

**Etapa en que se utilizó:** [Completar]

**Archivos proporcionados como contexto:** [Completar]

**Revisión realizada por el grupo:** [Completar]

**Verificación de resultados:** [Indicar cómo se contrastaron las cifras con la calculadora y los cálculos manuales]

## Anexos

**Anexo A.** Contenido del archivo `objetivos.yaml`.

**Anexo B.** Contenido del archivo `mediciones.csv`.

**Anexo C.** Salida completa de `calc_sla.py`.

**Anexo D.** Desarrollo de cálculos manuales.

**Anexo E.** Extracto del historial de commits y `CHANGELOG.md`.
