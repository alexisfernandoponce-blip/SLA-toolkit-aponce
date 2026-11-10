# Checklist de levantamiento de requisitos SLA

## 1. Datos del cliente

- [ ] Nombre de la empresa y RUT.
- [ ] Ubicación donde se entregará el servicio.
- [ ] Nombre y contacto del responsable técnico.
- [ ] Nombre y contacto del responsable del contrato.
- [ ] Proveedor del servicio.
- [ ] Fecha de inicio y vigencia del contrato.

## 2. Características del servicio

- [ ] Identificar el tipo de servicio contratado.
- [ ] Registrar la capacidad de subida y bajada en Mbps.
- [ ] Confirmar si el enlace es dedicado o compartido.
- [ ] Identificar la tecnología de acceso.
- [ ] Registrar la dirección IP o bloque asignado, cuando corresponda.
- [ ] Identificar el equipo CPE y su ubicación.
- [ ] Definir el punto de demarcación entre cliente y proveedor.
- [ ] Registrar los equipos y servicios incluidos en el contrato.

## 3. Requisitos de operación

- [ ] Identificar las aplicaciones que utilizan el enlace.
- [ ] Determinar los horarios críticos de funcionamiento.
- [ ] Registrar los servicios que requieren conectividad permanente.
- [ ] Identificar aplicaciones sensibles a latencia, jitter o pérdida de paquetes.
- [ ] Confirmar si existe un enlace de respaldo.
- [ ] Verificar si el CPE dispone de respaldo eléctrico.
- [ ] Establecer las responsabilidades del cliente y del proveedor.

## 4. Indicadores y objetivos del SLA

- [ ] Definir disponibilidad mínima y período de evaluación.
- [ ] Definir latencia máxima y el estadístico utilizado.
- [ ] Definir jitter máximo permitido.
- [ ] Definir pérdida de paquetes máxima.
- [ ] Establecer throughput mínimo exigido.
- [ ] Definir tiempo máximo de primera respuesta.
- [ ] Definir tiempo máximo de reparación.
- [ ] Confirmar unidades, operadores de comparación y umbrales de cada indicador.
- [ ] Registrar los objetivos acordados con el cliente.

## 5. Procedimientos de medición

- [ ] Identificar el origen y destino de las mediciones.
- [ ] Definir la herramienta utilizada para cada indicador.
- [ ] Establecer la frecuencia de medición.
- [ ] Definir el período de evaluación.
- [ ] Establecer la cantidad mínima de pruebas requeridas.
- [ ] Definir la cobertura mínima de datos válidos.
- [ ] Determinar cómo se tratarán las muestras faltantes.
- [ ] Confirmar que las mediciones se realicen desde el punto contractual.
- [ ] Establecer cómo se almacenarán los registros y resultados.

## 6. Gestión de incidentes

- [ ] Identificar los canales de atención del proveedor.
- [ ] Confirmar el horario de soporte.
- [ ] Definir el procedimiento para abrir tickets.
- [ ] Registrar el tiempo máximo de primera respuesta.
- [ ] Establecer el tiempo máximo de reparación.
- [ ] Definir los responsables del seguimiento.
- [ ] Establecer el procedimiento de escalamiento.
- [ ] Confirmar cómo se registrarán las causas y tiempos de cada incidente.

## 7. Mantenimientos y exclusiones

- [ ] Establecer el plazo mínimo de aviso para mantenimientos.
- [ ] Definir la duración máxima de mantenimiento excluible.
- [ ] Identificar las condiciones de fuerza mayor.
- [ ] Registrar las fallas que son responsabilidad del cliente.
- [ ] Definir cómo se contabilizará el tiempo excluido.
- [ ] Establecer la evidencia necesaria para justificar una exclusión.

## 8. Créditos de servicio

- [ ] Registrar el cargo mensual y su moneda.
- [ ] Definir los porcentajes de crédito por disponibilidad.
- [ ] Definir créditos por incumplimiento de otros indicadores.
- [ ] Establecer el límite máximo acumulable.
- [ ] Confirmar si los créditos se calculan sobre el cargo neto.
- [ ] Definir el procedimiento para solicitar y aplicar los créditos.

## 9. Revisión y aprobación

- [ ] Confirmar que los requisitos del cliente estén documentados.
- [ ] Verificar que cada indicador tenga un objetivo medible.
- [ ] Revisar que los procedimientos de medición estén definidos.
- [ ] Confirmar que las responsabilidades estén establecidas.
- [ ] Revisar las condiciones de exclusión y compensación.
- [ ] Obtener la aprobación del cliente y del proveedor.

## 10. Registro del levantamiento

**Cliente:** [Completar]

**Servicio:** [Completar]

**Fecha:** [DD/MM/AAAA]

**Responsable del levantamiento:** [Completar]

**Observaciones:** [Registrar requisitos pendientes, diferencias detectadas o acuerdos por confirmar]

**Estado:** [Completo / Pendiente]

## Referencias

Pauta Toolkit SLA, INACAP La Serena, puntos 4.2 y 4.4.

ITIL 4 - Service Level Management.

ISO/IEC 20000-1.

ITU-T E.860.

Documentación del método de diseño en `docs/metodo.md`.
