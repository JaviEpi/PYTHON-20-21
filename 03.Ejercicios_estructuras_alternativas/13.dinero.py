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
  - queda_dinero
 Algoritmo:
  - PEDIR dinero
  - Cálculos para saber el desglose de dinero
  - MOSTRAR el desglose
"""

# Pedimos datos
dinero = int(input("Introduce la cantidad de dinero: "))

# Calculamos el desglose del dinero
if dinero >= 500:
    cantidad_billetes = dinero // 500
    print(f"Existen {cantidad_billetes} billetes de 500€")
    dinero = dinero % 500
if dinero >= 200:
    cantidad_billetes = dinero // 200
    print(f"Existen {cantidad_billetes} billetes de 200€")
    dinero = dinero % 200
if dinero >= 100:
    cantidad_billetes = dinero // 100
    print(f"Existen {cantidad_billetes} billetes de 100€")
    dinero = dinero % 100
if dinero >= 50:
    cantidad_billetes = dinero // 50
    print(f"Existen {cantidad_billetes} billetes de 50€")
    dinero = dinero % 50
if dinero >= 20:
    cantidad_billetes = dinero // 20
    print(f"Existen {cantidad_billetes} billetes de 20€")
    dinero = dinero % 20
if dinero >= 10:
    cantidad_billetes = dinero // 10
    print(f"Existen {cantidad_billetes} billetes de 10€")
    dinero = dinero % 10
if dinero >= 5:
    cantidad_billetes = dinero // 5
    print(f"Existen {cantidad_billetes} billetes de 5€")
    dinero = dinero % 5
if dinero >= 2:
    cantidad_billetes = dinero // 2
    print(f"Existen {cantidad_billetes} moneda de 2€")
    dinero = dinero % 2
if dinero >= 1:
    cantidad_billetes = dinero // 1
    print(f"Existen {cantidad_billetes} moneda de 1€")
    dinero = dinero % 1