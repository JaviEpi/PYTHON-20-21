"""
 Ejercicio 13: Pide una cadena y dos caracteres por teclado (valida que sea un carácter), sustituye la aparición del primer carácter en la cadena por el segundo carácter.
 Autor: Javier Epifanio López
 Fecha: 1/11/2020
 
 Variables:
   - resultado <-- cadena convertida a str
   - cadena <-- cadena sin convertir a str
   - posición <-- caracter en la posición i
 Algoritmo:
   - Defino la variable resultado
   - Pido la cadena
   - PARA i en el rango de 0 a la longitud de la cadena...
   - Meto el carácter en una variable.
   - SI esa variable en minúscula es igual que el carácter
       - Añado el caracter en mayúscula al resultado
       - SI esa variable en mayúscula es igual que el caracter
       - Añado el caracter en minúscula al resultado
"""
print("Programa que intercambia mayúsculas por minúsculas y minúsculas por mayúsculas.")

# Defino la variable resultado
resultado = ""

# Pido la cadena
cadena = input("\nIntroduce una cadena: ")

for i in range(0, len(cadena)):
    posicion = cadena[i]
    if posicion.lower() == cadena[i]: # Si el caracter en minúscula es igual al caracter...
        resultado += str(cadena[i].upper()) # Le añado el caracter convertido
    if posicion.upper() == cadena[i]: # Si el caracter en mayúscula es igual al caracter en minúscula...
        resultado += str(cadena[i].lower()) # Le añado el caracter convertido

# Muestro el resultado por pantalla
print(resultado)