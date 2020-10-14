"""
 Ejercicio 7: Realiza un programa que reciba una cantidad de minutos y muestre por 
 pantalla a cuantas horas y minutos corresponde.
 Autor: Javier Epifanio López
 Fecha: 09/10/2020

 Variables:
  - min <-- Número entero

 Algoritmo:
  - PEDIR minutos
  - CONVERTIR min <-- horas y minutos 
  - Mostramos horas y minutos
"""
   


# Pedimos los minutos
min = int(input("Minutos que quieras convertir a horas y minutos: "))

# Cálculos (h=horas)
horas = min // 60
minutos = min % 60

# Mostrar las horas
print(min, "minutos son ", horas, "horas y", minutos, "minutos")