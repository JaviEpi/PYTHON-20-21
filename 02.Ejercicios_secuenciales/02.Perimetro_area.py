"""
 Ejercicio 2: Calcular el perí­metro y área de un rectángulo dada su base y su altura.
 Autor: Javier Epifanio López
 Fecha: 09/10/2020

  Variables:
   - Base
   - Altura

 Algoritmo:
  - PEDIR base, altura
  - Perimetro <-- 2*base + 2*altura
  - Área <-- base * altura
  - Mostramos el área y perímetro

"""

# Pedimos la base y la altura del rectángulo
base = float(input("Base del rectangulo: "))
height = float(input("Altura del rectangulo: "))

# Cálculos
perimeter = 2 * (base + height) 
area = base * height

# Mostramos los cálculos
print("El perímetro del rectangulo es:",perimeter, "y el área del rectangulo es:",area)
