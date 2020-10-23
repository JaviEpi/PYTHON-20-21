"""
 Ejercicio 03: Escribe un programa que lea un número e indique si es par o impar.
 Autor: Javier Epifanio López
 Fecha: 22/10/2020
 
 Variables:
  - num <-- número entero
 Algoritmo:
  - PEDIR num
  - Cálcular si es par --> num // 2 --> si el resto es 0 par, si es 1 es impar
  - Mostrar si es par o impar
"""

# Pedimos un número
num = int(input("Valor de un número: "))

# Cálculos para saber si es par o impar y mostramos el resultado en pantalla
if  num % 2 == 0:
    print(f"El número {num} es par")
else:
    print(f"El número {num} es impar")