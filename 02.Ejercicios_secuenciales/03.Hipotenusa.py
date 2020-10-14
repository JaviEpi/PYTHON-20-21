 """
 Ejercicio 3: Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
 Autor: Javier Epifanio López
 Fecha: 09/10/2020

 Variables:
   - Cateto1, cateto2
 Algoritmo:
  - PEDIR cateto1, cateto2
  - Hipotenusa <-- raiz cuadrada de cateto1**2 + cateto2**2

"""
# Importamos la función math
import math

# Pedimos los valores de los catetos
side1 = float(input("Valor del cateto 1: "))
side2 = float(input("Valor del cateto 2: "))

# Cálculos --> hipotenusa**2 = ((c1**2)+(c2**2))
hypotenuse = math.sqrt((side1**2)+(side2**2))

# Mostramos resultado
print("La hipotenusa es:", hypotenuse)