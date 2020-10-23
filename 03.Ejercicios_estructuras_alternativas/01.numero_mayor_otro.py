"""
 Ejercicio 01: Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no.
 Autor: Javier Epifanio López
 Fecha: 22/10/2020
 
 Variables:
  - num_uno, num_dos <-- número real
 Algoritmo:
  - PEDIR nun_uno, num_dos
  - Calcular si el primero es mayor que el segundo
  - Mostrar si el primero es mayor que el segunndo 
"""

# Pedimos dos números
num_uno = float(input("Valor del primer número: "))
num_dos = float(input("Valor del segundo número: "))

# Hacemos los cálculos y mostramos en pantalla si el primer número es mayor que el otro
if num_uno > num_dos:
    print(f"El número uno {num_uno} es mayor que el número dos {num_dos}")
else:
    print(f"El número uno {num_dos} no es mayor que el número dos {num_uno}")
