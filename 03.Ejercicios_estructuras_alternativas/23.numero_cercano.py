"""
 Ejercicio 23: Diseña un programa que, dados cinco números enteros, determine cuál de los cuatro últimos números es más cercano al primero. Por ejemplo, si el usuario introduce los números 2, 6, 4, 1 y 10, el programa responderá que el número más cercano al 2 es el 1.
 Autor: Javier Epifanio López
 Fecha: 22/10/2020
 
 Variables:
  - num_uno, num_dos, num_tres, num_cuatro <-- número entero
 Algoritmo:
  - PEDIR nun_uno, num_dos, num_tres, num_cuatro

  - Calcular abs(num_uno - num_dos) --> dif_uno_dos
             abs(num_uno - num_tres) --> dif_uno_tres
             abs(num_uno - num_cuatro) --> dif_uno_cuatro

  - SI num_uno == num_dos and num_dos == num_tres and num_tres == num_cuatro 
  - Mostrar Todos los números son iguales
  - SI NO 
        - num_cercano = num_dos
        - SI dif_uno_tres < num_menor <-- num_cercano = num_tres
        - SI dif_uno_cuatro < num_menor <-- num_cercano = num_cuatro
        - Mostrar num_cercano
"""

# Pedimos tres números enteros
num_uno = int(input("Valor del primer número: "))
num_dos = int(input("Valor del segundo número: "))
num_tres = int(input("Valor del tercero número: "))
num_cuatro = int(input("Valor del cuarto número: "))

# Hacemos la diferencia para comprobar cual es el mas cercano
dif_uno_dos = abs(num_uno - num_dos)
dif_uno_tres = abs(num_uno - num_tres)
dif_uno_cuatro = abs(num_uno - num_cuatro)

# Comprobamos que todos los números sean iguales
if num_uno == num_dos and num_dos == num_tres and num_tres == num_cuatro:
    print("Todos los números son iguales")
else:
    # Número 
    num_menor = dif_uno_dos
    num_cercano = num_dos
    # Si la diferencia del num_uno con el num_tres es menor al num_menor, el num_cercano es igual a num_tres
    if dif_uno_tres < num_menor:
        num_menor = dif_uno_tres
        num_cercano = num_tres
    # Si la diferencia del num_uno con el num_cuatro es menor al num_menor, el num_cercano es igual a num_cuatro    
    if dif_uno_cuatro < num_menor:
        num_menor = dif_uno_cuatro
        num_cercano = num_cuatro
    # Mostramos el número más cercano
    print (f"El número mas cercano es: {num_cercano}")
