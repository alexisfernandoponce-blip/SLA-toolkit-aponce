# Método de diseño de acuerdos de nivel de servicio (SLA)

**Toolkit SLA — INACAP La Serena**

## 1. Objetivo

Establecer un procedimiento técnico de seis pasos para diseñar acuerdos de nivel de servicio (SLA) en redes de telecomunicaciones, utilizando criterios de gestión, medición, viabilidad y verificación.

El método se fundamenta en ITIL 4 (Service Level Management), ITU-T E.860 e ISO/IEC 20000-1, complementándose con normas de medición de calidad de servicio.

## 2. Método de diseño en seis pasos

### Paso 1. Definir el servicio

**Qué se hace:** Se identifica el servicio de telecomunicaciones contratado, el proveedor, el cliente, el alcance técnico y el punto de demarcación donde termina la responsabilidad del proveedor.

**Norma de referencia:** ITU-T E.860.

**Producto generado:** Ficha de identificación del servicio, incluyendo capacidad contratada, ubicación y demarcación.

### Paso 2. Levantar los requisitos del cliente (SLR)

**Qué se hace:** Se identifican las necesidades operacionales del cliente, los servicios críticos y las consecuencias de una interrupción o degradación.

**Norma de referencia:** ITIL 4 — Service Level Management.

**Producto generado:** Documento de requisitos de nivel de servicio (SLR) y checklist de levantamiento.

### Paso 3. Elegir las métricas (SLI)

**Qué se hace:** Se seleccionan indicadores medibles, incluyendo disponibilidad, latencia, jitter, pérdida de paquetes y throughput.

Cada métrica debe tener unidad, método de medición, herramienta, punto de observación y período definido.

**Normas de referencia:**
- ITU-T Y.1540 / Y.1541: parámetros de rendimiento de redes IP.
- RFC 7679 / RFC 7680: mediciones de retardo y pérdida unidireccionales.
- RFC 3393: variación del retardo.
- RFC 5357: protocolo TWAMP.
- RFC 6349: metodología de pruebas de throughput TCP.
- MEF 10.4: atributos de servicio Ethernet.

**Producto generado:** Matriz de indicadores SLI con sus métodos de medición.

### Paso 4. Fijar objetivos viables (SLO)

**Qué se hace:** Se determinan los umbrales de calidad comprometidos, verificando previamente las capacidades reales de la infraestructura.

Se consideran cálculos de disponibilidad de componentes en serie y paralelo, redundancia, tiempos de indisponibilidad y latencia física.

**Normas de referencia:** ITU-T Y.1540 / Y.1541 e ITU-T E.860.

**Producto generado:** Matriz de objetivos SLO técnicamente justificados.

### Paso 5. Definir operación y medición

**Qué se hace:** Se establecen los procedimientos de monitoreo, períodos de evaluación, herramientas, exclusiones, tiempos de respuesta, MTTR, escalamiento de incidentes y reportes.

Se debe especificar cómo se valida la evidencia y cómo se determina el cumplimiento de cada objetivo.

**Normas de referencia:** ITIL 4, ISO/IEC 20000-1 y normas de medición aplicables.

**Producto generado:** Plan de operación, monitoreo y verificación del SLA.

### Paso 6. Definir consecuencias y revisión

**Qué se hace:** Se establecen las consecuencias de incumplimiento, los créditos de servicio, los límites contractuales y el procedimiento de revisión periódica.

Se aplica un enfoque de mejora continua mediante el ciclo PDCA: planificar, hacer, verificar y actuar.

**Normas de referencia:** ITIL 4, ITU-T E.860 e ISO/IEC 20000-1.

**Producto generado:** Acuerdo SLA con cláusulas de revisión, créditos y mejora continua.

## 3. Regla fundamental

No se debe comprometer un objetivo de nivel de servicio que la infraestructura no pueda cumplir o que no sea posible medir mediante un procedimiento verificable.

## 4. Aplicación del método

Este método se utilizará en el toolkit como base para elaborar plantillas, definir objetivos, analizar mediciones y generar informes técnicos de cumplimiento.

Su aplicación al caso Agrícola Valle de Elqui SpA se documentará por separado en el directorio `ejemplos/caso-valle-elqui/`.

## 5. Referencias

- ITIL 4 — Service Level Management.
- ITU-T E.860.
- ISO/IEC 20000-1.
- ITU-T Y.1540 / Y.1541.
- MEF 10.4.
- RFC 7679, RFC 7680, RFC 3393, RFC 5357 y RFC 6349.

**Fuente académica:** Pauta_Toolkit_SLA, secciones 2, 3 y 4.2; material de apoyo SLA y niveles de servicio en redes.
