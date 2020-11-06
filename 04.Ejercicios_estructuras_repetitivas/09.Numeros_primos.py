'''
 Ejercicio 09: Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de números primos que queremos mostrar.
 Autor: Javier Epifanio López
 Fecha: 1/11/2020
 
 Variables:
   - num_primos <-- Cantidad de números primos que se muestran
   - contador <-- Contador
 Algoritmo:
   - PEDIR num_primos
   - CREAR contador
   - PARA i en rango entre 2 y 999999
        - factorial <-- math.factorial((i-1))
        - SI contador < num_primo
              - SI (factorial + 1) % i == 0 <-- MOSTRAR i (número primo) y contador + 1
        - SI NO termina      
'''


import math

print("Programa que muestra los n primeros números primos.")

# Pido el número de primos a mostrar
num_primo = int(input("\nIntroduce cuantos números quieres mostrar: "))

# Creo la variable que hará de contador
contador = 0

for i in range(2, 999999):
  factorial = math.factorial((i-1)) # Calculo el factorial de i menos 1
  if contador < num_primo: # Si no he superado el límite para contador...
    if (factorial + 1) % i == 0: # Le sumo uno al resultado del factorial y compruebo si el resto es 0
      print(i) # Muestro el número primo
      contador += 1 # Le sumo uno al contador
  else:
    break