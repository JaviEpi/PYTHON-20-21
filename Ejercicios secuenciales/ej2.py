# Ejercicio 1 de secuenciales: Calcular el perí­metro y área de un rectángulo dada su base y su altura.
# Autor: Javier Epifanio López
# Fecha: 05/10/2020

# Pedimos los datos (base y altura)
base = int(input("Base del rectángulo (en cm): "))
altura = int(input("Altura del rectángulo (en cm): "))

# Calculamos el perímetro y el área
perimetro = 2 * (base + altura)
area = base * altura

# Mostramos por pantalla el resultado del perímetro y del área
print("El perímetro del rectángulo:",perimetro, "y el área del rectángulo:",area)