# Programa para calcular la longitud y el área de una circunferencia dado el radio.
# Autor: @JavierEpifanio.
# Fecha: 23/09/2020

# Importamos la función math para coger el número pi.
import math

# Pedimos el radio
radio = float(input("Dame el radio: "))

# Calculamos la longitud y el área.
longitud = 2 * math.pi * radio
area = math.pi * radio ** 2

# Mostramos por pantalla los resultados.
print("La longitud de la circunferencia es", round(longitud, 2), "y el area de la circunferencia es", round(area,2))