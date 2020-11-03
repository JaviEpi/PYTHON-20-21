"""
 Ejercicio 23: Diseña un programa que, dado un número real que debe representar la calificación numérica de un examen, proporcione la calificación cualitativa correspondiente al número dado. La calificación cualitativa será una de las siguientes: «Suspenso» (nota menor que 5), «Aprobado» (nota mayor o igual que 5, pero menor que 7), «Notable» (nota mayor o igual que 7, pero menor que 9), «Sobresaliente» (nota mayor o igual que 9, pero menor que 10), «Matrícula de Honor» (nota 10).
 Autor: Javier Epifanio López
 Fecha: 22/10/2020
 
 Variables:
  - mark <-- nota del examen (número entero)
 Algoritmo:
  - PEDIR mark
  - SI mark < 0 and mark > 10 <-- Nota fuera de rango
  - SI NO
    - SI mark < 5 <-- Insuficiente
    - SI mark >= 5 <--  Aprobado
    - SI mark >= 7 <--  Notable
    - SI mark == 9 <--  Sobresaliente
    - SI mark == 10 <-- Matricula de Honor
"""

# Pedimos tres números enteros
mark = float(input("Nota del examen: "))

if mark < 0 and mark > 10:
    print("La nota no es correcta, nota entre 0 y 10")
else:
    # SI mark < 5 <-- Insuficiente
    if mark < 5:
        print(f"La nota es de {mark}, Insuficiente")
    # SI NO mark >= 5 <--  Aprobado   
    elif mark >= 5 and mark < 7:
        print(f"La nota es de {mark}, Aprobado")
    # SI NO mark >= 7 <--  Notable
    elif mark >= 7 and mark < 9:
        print(f"La nota es de {mark}, Notable")
    # SI NO mark = 9 <--  Sobresaliente
    elif mark >= 9 and mark < 10:
        print(f"La nota es de {mark}, Sobresaliente")
    # SI NO mark == 10 <-- Matricula de Honor
    elif mark == 10:
        print(f"La nota es de {mark}, Matricula de Honor")