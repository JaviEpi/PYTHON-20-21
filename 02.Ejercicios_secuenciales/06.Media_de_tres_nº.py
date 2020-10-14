"""
 Ejercicio 6: Programa que hace la media a tres números
 Autor: Javier Epifanio López
 Fecha: 09/10/2020
 
 Variables:
   num1, num2, num3 <-- número real

 Algoritmo:
  - PEDIR num1, num2, num3
  - media <-- (num1 + num2 + num3)/ 3
  - Mostrar media
"""


# Pedir los tres números 
num1 = float(input("Introduce el valor del número 1: "))
num2 = float(input("Introduce el valor del número 2: "))
num3 = float(input("Introduce el valor del número 3: "))

# Cálculos
media = (num1 + num2 + num3)/ 3

# Mostramos en pantalla la media de los tres números
print(f"La media de los tres números es: {media:.3}")