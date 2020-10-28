"""
 Ejercicio 10: Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios 
 r1,r2 de dos circunferencias y las clasifique en uno de estos estados:
  - exteriores
  - tangentes exteriores
  - secantes
  - tangentes interiores
  - interiores
  - concéntricas

 Autor: Javier Epifanio López
 Fecha: 22/10/2020
 
 Variables:
  - x1, y1 r1 <-- coordenadas de la primera circunferencia
  - x2, y2 r2 <-- coordenadas de la segunda circunferencia
 Algoritmo:
  - PEDIR x1, y1, r1, x2, y2, r2
  - Cálculos
  - MOSTRAR en pantalla dependiendo de la clasificación
"""

# Importamos math
import math

# Pedimos datos de la circuferencia
x1 = float(input("Dime coordenada x primera circunferencia: "))
y1 = float(input("Dime coordenada y primera circunferencia: "))
r1 = float(input("Dime radio primera circunferencia: "))

x2 = float(input("Dime coordenada x segunda circunferencia: "))
y2 = float(input("Dime coordenada y segunda circunferencia: "))
r2 = float(input("Dime radio segunda circunferencia: "))

# Cálculo de la distancia entre las dos circunferencias
distancia = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))

# Circunferencias concétricas
# La distancia = 0.
if distancia == 0:
    print("Circunferencias concéntricas")

# Circunferencias exteriores
# La distancia entre los centros es mayor que la suma de los radios.
elif distancia > (r1+r2):
    print("Circunferencias exteriores")

# Circunferencias tangentes exteriores
# La distancia entre los centros es igual a la suma de los radios.
elif distancia == (r1+r2):
    print("Circunferencias tangentes exteriores")

# circunferencias secantes
# La distancia  es menor que la suma de los radios y mayor que su diferencia.
elif distancia < (r1+r2) and distancia > abs(r1-r2):
    print("Circunferencias secantes")

# Circunferencias tangentes interiores
# La distancia entre los centros es igual a la diferencia entre los radios.
elif distancia == abs(r1-r2):
    print("Circunferencias tangentes interiores")

# Circunferencias interiores
# La distancia entre los centros es mayor que cero y menor que la diferencia entre los radios.
elif distancia > 0 and distancia < abs(r1-r2):
    print("Circunferencias interiores")

