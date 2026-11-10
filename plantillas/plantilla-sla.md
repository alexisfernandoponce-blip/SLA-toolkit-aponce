# Plantilla de Acuerdo de Nivel de Servicio (SLA)

## 1. Identificación del servicio

**Cliente:** [Nombre de la empresa]

**Proveedor:** [Nombre del proveedor]

**Servicio contratado:** [Tipo de servicio]

**Ubicación:** [Dirección o instalación]

**Código de contrato:** [Identificador]

**Fecha de inicio:** [DD/MM/AAAA]

**Vigencia:** [Período contratado]

**Responsable del cliente:** [Nombre y cargo]

**Responsable del proveedor:** [Nombre y cargo]

## 2. Descripción y alcance

**Descripción del servicio:**

[Indicar las características del servicio contratado, su finalidad y los recursos incluidos.]

**Capacidad contratada:** [Mbps o Gbps]

**Tipo de conexión:** [Fibra óptica, radioenlace u otra]

**Modalidad:** [Dedicado o compartido]

**Dirección del servicio:** [Simétrico o asimétrico]

**Punto de demarcación:** [Interfaz o equipo donde termina la responsabilidad del proveedor]

**Horario de operación:** [24/7 u horario definido]

**Equipos incluidos:** [CPE, router, ONT u otros]

**Servicios excluidos del alcance:** [Indicar si corresponde]

## 3. Requisitos del cliente

Registrar los requisitos identificados durante el levantamiento del servicio.

**Aplicaciones principales:** [Completar]

**Necesidades de conectividad:** [Completar]

**Disponibilidad requerida:** [Completar]

**Requisitos de rendimiento:** [Completar]

**Horario crítico de operación:** [Completar]

**Condiciones especiales:** [Completar]

Estos antecedentes se utilizarán para definir los indicadores y objetivos del SLA.

## 4. Indicadores y objetivos de servicio

Completar los valores acordados entre el cliente y el proveedor.

| Indicador | Objetivo contratado | Unidad |
|---|---|---|
| Disponibilidad mensual | [Valor] | % |
| Latencia | [Valor máximo] | ms |
| Jitter | [Valor máximo] | ms |
| Pérdida de paquetes | [Valor máximo] | % |
| Throughput | [Valor mínimo] | Mbps |
| Tiempo de respuesta | [Valor máximo] | minutos |
| Tiempo de reparación | [Valor máximo] | horas |

**Período de evaluación:** [Mensual u otro]

**Cobertura mínima de mediciones:** [Porcentaje]

**Criterio de cumplimiento:** [Indicar si se evalúa promedio, máximo, percentil o cada incidente]

## 5. Procedimientos de medición

### Disponibilidad

**Método:** [Indicar procedimiento]

**Punto de medición:** [Completar]

**Período:** [Completar]

**Tratamiento de exclusiones:** [Completar]

### Latencia

**Herramienta o protocolo:** [ICMP, TWAMP u otro]

**Origen y destino:** [Completar]

**Frecuencia de medición:** [Completar]

**Estadístico utilizado:** [Promedio, máximo o percentil]

### Jitter y pérdida de paquetes

**Herramienta o protocolo:** [Completar]

**Puntos de medición:** [Completar]

**Frecuencia:** [Completar]

**Criterio de validez:** [Completar]

### Throughput

**Herramienta:** [Completar]

**Protocolo:** [TCP o UDP]

**Cantidad de pruebas:** [Completar]

**Punto de medición:** [Completar]

**Criterio de evaluación:** [Completar]

## 6. Atención de incidentes

**Canal de atención:** [Teléfono, correo o plataforma de tickets]

**Horario de soporte:** [Completar]

**Tiempo máximo de primera respuesta:** [Completar]

**Tiempo máximo de reparación:** [Completar]

**Procedimiento de escalamiento:** [Completar]

**Responsable del seguimiento:** [Completar]

Para cada incidente se deberá registrar el número de ticket, fecha y hora de apertura, descripción de la falla, primera respuesta, acciones realizadas y fecha y hora de restablecimiento.

## 7. Mantenimientos y exclusiones

**Aviso previo para mantenimiento programado:** [Completar]

**Duración máxima permitida:** [Completar]

**Condiciones para excluir una interrupción:** [Completar]

**Eventos de fuerza mayor:** [Completar]

**Fallas atribuibles al cliente:** [Completar]

**Tratamiento del tiempo excluido en el cálculo de disponibilidad:** [Completar]

Las exclusiones deberán contar con antecedentes que permitan verificar su aplicación según las condiciones del contrato.

## 8. Créditos por incumplimiento

**Cargo mensual del servicio:** [$ Valor y moneda]

**Base de cálculo:** [Cargo neto u otra condición contractual]

**Crédito por incumplimiento de disponibilidad:** [Porcentaje o escala acordada]

**Crédito por incumplimiento de otros indicadores:** [Completar]

**Crédito máximo acumulable:** [Porcentaje]

**Procedimiento para solicitar o aplicar créditos:** [Completar]

Los créditos se calcularán únicamente cuando el incumplimiento esté respaldado por evidencia válida y corresponda según las cláusulas del SLA.

## 9. Seguimiento y revisión

**Frecuencia de entrega de informes:** [Completar]

**Responsable de las mediciones:** [Completar]

**Responsable de revisar el cumplimiento:** [Completar]

**Período de conservación de registros:** [Completar]

**Frecuencia de revisión del SLA:** [Completar]

**Procedimiento para modificar objetivos:** [Completar]

Las revisiones permitirán identificar incumplimientos, analizar sus causas y acordar medidas correctivas cuando corresponda.

## 10. Referencias técnicas

Seleccionar las referencias aplicables al servicio contratado.

- ITIL 4 - Service Level Management.
- ISO/IEC 20000-1.
- ITU-T E.860.
- ITU-T Y.1540 y Y.1541.
- MEF 10.4.
- RFC 7679, 7680, 3393, 5357 y 6349.
- ITU-T G.114.
- Otras referencias: [Completar].

Las referencias técnicas se utilizarán según el tipo de servicio y el procedimiento de medición acordado.

## 11. Aprobación del acuerdo

**Por el cliente**

Nombre: [Completar]

Cargo: [Completar]

Firma: [Completar]

Fecha: [Completar]

**Por el proveedor**

Nombre: [Completar]

Cargo: [Completar]

Firma: [Completar]

Fecha: [Completar]
