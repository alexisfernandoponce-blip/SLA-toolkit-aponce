# Fórmulas para el cálculo y verificación de SLA

## 1. Disponibilidad del servicio

La disponibilidad indica el porcentaje de tiempo durante el cual un servicio permanece operativo dentro del período evaluado.

**Fórmula:**

Disponibilidad (%) = ((T - Ti) / T) x 100

**Variables:**

- T: tiempo total del período, en minutos.
- Ti: tiempo de indisponibilidad atribuible al proveedor, en minutos.

**Referencia:** ITU-T E.860 para la definición del compromiso SLA. El tratamiento de las interrupciones depende del contrato.

**Ejemplo:**

El contrato de Agrícola Valle de Elqui establece una disponibilidad mensual mínima de 99,9 %.

Septiembre de 2026 tiene 30 días:

T = 30 x 24 x 60 = 43.200 minutos

Según los anexos del caso, las interrupciones atribuibles al proveedor son:

- 09 de septiembre: 55 minutos.
- 21 de septiembre: 75 minutos.
- 27 de septiembre: 30 minutos.

La mantención del 3 de septiembre cumple las condiciones de exclusión y la falla del 15 de septiembre corresponde al cliente.

Ti = 55 + 75 + 30 = 160 minutos

Disponibilidad = ((43.200 - 160) / 43.200) x 100

**Disponibilidad = 99,6296 %**

El resultado es inferior al 99,9 % contratado.

## 2. Tiempo máximo de caída permitido

Permite determinar cuánto tiempo puede permanecer indisponible un servicio sin superar el límite de disponibilidad acordado.

**Fórmula:**

Caída permitida = T x (1 - A / 100)

**Variables:**

- T: tiempo total evaluado, en minutos.
- A: disponibilidad mínima contratada, en porcentaje.

**Referencia:** cálculo derivado del indicador de disponibilidad. El objetivo se establece en el SLA.

**Ejemplo:**

T = 43.200 minutos

A = 99,9 %

Caída permitida = 43.200 x (1 - 99,9 / 100)

**Caída permitida = 43,2 minutos**

La indisponibilidad atribuible registrada fue de 160 minutos.

Exceso = 160 - 43,2

**Exceso = 116,8 minutos**

## 3. Disponibilidad de componentes en serie

Cuando varios componentes son necesarios para mantener operativo un servicio, la disponibilidad total depende del funcionamiento de todos ellos.

**Fórmula:**

Aserie = A1 x A2 x A3 x ... x An

**Variables:**

- A1, A2, An: disponibilidad de cada componente, expresada como valor decimal.
- Aserie: disponibilidad conjunta de los componentes.

**Referencia:** modelo de confiabilidad para componentes en serie. Se utiliza como análisis de infraestructura y no como medición directa de disponibilidad contractual.

**Ejemplo:**

El anexo 7 del caso entrega las siguientes disponibilidades anuales:

- CPE: 99,95 % = 0,9995
- Fibra de acceso: 99,80 % = 0,9980
- PE La Serena: 99,99 % = 0,9999
- Backbone: 99,99 % = 0,9999

Aserie = 0,9995 x 0,9980 x 0,9999 x 0,9999

Aserie = 0,9973015098

**Disponibilidad en serie = 99,7302 %**

Bajo el supuesto de fallas independientes, la disponibilidad estimada de esta infraestructura es inferior al objetivo de 99,9 %.

## 4. Disponibilidad de componentes en paralelo

Se utiliza cuando existen dos caminos alternativos y basta con que uno funcione para mantener el servicio.

**Fórmula:**

Aparalelo = 1 - (1 - A1) x (1 - A2)

**Variables:**

- A1: disponibilidad del enlace principal, en valor decimal.
- A2: disponibilidad del enlace de respaldo, en valor decimal.
- Aparalelo: disponibilidad conjunta de ambos caminos.

**Referencia:** modelo de confiabilidad para redundancia en paralelo.

**Ejemplo:**

El proveedor ofrece un radioenlace de respaldo con disponibilidad anual de 99,50 %.

Fibra principal = 0,9980

Radioenlace = 0,9950

Aparalelo = 1 - (1 - 0,9980) x (1 - 0,9950)

Aparalelo = 0,99999

**Disponibilidad de los accesos = 99,9990 %**

Para calcular la disponibilidad completa se incorporan los componentes comunes:

