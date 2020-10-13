# Ejercicio 2: Calcular el perí­metro y área de un rectángulo dada su base y su altura.
# Autor: Javier Epifanio López
# Fecha: 09/10/2020
#
# Algoritmo:
# PEDIR base
# PEDIR altura
# Perimetro --> 2*base + 2*altura
# Área --> base * altura
# Mostramos el área y perímetro
#
# Variables:
#   *Base
#   *Altura


# Pedimos la base y la altura del rectángulo
base = float(input("Base del rectangulo: "))
altura = float(input("Altura del rectangulo: "))

# Cálculos
perimetro = 2 * (base + altura) 
area = base * altura

# Mostramos los cálculos
print("El perímetro del rectangulo es:",perimetro, "y el área del rectangulo es:",area)
