"""
 Ejercicio 18: Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
 Autor: Javier Epifanio López
 Fecha: 10/10/2020
 
 Variables:
  - nombre
  - primer_apellido
  - segundo_apellido
  - iniciales
 Algoritmo:
  - PEDIR nombre y apellidos
  - iniciales <-- nombre[0] + primer_apellido[0] + segundo_apellido[0]
  - Mostrar iniciales
"""

# Pedimos el nombre y los apellidos
nombre = input("Nombre: ")
primer_apellido = input("Primer apellido: ")
segundo_apellido = input("Segundo apellido: ")

# Cálculos
iniciales = (nombre[0] + primer_apellido[0] + segundo_apellido[0])

# Mostramos las iniciales
print("Las iniciales son: ", iniciales)