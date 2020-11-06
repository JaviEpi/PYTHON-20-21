"""
 Ejercicio 14: Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado.
 Autor: Javier Epifanio López
 Fecha: 1/11/2020
 
 Variables:
   - cadena <-- cadena introducida str
   - subcadena <-- cadena a buscar str
 Algoritmo:
   - Pido la cadena
   - Pido la subcadena
   - Pongo un contador para saber cuando se ha encontrado una subcadena
   - PARA i en el rango de 0 y final de la cadena
        - Si un rango de caracteres es igual que la subcadena, la ha encontrado e incremento el contador
        - Si no, miro si el contador está a 0 y si lo está digo que no la ha encontrado
"""

print("Programa que comprueba si una cadena contiene una subcadena.")

# Pido las cadenas y le pongo 0 a la variable del contador
cadena = input("\nIntroduce una cadena: ")
subcadena = input("Introduce la subcadena: ")
c = 0

for i in range(0, len(cadena)):
    if cadena[i:(len(subcadena) + i)].lower() == subcadena: # Si el rango i a la longitud de subcadena equivale a subcadena
        print(f"Si, {cadena} incluye {subcadena}.")
        c = 1
    elif c == 0 and len(cadena) == (i + 1): # Si el contador es 0 y la longitud de la cadena es igual a i, (es decir, es la última vuelta del bucle) 
        print(f"No, {cadena} no incluye {subcadena}.") # muestro que no se ha encontrado la subcadena en la cadena.