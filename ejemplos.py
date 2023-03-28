# import os
# import tkinter as tk
# from tkinter import Tk, PhotoImage


# ventana = tk.Tk()

# Configuración de la ventana...
# ventana.title("Mi ventana")
# ventana.geometry("400x300")

# Icono de la ventana
# absolutepath = os.path.abspath(__file__)
# Directorio = os.path.dirname(absolutepath)  
# path = Directorio + r'/netflix_logo_icon_170919.png'
# print(path)
# icon = PhotoImage(file=path)
# ventana.wm_iconphoto(True, icon)

# ventana.mainloop()
# Centrar la ventana...
# ancho_ventana = ventana.winfo_reqwidth()
# alto_ventana = ventana.winfo_reqheight()
# ancho_pantalla = ventana.winfo_screenwidth()
# alto_pantalla = ventana.winfo_screenheight()
# posicion_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
# posicion_y = (alto_pantalla // 2) - (alto_ventana // 2)
# ventana.geometry("+{}+{}".format(posicion_x, posicion_y))

# ventana.mainloop()
# import tkinter as tk

# root = tk.Tk()

# # Creamos el objeto Text
# texto = tk.Text(root, height=10, width=50)
# texto.pack()

# # Insertamos texto en el objeto Text
# texto.insert(tk.END, "Hola, esto es un ejemplo de como insertar texto en un objeto Text.")

# root.mainloop()

import tkinter as tk
from tkinter import filedialog

def guardar_archivo(): 
    archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
    
    if archivo:
        with open(archivo, 'w') as f:
            text = txtEditor.get('1.0', tk.END)
            f.write(text)

root = tk.Tk()

# Crear el botón "Guardar"
btnGuardar = tk.Button(root, text='Guardar', command=guardar_archivo)
btnGuardar.pack(side=tk.LEFT, padx=5)

# Crear el área de edición de texto
txtEditor = tk.Text(root)
txtEditor.pack(expand=True, fill='both')

root.mainloop()
