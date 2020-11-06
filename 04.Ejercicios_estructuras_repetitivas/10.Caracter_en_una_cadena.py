"""
 Ejercicio 10: Pide una cadena y un carácter por teclado y muestra cuantas veces aparece el carácter en la cadena.
 Autor: Javier Epifanio López
 Fecha: 1/11/2020
 
 Variables:
   - cadena 
   - caracter 
 Algoritmo:
   - PEDIR cadena, caracter
   - Contador = 0
   - PARA i en el rango de 0 a la longitud de la cadena
        - SI el caracter de la posición i de la cadena en minúscula es igual a el caracter en minúscula y sumo uno al contador
   - Mostramos por pantalla contador y caracter
"""

print("Programa que te dice cuantos caracteres iguales tiene una cadena.")

# Pido la cadena y el caracter
cadena = input("\nIntroduce una cadena: ")
caracter = input("Introduce un caracter: ")

# Creo la variable del contador
contador = 0

# Para i en el rango de 0 a la longitud de la cadena...
for i in range(0, len(cadena)):
    if cadena[i].lower() == caracter.lower(): # Si el caracter de la posición i de la cadena en minúscula es igual a el caracter en minúscula
        contador += 1 # Le sumo uno al contador

# Muestro el resultado por pantalla
print(f"\nLa cadena {cadena} tiene {contador} {caracter}.")
    