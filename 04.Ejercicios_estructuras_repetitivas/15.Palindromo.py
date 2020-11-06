"""
 Ejercicio 14: Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado.
 Autor: Javier Epifanio López
 Fecha: 1/11/2020
 
 Variables:
   - cadena <-- cadena introducida str
   - cadena_inv <-- cadena invertida str
 Algoritmo:
   - MIENTRAS que la cadena no sea un espacio.
        - PIDO cadena.
        - Invertimos cadena.
        - SI cadena en minúsculas es igual que la cadena invertida en minúsculas, es un palíndromo.
        - SI NO, no es un palíndromo. 
"""
print("Programa que comprueba si una cadena es un palíndromo.")

# Defino la variable
cadena = ""

# Mientras que cadena no sea espacio...
while cadena != " ":
    cadena = input("Introduce una cadena (para salir introduzca espacio): ") # Pido la cadena
    cadenainv = cadena[::-1] # Invierto la cadena
    if cadena.lower() == cadenainv.lower(): # Comparo la cadena con la cadena invertida
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")