Atotal = 0,9995 x 0,99999 x 0,9999 x 0,9999

**Disponibilidad total estimada = 99,9290 %**

El resultado supera el 99,9 % contratado, siempre que los enlaces sean realmente redundantes, las fallas sean independientes y la conmutación permita mantener el servicio. Este cálculo no reemplaza una prueba de funcionamiento del respaldo.

## 5. Throughput

El throughput corresponde a la tasa efectiva de transferencia de datos durante una medición.

**Fórmula:**

Throughput = Datos transferidos / Tiempo

Para obtener Mbps, si los datos están expresados en bits y el tiempo en segundos:

Throughput (Mbps) = Bits transferidos / (Tiempo x 1.000.000)

Cuando el contrato exige el promedio de varias pruebas:

Throughput promedio = Suma de velocidades medidas / Número de pruebas válidas

**Variables:**

- Datos transferidos: cantidad de información transmitida, en bits.
- Tiempo: duración de la prueba, en segundos.
- Número de pruebas: cantidad de mediciones válidas.
- Throughput: velocidad efectiva, en Mbps.

**Referencia:** RFC 6349, evaluación del rendimiento TCP.

**Ejemplo:**

El anexo 6 registra cuatro pruebas válidas con iperf3 TCP desde el puerto LAN del CPE:

186 Mbps, 182 Mbps, 171 Mbps y 184 Mbps.

Throughput promedio = (186 + 182 + 171 + 184) / 4

**Throughput promedio = 180,75 Mbps**

El contrato exige al menos el 90 % de 200 Mbps:

Throughput mínimo = 200 x 0,90 = 180 Mbps

El promedio obtenido supera el mínimo contratado.

La medición Speedtest de 95 Mbps realizada desde un notebook por Wi-Fi no se incorpora al promedio, porque no corresponde al método contractual.

## 6. Eficiencia del enlace

Permite comparar el throughput medido con la capacidad nominal contratada.

**Fórmula:**

Eficiencia (%) = (Throughput medido / Capacidad contratada) x 100

**Variables:**

- Throughput medido: velocidad efectiva, en Mbps.
- Capacidad contratada: velocidad nominal del servicio, en Mbps.

**Referencia:** relación de cálculo utilizada para comparar resultados de throughput. RFC 6349 se considera como referencia para las pruebas TCP.

**Ejemplo:**

Throughput promedio = 180,75 Mbps

Capacidad contratada = 200 Mbps

Eficiencia = (180,75 / 200) x 100

**Eficiencia = 90,375 %**

El resultado cumple el mínimo contractual de 90 %.

## 7. Pérdida de paquetes

Permite determinar qué porcentaje de los paquetes enviados no llega al destino.

**Fórmula:**

Pérdida (%) = (Paquetes perdidos / Paquetes enviados) x 100

**Variables:**

- Paquetes perdidos: cantidad de paquetes no recibidos.
- Paquetes enviados: total de paquetes transmitidos durante la prueba.

**Referencia:** RFC 7680 e ITU-T Y.1540. El protocolo de medición del caso es TWAMP, definido en RFC 5357.

**Ejemplo:**

Si se envían 10.000 paquetes y se pierden 31:

Pérdida = (31 / 10.000) x 100

**Pérdida = 0,31 %**

El valor coincide con el porcentaje informado para el período del 1 al 18 de septiembre.

Sin embargo, el colector TWAMP dejó de registrar datos el 19 de septiembre. Por lo tanto, ese resultado parcial no permite acreditar el cumplimiento mensual, ya que no alcanza la cobertura mínima del 90 % establecida en el contrato.

## 8. Jitter

El jitter representa la variación del retardo entre paquetes. Cuando se dispone de promedios por período con distintas cantidades de muestras, corresponde calcular un promedio ponderado.

**Fórmula:**

Jitter ponderado = Suma de (Ni x Ji) / Suma de Ni

**Variables:**

- Ni: cantidad de muestras válidas del período.
- Ji: jitter promedio del período, en ms.
- Jitter ponderado: promedio calculado, en ms.

**Referencia:** RFC 3393 para variación del retardo y RFC 5357 para medición mediante TWAMP.

**Ejemplo:**

Según el anexo 4:

- 1 al 7 de septiembre: 9.870 muestras, 9,0 ms.
- 8 al 14 de septiembre: 10.025 muestras, 10,5 ms.
- 15 al 21 de septiembre: 9.900 muestras, 13,8 ms.
- 22 al 30 de septiembre: 12.930 muestras, 7,2 ms.

