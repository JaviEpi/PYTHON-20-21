"""
 Ejercicio 11: Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).
 Autor: Javier Epifanio López
 Fecha: 10/10/2020
 
 Variables:
   - num1, num2 <-- Número entero 
 Algoritmo:
  - PEDIR num1 y num2
  - distancia <-- (numero_2 - numero_1)
  - MOSTRAR distancia
"""
# Pedimos numero_1 y numero_2
num1 = int(input("Valor número 1: "))
num2 = int(input("Valor número 2: "))

# Cálculos
distancia = abs(num2 - num1)

# Mostramos el resultado de la distancia entre dos puntos
print("La distancia entre estos dos puntos es: ", distancia)
