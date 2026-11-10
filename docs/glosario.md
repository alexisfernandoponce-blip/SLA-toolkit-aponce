# Glosario de términos SLA

## 1. Introducción

Este glosario reúne los principales conceptos utilizados en el diseño, medición y evaluación de acuerdos de nivel de servicio en telecomunicaciones.

Las definiciones se utilizarán como referencia para las plantillas, fórmulas, herramientas de cálculo y el informe de cumplimiento del caso de estudio.

## 2. Términos y definiciones

### SLA - Service Level Agreement

Acuerdo de nivel de servicio entre un proveedor y un cliente. Establece las características del servicio contratado, los indicadores que se evaluarán, los niveles de cumplimiento exigidos y las condiciones aplicables ante incumplimientos.

### SLI - Service Level Indicator

Indicador utilizado para medir el comportamiento de un servicio. Puede corresponder a disponibilidad, latencia, jitter, pérdida de paquetes, throughput o tiempos de atención.

### SLO - Service Level Objective

Objetivo que debe alcanzar un indicador de servicio. Por ejemplo, una disponibilidad mensual igual o superior al 99,9 %.

### SLR - Service Level Requirement

Requisito de nivel de servicio definido a partir de las necesidades del cliente. Se utiliza como base para establecer los objetivos que posteriormente quedarán incluidos en el SLA.

### OLA - Operational Level Agreement

Acuerdo operativo interno entre equipos o áreas de una organización. Define responsabilidades y tiempos de atención necesarios para cumplir los compromisos establecidos en el SLA.

### MTBF - Mean Time Between Failures

Tiempo medio entre fallas de un sistema reparable. Se calcula utilizando el tiempo de funcionamiento y la cantidad de fallas registradas durante el período de análisis.

MTBF = Tiempo de funcionamiento / Número de fallas

### MTTR - Mean Time To Repair

Tiempo medio de reparación. Representa el promedio de tiempo necesario para restablecer un servicio después de una falla.

MTTR = Tiempo total de reparación / Número de fallas

En un contrato SLA también puede establecerse un tiempo máximo de reparación por incidente, que debe evaluarse según la definición contractual.

### Disponibilidad

Porcentaje del período de evaluación durante el cual el servicio se encuentra operativo.

Disponibilidad (%) = (Tiempo total - Tiempo de indisponibilidad) / Tiempo total x 100

Para calcularla se deben considerar las exclusiones y condiciones establecidas en el contrato.

### Indisponibilidad

Tiempo durante el cual el servicio no cumple las condiciones de funcionamiento establecidas en el SLA.

No todas las interrupciones necesariamente se consideran incumplimientos, ya que pueden existir exclusiones contractuales.

### Latencia

Tiempo que tarda la información en desplazarse entre dos puntos de una red. Puede medirse en una dirección o como tiempo de ida y vuelta.

Su unidad habitual es el milisegundo (ms).

### RTT - Round Trip Time

Tiempo que tarda un paquete en viajar desde el origen hasta el destino y regresar.

Se utiliza habitualmente en pruebas ICMP mediante ping.

### Jitter

Variación del retardo entre paquetes transmitidos por una red.

Un jitter elevado puede afectar aplicaciones de tiempo real, especialmente voz y video.

Se expresa habitualmente en milisegundos (ms).

### Pérdida de paquetes

Porcentaje de paquetes que no llegan a su destino durante una medición.

Pérdida (%) = Paquetes perdidos / Paquetes enviados x 100

### Throughput

Cantidad de datos transferidos efectivamente por una conexión durante un intervalo de tiempo.

Se expresa habitualmente en Mbps o Gbps y puede ser inferior a la capacidad nominal del enlace.

### Ancho de banda

Capacidad de transmisión asignada a un enlace o servicio de comunicaciones.

En el caso de un enlace dedicado de 200 Mbps simétricos, se dispone de una capacidad nominal de 200 Mbps en cada sentido.

### QoS - Quality of Service

Conjunto de mecanismos y parámetros utilizados para gestionar la calidad de transmisión de una red, considerando aspectos como retardo, pérdida de paquetes y prioridad del tráfico.

### CPE - Customer Premises Equipment

Equipo de comunicaciones instalado en las dependencias del cliente para acceder al servicio entregado por el proveedor.

### Punto de demarcación

Punto físico o lógico que establece el límite de responsabilidad entre el proveedor y el cliente.

También permite definir desde dónde deben realizarse las mediciones contractuales.

### ICMP - Internet Control Message Protocol

Protocolo utilizado para intercambiar mensajes de control y diagnóstico en redes IP.

Herramientas como ping utilizan ICMP para comprobar conectividad y medir RTT.

### TWAMP - Two-Way Active Measurement Protocol

Protocolo de medición activa utilizado para evaluar el rendimiento de una red mediante el intercambio de paquetes de prueba entre equipos de medición.

Está definido en RFC 5357.

### iperf3

Herramienta utilizada para realizar pruebas de rendimiento de red mediante tráfico TCP o UDP.

En la EVA 3 se utiliza para evaluar el throughput TCP del enlace contratado.

### Cobertura de medición

Porcentaje de muestras válidas disponibles respecto de las muestras esperadas durante un período de evaluación.

Cobertura (%) = Muestras válidas / Muestras esperadas x 100

### Ventana de mantenimiento

Período programado para realizar trabajos sobre la infraestructura o el servicio.

Su tratamiento en el cálculo de disponibilidad depende de las condiciones de aviso, duración y exclusión establecidas en el SLA.

### Incidente

Evento que provoca una interrupción o degradación del servicio y requiere atención para recuperar las condiciones normales de funcionamiento.

### Tiempo de respuesta

Tiempo transcurrido entre el registro de un incidente y la primera respuesta del proveedor, según lo establecido en el contrato.

No debe confundirse con el tiempo necesario para resolver la falla.

### Crédito de servicio

Compensación económica establecida en el SLA cuando se comprueba el incumplimiento de un compromiso contractual.

Generalmente se expresa como un porcentaje del cargo mensual del servicio.

### Evidencia insuficiente

Situación en que los datos disponibles no permiten determinar de manera confiable si un indicador cumple o incumple el objetivo establecido.

Puede producirse por falta de muestras, cobertura inferior a la exigida o mediciones realizadas fuera del procedimiento contractual.

### PDCA - Plan, Do, Check, Act

Ciclo de mejora continua basado en planificar, ejecutar, verificar y actuar.

Se utiliza para revisar los resultados del servicio y establecer acciones de mejora.

## 3. Referencias

Pauta Toolkit SLA, INACAP La Serena.

EVA 3, Caso de estudio Agrícola Valle de Elqui.

Material de la asignatura SLA y niveles de servicio en redes.

ITIL 4, ISO/IEC 20000-1, recomendaciones ITU-T y RFC relacionados con medición de rendimiento.
