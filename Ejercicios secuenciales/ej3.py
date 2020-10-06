# Ejercicio 3 de secuenciales:  Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
# Autor: Javier Epifanio López
# Fecha: 05/10/2020

#importamos la funcion math para hacer la raiz cuadrada
import math
# Pedimos los datos (catetos)
cateto1 = float(input("Introduce el valor del cateto 1 (en cm): "))
cateto2 = float(input("Introduce el valor del cateto 2 (en cm): "))

# Calculamos la hipotenusa
hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

# Mostramos el valor de la hipotenusa
print("El valor de la hipotenusa es:",hipotenusa)





 