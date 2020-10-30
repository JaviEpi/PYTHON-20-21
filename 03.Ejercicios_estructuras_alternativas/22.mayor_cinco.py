"""
 Ejercicio 21: Realiza un programa que pida cinco números enteros y diga cuál es el mayor.
 Autor: Javier Epifanio López
 Fecha: 22/10/2020
 
 Variables:
  - num_uno, num_dos, num_tres, num_cuatro, num_cinco <-- número entero
  - num_mayor <-- número mas grande
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
num_cuatro = int(input("Valor del cuarto número: "))
num_cinco = int(input("Valor del quinto número: "))
num_mayor = num_uno

# Comprobamos que el número uno es mayor que el segundo
if num_mayor == num_dos and num_mayor == num_tres and num_mayor == num_cuatro and num_mayor == num_cinco:
    print("Todos los números son iguales")
else:
    # Comprobamos que el num_mayor es mayor que el num_dos
    if num_mayor < num_dos:
        num_mayor = num_dos
    # Comprobamos que el num_mayor es mayor que el num_tres
    if num_mayor < num_tres:
        num_mayor = num_tres
    # Comprobamos que el num_mayor es mayor que el num_cuatro
    if num_mayor < num_cuatro:
        num_mayor = num_cuatro
    # Comprobamos que el num_mayor es mayor que el num_cinco
    if num_mayor < num_cinco:
        num_mayor = num_cinco
    # Mostramos el num_mayor
    print(f"El número mayor es {num_mayor}")


