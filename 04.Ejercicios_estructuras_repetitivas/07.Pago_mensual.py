'''
 Ejercicio 07: Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un programa para determinar cuánto debe pagar mensualmente y el total de lo que pagará después de los 20 meses.
 Autor: Javier Epifanio López
 Fecha: 30/10/2019

 Variables:
   - pago_mensual
   - total_pago
   - mes
 Algoritmo:
   - PARA mes en el rango entre 1 y 21:
        - Mostramos cuanto paga en cada mes
        - total_pago <-- sumamos lo de cada mes
        - Incrementamos el pago_mensual *2
   - Mostramos total_pago 
'''

# Inicializamos
pago_mensual = 10 # Pago del primer mes
total_pago = 0
mes = 0

# PARA mes en el rango entre 1 y 21
for mes in range(1,21):
    print(f"En el mes {mes} paga: {pago_mensual}€")
    total_pago +=  pago_mensual
    pago_mensual *= 2
    
# Mostramos los resultados por pantalla total_pago
print("----------------------------")
print(f"Total pago: {total_pago}€")