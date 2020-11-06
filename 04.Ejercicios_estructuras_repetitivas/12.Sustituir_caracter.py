"""
 Ejercicio 12: Pide una cadena y dos caracteres por teclado (valida que sea un carácter), sustituye la aparición del primer carácter en la cadena por el segundo carácter.
 Autor: Javier Epifanio López
 Fecha: 1/11/2020
 
 Variables:
   - cadena 
   - caracter_1, caracter_2
 Algoritmo:
   - Pido la cadena y los caracteres
   - Creo una variable para ir metiendo todos los caracteres
   - SI la longitud de lo introducido es un 1
   - SI lo es, PARA en un rango de 0 a cadena
        - SI el caracter de la posición es igual que el primero introducido. Si lo es, añado el segundo caracter
        - SI el caracter de la posición no es igual que el primero introducido. Si es cierto, añado el mismo caracter.
   - SI NO lo es, digo que no se han introducido bien los caracteres
   - Muestro el contenido de repl
"""


print("Programa que a partir de una cadena reemplaza un caracter indicado por otro.")

# Pido la cadena y los caracteres
cadena = input("\nIntroduce una cadena: ")
caracter_1 = input("Introduce el caracter que quieres remplazar: ")
caracter_2 = input("Introduce el nuevo caracter: ")

# Creo la variable
repl = ""

if len(caracter_1) == 1 and len(caracter_2) == 1: # Compruebo si es un caracter
    for i in range(0, len(cadena)):
        if cadena[i].lower() == caracter_1.lower(): # Si coincide con el primer introducido
            repl += caracter_2 # Añado el segundo introducido
        if cadena[i].lower() != caracter_1.lower(): # Si no coincide con el primer introducido
            repl += cadena[i] # Añado el mismo
else:
    print("\nNo has introducido bien los caracteres.")

print(f"\n{repl}")