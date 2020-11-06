'''
 Ejercicio 06: Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.
 Autor: Javier Epifanio López
 Fecha: 1/10/2020

 Variables:
   - base
   - exponente
   - potencia = 1
 Algoritmo:
   - Pedimos base, exponente
   - PARA i en rango entre 1 y exponente + 1:
        - potencia = potencia * base

   - Mostramos la potencia 
'''
# Pedimos base, exponente
base = float(input("Base: "))
exponente = int(input("Exponente: "))
potencia = 1

# PARA i en rango entre 1 y exponente + 1
for cont in range (1, exponente + 1):
    potencia = potencia * base

# Mostramos la potencia
print("Potencia = ", potencia)