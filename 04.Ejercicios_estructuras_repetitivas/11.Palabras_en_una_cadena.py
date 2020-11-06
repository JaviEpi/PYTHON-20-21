"""
 Ejercicio 11: Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios), realiza un programa que cuente cuantas palabras tiene.
 Autor: Javier Epifanio López
 Fecha: 1/11/2020
 
 Variables:
   - cadena 
   - palabra
 Algoritmo:
   - Pido la frase
   - Establezo la variable palabras a 1 (para que cuente la última palabra)
   - Para i en el rango 0, longitud de la cadena...
   - Si la posición i de la cadena es un espacio...
        - Le sumo uno a palabras y pongo el contador de letras a 0
   - Muestro palabras. 
"""

print("Programa que cuenta las palabras de una frase")

# Pido la cadena y defino la variable palabras
cadena = input("\nIntroduce una frase: ")
palabras = 1

# Para i en el rango 0, longitud de cadena
for i in range(0, len(cadena)):
    if cadena[i] == " ":
        palabras += 1 # Si la posicion i de cadena es un espacio, sumo uno a palabras

# Muestro por pantalla el resultado
print(f"Esta frase tiene {palabras} palabras.")