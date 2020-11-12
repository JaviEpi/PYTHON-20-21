'''
 Ejercicio 04 :Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.
 Autor: Javier Epifanio López
 Fecha: 31/10/2020
 
 Variables:
   - num_1, num_2 <-- Dos números introducidos por el usuario

 Algoritmo: 
   - PEDIR num_1, num_2
   - SI num_1 % 2 == 1 <-- num_1 += 1
   - PARA num en rango num_1, num_2 + 1 de 2 en 2<-- Mostramos número par
'''

# Pedimos datos
num_1 = int(input("Introduce el número 1: "))
num_2 = int(input("Introduce el número 2: "))

# Si primer número es impar pasamos al siguiente par
if num_1 < num_2:
  num_1, num_2 == num_2,num_1
if num_1 % 2 == 1:
  num_1 += 1



# Mostramos salida
for num in range(num_1, num_2 + 1, 2):
    print(f"{num} ",end="")