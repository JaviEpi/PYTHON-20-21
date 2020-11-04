"""
 Ejercicio 03: Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina cuando se introduce un espacio.
 Autor: Javier Epifanio López
 Fecha: 31/10/2020

 Variables:
   - letra <-- Letra introducida por el usuario
 Algoritmo:
   - Pedimos letra
   - MIENTRAS que letra != espacio
        - SI letra == "a" o letra == "e" o letra == "i" o letra == "o" o letra == "u" <-- VOCAL
        - SI NO <-- CONSONANTE
        - Pedimos letra
   
"""

# Pedimos letra al usuario
letra = input("Letra: ")

# MIENTRAS que letra != espacio
while letra != (" "):
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print("Vocal")
    else:
        print ("Consonante")

    letra = input("Letra: ")