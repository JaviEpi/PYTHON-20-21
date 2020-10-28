"""
 Ejercicio 07: Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:
   - El exponente sea positivo, sólo tienes que imprimir la potencia.
   - El exponente sea 0, el resultado es 1.
   - El exponente sea negativo, el resultado es 1 / potencia con el exponente positivo.
 Autor: Javier Epifanio López
 Fecha: 22/10/2020

 Variables:
  - base
  - exponente
 Algoritmo:
  - PEDIR base, exponente
  - SI expononente posisitivo --> mostrar la potencia
  - SI exponente es 0 --> mostrar el resultado de la potencia --> 1
  - SI exponente es negativo --> mostrar el resultado 1 / potencia
"""
# Pedimos la base y el exponente
base = float(input("Valor de la base: "))
exponente = float(input("Valor del exponente: "))

# SI expononente posisitivo --> mostrar la potencia
if exponente > 0:
    print("El resultado es: ", base ** exponente)

# SI exponente es 0 --> mostrar el resultado de la potenci --> 1
elif exponente == 0:
    print("El resultado es: 1")

# SI exponente es negativo --> mostrar el resultado 1 / potencia
else:
    print("El resultado es: ",(base ** (1 / exponente)))
