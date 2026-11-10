# Normas de referencia para SLA

## 1. Introducción

Para desarrollar el toolkit SLA se consideran las normas indicadas en la pauta de la asignatura. Estas permiten establecer los requisitos del servicio, definir los parámetros de calidad y determinar cómo se deben realizar las mediciones.

No todas las normas cumplen la misma función. Algunas se relacionan con la gestión del servicio y otras con aspectos técnicos como latencia, jitter, pérdida de paquetes y throughput.

A continuación se indica qué establece cada una y en qué parte del método de diseño se utiliza.

## 2. Normas para la gestión del servicio

### ITIL 4 - Service Level Management

Se utiliza para gestionar los acuerdos de nivel de servicio entre el cliente y el proveedor. Considera el levantamiento de requisitos, la definición de compromisos, el monitoreo y la revisión de resultados.

Se aplica en los pasos 2, 5 y 6 del método.

### ISO/IEC 20000-1

Establece requisitos para la gestión de servicios, incluyendo su operación, seguimiento y mejora continua.

En el toolkit se considera para definir procedimientos de control, atención de incidentes y revisión del servicio.

Se aplica en los pasos 5 y 6.

### ITU-T E.860

Entrega una referencia para estructurar los acuerdos de nivel de servicio en telecomunicaciones.

Permite definir el servicio contratado, su alcance, las responsabilidades y las condiciones que deben quedar establecidas entre el cliente y el proveedor.

Se aplica en los pasos 1, 4 y 6.

### ISO/IEC 19086-1

Establece un marco para acuerdos de nivel de servicio asociados a servicios cloud.

Se incluye como referencia para aquellos casos en que el servicio contratado corresponde a infraestructura o aplicaciones en la nube.

Se aplica en los pasos 1 y 4.

## 3. Normas para medir la calidad de la red

### ITU-T Y.1540

Define parámetros de rendimiento para redes IP, entre ellos el retardo, la variación del retardo y la pérdida de paquetes.

Se utiliza para identificar las métricas que deben medirse al evaluar el comportamiento de una red.

Se aplica en los pasos 3 y 5.

### ITU-T Y.1541

Establece objetivos de rendimiento y clases de calidad de servicio para redes IP.

Sirve como referencia para definir objetivos técnicos según las características del servicio.

Se aplica en los pasos 3 y 4.

### MEF 10.4

Define atributos de los servicios Carrier Ethernet, incluyendo parámetros relacionados con su desempeño y disponibilidad.

Se utiliza cuando el SLA corresponde a servicios Ethernet entregados por un operador.

Se aplica en los pasos 1, 3 y 5.

### ITU-T G.114

Entrega recomendaciones sobre el retardo de transmisión en comunicaciones de voz.

La pauta considera como referencia un retardo unidireccional de 150 ms. Este valor no debe confundirse con el RTT, ya que este último corresponde al tiempo de ida y vuelta.

Se aplica en los pasos 3 y 4.

## 4. RFC para las mediciones

### RFC 7679

Define la métrica de retardo unidireccional de paquetes IP.

Se utiliza para medir el tiempo que tarda un paquete en viajar desde el origen hasta el destino.

Se aplica en los pasos 3 y 5.

### RFC 7680

Define la métrica de pérdida unidireccional de paquetes IP.

Permite determinar si los paquetes enviados llegan a su destino bajo las condiciones establecidas para la medición.

Se aplica en los pasos 3 y 5.

### RFC 3393

Define la variación del retardo unidireccional, utilizada como referencia para medir jitter.

Este parámetro es importante para evaluar servicios sensibles a variaciones en los tiempos de entrega de paquetes.

Se aplica en los pasos 3 y 5.

### RFC 5357

Describe el protocolo TWAMP, utilizado para realizar mediciones activas bidireccionales del rendimiento de una red IP.

En la EVA 3 se utiliza como referencia para las mediciones de jitter y pérdida de paquetes desde el punto de demarcación.

Se aplica en los pasos 3 y 5.

### RFC 6349

Establece un marco para evaluar el throughput TCP.

Se utiliza para analizar la capacidad efectiva de transferencia y las condiciones que pueden afectar el rendimiento de una conexión.

En el caso de la EVA 3, el contrato exige pruebas iperf3 TCP realizadas desde el puerto LAN del CPE.

Se aplica en los pasos 3 y 5.

## 5. Aplicación en la EVA 3

Para el caso Agrícola Valle de Elqui se debe evaluar el enlace dedicado de 200 Mbps contratado a NorteNet Telecomunicaciones durante septiembre de 2026.

El contrato establece una disponibilidad mínima de 99,9 %, latencia RTT promedio de hasta 30 ms, jitter promedio de hasta 10 ms y pérdida de paquetes máxima de 0,5 %.

Para throughput se exige un promedio mínimo equivalente al 90 % de la capacidad contratada, es decir, 180 Mbps, considerando al menos cuatro pruebas mensuales realizadas con iperf3 TCP.

También se deben revisar los tiempos de respuesta, el MTTR y las exclusiones establecidas en el contrato.

Las normas permiten definir cómo se evalúan los parámetros técnicos, pero el cumplimiento se determina utilizando las condiciones y los valores establecidos en el SLA.

Un punto importante es que no todas las mediciones disponibles necesariamente sirven para evaluar el contrato. Se debe revisar el origen de los datos, el punto donde se midieron, la herramienta utilizada y la cobertura del período.

En este caso, las mediciones deben cubrir al menos el 90 % del mes para considerarse válidas según la cláusula 5.1.

## 6. Referencias

Pauta Toolkit SLA, INACAP La Serena.

EVA 3, Caso de estudio Agrícola Valle de Elqui.

SLA y niveles de servicio en redes, material de la asignatura.

ITU-T E.860, Y.1540, Y.1541 y G.114.

ISO/IEC 20000-1 e ISO/IEC 19086-1.

MEF 10.4.

RFC 7679, 7680, 3393, 5357 y 6349.
