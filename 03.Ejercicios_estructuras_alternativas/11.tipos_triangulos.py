"""
 Ejercicio 11: Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:
   - Si se cumple Pitágoras entonces es triángulo rectángulo
   - Si sólo dos lados del triángulo son iguales entonces es isósceles.
   - Si los 3 lados son iguales entonces es equilátero.
   - Si no se cumple ninguna de las condiciones anteriores, es escaleno.

 Autor: Javier Epifanio López
 Fecha: 22/10/2020

 Variables:
  - lado_a, lado_b, lado_c
 Algoritmo:
  - PEDIR lado_a, lado_b, lado_c
  - Cálculos para saber que tipo de triángulo es equilátero, rectángulo, isóceles y escaleno
  - MOSTRAR el tipo de triángulo 
"""

# Pedimos datos
lado_a = float(input("Introduce longitud lado A: "))
lado_b = float(input("Introduce longitud lado B: "))
lado_c = float(input("Introduce longitud lado C: "))

# Cálculamos si el triángulo es equilátero y si se cumple mostramos que es equilátero 
if lado_a == lado_b and lado_a == lado_c:
    print("El triángulo es Equilátero")
else:
    # Cálculamos Pitágoras y si se cumple mostramos que es rectángulo 
    if ((lado_a**2 + lado_b**2) == lado_c**2) or ((lado_a**2 + lado_c**2) == lado_b**2) or ((lado_b**2 + lado_c)**2 == lado_a**2):
        print("El triángulo es Rectángulo")

    # Cálculamos si el triángulo es isósceles y si se cumple mostramos que es isóceles
    if lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        print("El triángulo es Isóceles")

    # Cálculamos si el triángulo es escaleno y si se cumple mostramos que es escaleno
    else:
        print("El triángulo es Escaleno")