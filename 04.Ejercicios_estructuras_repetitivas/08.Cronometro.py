'''
 Ejercicio 08: Hacer un programa que muestre un cronómetro, indicando las horas, minutos y segundos.
 Autor: Javier Epifanio López
 Fecha: 1/11/2020

 Variables: 
   - horas
   - minutos
   - segundos
 Algoritmo:
   - Mostramos en pantalla que se inicia el cronómetro
   - PARA horas en el rango de las horas, minutos y segundos
   - Mostramos en pantalla el resultado de uno en uno
'''

import time
from os import system

# Mostramos que inicia el cronómetro
print("Cronómetro iniciado")
print("-------------------")

# PARA el rango de horas
for horas in range(0,24):
    for minutos in range(0,60): # PARA el rango de minutos
        for segundos in range(0,60): # PARA el rango de segundos
            print(f"{horas:02}:{minutos:02}:{segundos:02}") # Mostramos horas, minutos y segundos
            time.sleep(1)
            system("cls")


'''
# Variables
horas = 0
minutos = 0
segundos = 0

# Inicamos el cronómetro
print("Cronómetro iniciado")
print("-------------------")

# 
while True:
    print(f"{horas:02} : {minutos:02} : {segundos:02}")
    time.sleep(1)

    if segundos < 59:
        segundos += 1
    else:
        segundos = 0
        if minutos < 59:
            minutos = 1
        else:
            minutos = 0
            horas += 1
    print(0 * "\b", end="")       
'''