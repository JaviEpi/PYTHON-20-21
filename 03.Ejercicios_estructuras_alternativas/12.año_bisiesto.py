"""
 Ejercicio 12: Escribir un programa que lea un año indicar si es bisiesto. 
 Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.
 Autor: Javier Epifanio López
 Fecha: 22/10/2020
 
 Variables:
  - year <-- año (número entero)
 Algoritmo:
  - PEDIR un año   
  - Calcular si el año es bisiesto o no
  - Mostrar si es bisiesto o no
"""
# Pedimos el año
year = int(input("Introduce el año: "))

# Es bisiesto o no es bisiesto
if year > 0:
    if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
            print("El año ", year, " es bisiesto")
    else:
        print("El año ", year, " no es bisiesto")
else:
    print("El año ",year, " no es un año válido")