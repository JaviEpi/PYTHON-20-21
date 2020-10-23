"""
 Ejercicio 04: Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario.
 Autor: Javier Epifanio López
 Fecha: 22/10/2020
 
 Variables:
  - num_1, num_2 
 Algoritmo:
  - PEDIR num_1, num_2
  - Calcular la division <-- num_1 / num_2
  - Si numero_2 = 0, Mostrar en pantalla un aviso
  - Si numero_2 != 0, Mostrar en pantalla a división 
"""

# Pedimos el valor de los números
num_1 = int(input("Valor del primer número: "))
num_2 = int(input("Valor del segundo número: "))

# Mostramos en pantalla el resutado
if num_2 == 0:
    print("Math error")
else:
    print("El resultado de la división es:",num_1 / num_2)