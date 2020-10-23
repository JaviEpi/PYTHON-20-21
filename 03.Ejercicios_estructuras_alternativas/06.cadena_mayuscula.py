"""
 Ejercicio 06: Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
 Autor: Javier Epifanio López
 Fecha: 22/10/2020
 
 Variables:
  - letter --> cadena(letra)
 Algoritmo:
  - PEDIR la cadena
  - SI la letter <-- letter >= A y cad <= Z --> mostrar la cadena es mayuscula
  - SI NO mostrar la cadena no es mayuscula
"""

# Pedimos la cadena
letter = input("Introduce una letra: ")

# if la cadena es una letra mayuscula muestralo y si no muestra que no es mayuscula
if len(letter)==1 and letter>="A" and letter<="Z":
    print("La cadena es una letra mayúscula")
else:
    print("La cadena no es una letra mayúscula")