"""
 Ejercicio 21: Realiza un programa que pida tres números enteros y diga cuál es el mayor.
 Autor: Javier Epifanio López
 Fecha: 22/10/2020
 
 Variables:
  - num_uno, num_dos, num_tres <-- número entero
 Algoritmo:
  - PEDIR nun_uno, num_dos, num_tres
  - Calcular num_uno == num_dos and num_uno == num_tres <-- Números iguales
             num_uno > num_dos and num_uno > num_tres <-- num_uno mayor
             num_dos > num_uno and num_dos > num_tres <-- num_dos mayor
             num_tres > num_uno and num_tres > num_dos <-- num_tres mayor
  - Mostrar número mayor 
"""

# Pedimos tres números enteros
num_uno = int(input("Valor del primer número: "))
num_dos = int(input("Valor del segundo número: "))
num_tres = int(input("Valor del tercero número: "))

# Hacemos los cálculos y mostramos en pantalla si el primer número es mayor que el otro
if num_uno == num_dos and num_uno == num_tres:
    print("Los tres números son iguales")
elif num_uno > num_dos and num_uno > num_tres:
    print(f"El número mayor es {num_uno}")
elif num_dos > num_uno and num_dos > num_tres:
    print(f"El número mayor es {num_dos}")
else:
    print(f"El número mayor es {num_tres}")