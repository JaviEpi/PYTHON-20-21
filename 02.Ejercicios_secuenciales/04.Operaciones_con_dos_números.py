"""
  Ejercicio 4: Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
 Autor: Javier Epifanio López
 Fecha: 09/10/2020
 
 Variables:
  - num1, num2
   
 Algoritmo:
  - PEDIR un num1, num2
  - SUMAR <-- num1 + num2
  - RESTAR <-- num1 - num2
  - MULTIPLICAR <-- num1 * num2
  - Dividir <-- num1 / num2

"""

# Pedimos los números
num1 = float(input("Valor de número 1: "))
num2 = float(input("Valor de número 2: "))

# Mostramos los resultados (suma, resta, multiplicación y división)
print(f"Resultado suma: {num1 + num2}")
print(f"Resultado resta: {num1 - num2}")
print(f"Resultado multiplicación: {num1 * num2}")
print(f"Resultado división: {num1 / num2}")