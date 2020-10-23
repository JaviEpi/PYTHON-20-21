"""
 Ejercicio 01: Crea un programa que lea la edad de dos personas y diga quién es más joven, la primera o la segunda. Ten en cuenta que ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado.
 Autor: Javier Epifanio López
 Fecha: 22/10/2020
 
 Variables:
  - age_1, age_2
 Algoritmo:
  - PEDIR age_1, age_2
  - Calcular si el primero es mayor que el segundo
  - Mostrar si el primero es mayor que el segunndo 
"""

# Pedimos dos números
age_1 = float(input("Edad del la primera persona: "))
age_2 = float(input("Edad del la segunda persona: "))

# Todas las edades deben de ser mayor que 0
if (age_1 or age_2) < 0:
    print("La edad nunca puede ser menor que 0")
# Hacemos los cálculos y mostramos en pantalla si el primer número es mayor que el otro
elif age_1 > age_2:
    print(f"La primera persona { age_1} es mayor que la segunda {age_2}")
elif age_2 > age_1:
    print(f"El segunda persona {age_2} no es mayor que la primera {age_1}")
else:
    print("Las dos personas tienen la misma edad")