Jitter = ((9.870 x 9,0) + (10.025 x 10,5) + (9.900 x 13,8) + (12.930 x 7,2)) / (9.870 + 10.025 + 9.900 + 12.930)

Jitter = 423.782,5 / 42.725

**Jitter promedio ponderado = 9,92 ms**

El valor calculado es inferior al máximo contractual de 10 ms.

La validez definitiva de la medición también requiere comprobar la cobertura del período.

## 9. Latencia por distancia

La distancia influye en el retardo de propagación de una señal. En fibra óptica puede estimarse utilizando la velocidad de propagación en el medio.

**Fórmula:**

t = d / v

**Variables:**

- t: retardo de propagación, en segundos.
- d: distancia recorrida, en metros.
- v: velocidad de propagación, en metros por segundo.

Para fibra óptica puede utilizarse como aproximación una velocidad de 200.000.000 m/s.

**Referencia:** cálculo físico de propagación. ITU-T Y.1540 y RFC 7679 se relacionan con la definición y medición del retardo IP, pero no establecen esta fórmula geométrica como método contractual.

**Ejemplo:**

Para un recorrido de fibra de 100 km:

d = 100.000 metros

t = 100.000 / 200.000.000

t = 0,0005 segundos

**Retardo de propagación = 0,5 ms**

Si se considera un recorrido de ida y vuelta por la misma distancia:

RTT de propagación aproximado = 2 x 0,5

**RTT aproximado = 1,0 ms**

Este valor considera solamente propagación. El RTT real también incluye procesamiento, transmisión, colas y otros retardos de la red.

## 10. Créditos de servicio

Los créditos corresponden a descuentos contractuales aplicables cuando se comprueba un incumplimiento del SLA.

**Fórmula:**

Crédito ($) = Cargo mensual x (Porcentaje de crédito / 100)

**Variables:**

- Cargo mensual: valor neto mensual del servicio, en pesos.
- Porcentaje de crédito: porcentaje establecido en el contrato.
- Crédito: monto económico aplicable, en pesos.

**Referencia:** ITU-T E.860 como marco para acuerdos SLA. Los porcentajes y condiciones se obtienen de las cláusulas contractuales.

**Ejemplo:**

Cargo mensual = $1.200.000 neto

Disponibilidad calculada = 99,6296 %

Según la cláusula 8.1, una disponibilidad desde 99,5 % y menor que 99,9 % genera un crédito del 10 %.

Crédito = $1.200.000 x (10 / 100)

**Crédito por disponibilidad = $120.000 netos**

Para otros indicadores, la cláusula 8.2 establece un 5 % por incumplimiento acreditado.

Crédito por un indicador = $1.200.000 x 0,05

**Crédito por indicador = $60.000 netos**

El crédito total se obtiene sumando los porcentajes aplicables, sin superar el tope contractual del 50 %.

Crédito total (%) = mínimo entre la suma de créditos y el tope contractual.

El crédito máximo posible es:

$1.200.000 x 0,50 = $600.000 netos

Este es el límite del contrato, no necesariamente el monto que corresponde aplicar al caso.

## 11. Cobertura de las mediciones

Para emitir un veredicto se debe comprobar que exista suficiente evidencia del período evaluado.

**Fórmula:**

Cobertura (%) = (Muestras válidas / Muestras esperadas) x 100

**Variables:**

- Muestras válidas: registros aceptados para la evaluación.
- Muestras esperadas: registros que deberían existir según la frecuencia de medición.

**Referencia:** cláusula 5.1 del contrato, que establece una cobertura mínima del 90 %.

**Ejemplo:**

Para latencia se registraron:

Muestras esperadas = 43.200

Muestras válidas = 42.725

Cobertura = (42.725 / 43.200) x 100

**Cobertura = 98,90 %**

La medición supera el mínimo exigido y puede utilizarse para evaluar el RTT promedio mensual de 27,4 ms.

## 12. Referencias

Pauta Toolkit SLA, punto 4.5.

EVA 3 - Caso de estudio Agrícola Valle de Elqui SpA, contrato y anexos 1 al 7.

ITU-T E.860, Y.1540 y Y.1541.

RFC 7679, 7680, 3393, 5357 y 6349.

MEF 10.4, para servicios Carrier Ethernet cuando corresponda.
