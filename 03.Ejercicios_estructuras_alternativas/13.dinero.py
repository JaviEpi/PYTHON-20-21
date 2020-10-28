"""
 Ejercicio 13: Escribir un programa que que calcule el desglose mínimo en billetes y monedas de una cantidad exacta de euros. Hay billetes de 500, 200, 100, 50, 20, 10 y 5€ y monedas de 2 y 1€.
 Por ejemplo, si deseamos conocer el desglose de 434€, el programa mostrará por pantalla el siguiente resultado:
   - 2 billetes de 200 euros.
   - 1 billete de 20 euros.
   - 1 billete de 10 euros.
   - 2 monedas de 2 euros.

 Autor: Javier Epifanio López
 Fecha: 22/10/2020

 Variables:
  - dinero
  - billete_500, billete_200, billete_100, billete_50, billete_20, billete_10, billete_5, modena_2 y moneda_1
 Algoritmo:
  - PEDIR dinero
  - Cálculos para saber el desglose de dinero
  - MOSTRAR el desglose
"""

# Pedimos datos
dinero = int(input("Introduce la cantidad de dinero: "))

# Calculamos el desglose del dinero
if dinero >= 500:
    queda = dinero // 500
    print(f"Existen {queda} billetes de 500€")
    dinero = dinero % 500
if dinero >= 200:
    queda = dinero // 200
    print(f"Existen {queda} billetes de 200€")
    dinero = dinero % 200
if dinero >= 100:
    queda = dinero // 100
    print(f"Existen {queda} billetes de 100€")
    dinero = dinero % 100
if dinero >= 50:
    queda = dinero // 50
    print(f"Existen {queda} billetes de 50€")
    dinero = dinero % 50
if dinero >= 20:
    queda = dinero // 20
    print(f"Existen {queda} billetes de 20€")
    dinero = dinero % 20
if dinero >= 10:
    queda = dinero // 10
    print(f"Existen {queda} billetes de 10€")
    dinero = dinero % 10
if dinero >= 5:
    queda = dinero // 5
    print(f"Existen {queda} billetes de 5€")
    dinero = dinero % 5
if dinero >= 2:
    queda = dinero // 2
    print(f"Existen {queda} moneda de 2€")
    dinero = dinero % 2
if dinero >= 1:
    queda = dinero // 1
    print(f"Existen {queda} moneda de 1€")
    dinero = dinero % 1