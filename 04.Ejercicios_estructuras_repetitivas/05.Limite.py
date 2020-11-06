'''
 Ejercicio 05: Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite inferior es mayor que el superior lo tiene que volver a pedir. A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes informaciones:
    - La suma de los números que están dentro del intervalo (intervalo abierto).
    - Cuantos números están fuera del intervalo.
    - Informa si hemos introducido algún número igual a los límites del intervalo.

 Autor: Javier Epifanio López
 Fecha: 1/11/2020

 Variables:
   - cont_fuera_intervalo = 0
   - igual_limites = False
   - suma_dentro_intervalo = 0
 Algoritmo:
   - Inicializamos variables cont_fuera_intervalo, igual_limites, suma_dentro_intervalo
   - MIENTRAS sea verdad:
        - Pedimos limite_inferior, limite_superior
        - SI limite_inferior > limite_superior <-- ERROR: El límite inferior debe ser menor que el superior.
        - SI NO limite_inferior > limite_superior <-- break

   - Pedimos num <-- Introduce un número (0, para salir)
   - MIENTRAS num != 0:
        - SI num > limite_inferior y num < limite_superior <-- suma_dentro_intervalo += num (Pertenece al intervalo)
        - SI NO <-- cont_fuera_intervalo += 1 (No pertenece al intervalo)
        - SI num == limite_inferior or num == limite_superior <-- igual a limite
        - Pedimos num <-- Introduce un número (0, para salir)

    - Mostramos la suma_dentro_limite y cant_fuera_intervalo
    - SI igual_limites == True <-- Se ha introducido ningún número igual a los límites del intervalo.
    - SI NO <-- No se ha introducido ningún número igual a los límites del intervalo.
'''

# Variables para el programa
cont_fuera_intervalo = 0
igual_limites = False
suma_dentro_intervalo = 0

# Comprobamos que el limite inferior es menor que el limite superior
while True:
    limite_inferior = int(input("Introduce el límite inferior del intervalo: "))
    limite_superior = int(input("Introduce el límite superior del intervalo: "))
    if limite_inferior > limite_superior:
        print("ERROR: El límite inferior debe ser menor que el superior.")
    if not (limite_inferior > limite_superior): 
        break

# Proceso
num = int(input("Introduce un número (0, para salir): "))
while num!=0:
    # Pertenece al intervalo
    if num > limite_inferior and num < limite_superior:
        suma_dentro_intervalo += num
    else:
    # No pertenece al intervalo
        cont_fuera_intervalo+=1

    # Número igual a alguno de los límites
    if num == limite_inferior or num == limite_superior:
        igual_limites = True
    num = int(input("Introduce un número (0, para salir): "))

# Resultados
print("La suma de los número dentro del intervalo es", suma_dentro_intervalo)
print("La cantidad de números fuera del intervalo es", cont_fuera_intervalo) 

# Comprobamos si hay algún número igual que los limites
if igual_limites == True:
    print("Se ha introducido algún número igual a los límites del intervalo.")
else:
    print("No se ha introducido ningún número igual a los límites del intervalo.")