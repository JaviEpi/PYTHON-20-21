'''
 Ejercicio 06: Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.
 Autor: Javier Epifanio López
 Fecha: 1/11/2020

 Variables:
   - base
   - exponente
   - potencia = 1
 Algoritmo:
   - Pedimos base, exponente
   - SI exponente >= 0:
      - PARA i en rango entre 1 y exponente + 1:
          - potencia = potencia * base

   - Mostramos la potencia 
'''

potencia = 1

# Pedimos base, exponente
base = float(input("Base: "))
exponente = int(input("Exponente: "))


# SI exponente >= 0
if exponente >= 0:
  for _ in range (exponente): # PARA _ en rango entre 1 y exponente + 1
    potencia *= base

  print("Potencia = ", potencia) # Mostramos la potencia

else:
  print("El exponente tiene que ser positivo") # El exponente tiene que ser positivo
