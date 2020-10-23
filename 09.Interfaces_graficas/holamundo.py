"""
 Ejercicio 1: Hola Mundo con entorno gráfico Tkinter
 Autor: Javier Epifanio López
 Fecha: 21/10/2020
"""

# Importamos la función Tkinter
import tkinter as tk
ventana = tk.Tk()

label = tk.Label(ventana, text="Hello World!") # Create a text label
label.pack(padx=20, pady=20) # Pack it into the window

ventana.mainloop()