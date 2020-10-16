"""
 Ejercicio 14: Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.
 Autor: Javier Epifanio López
 Fecha: 10/10/2020
 
 Variables:
   - número <-- Número entero
   - cifra1, cifra2 
   - numero_inverso
 Algoritmo:
  - PEDIR un numero de dos cifras
  - Cálcuos <-- numero_inverso cifra1 = int((numero % 100) / 10) cifra2 = numero % 10 
                numero_inverso = (str(cifra2) + str(cifra1))
  - Mostrar numero_inverso
"""

# Pedimos un número
numero = int(input("Introduzca un numero de dos digitos: "))

# Cálculo el número inverso
cifra1 = int((numero % 100) / 10)
cifra2 = numero % 10 
numero_inverso = (str(cifra2) + str(cifra1))

# Mostramos el resultado del invertido
print("El numero inverso es: ", numero_inverso)