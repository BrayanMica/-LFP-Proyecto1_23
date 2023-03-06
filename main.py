import os
from tkinter import *
import tkinter.messagebox
from turtle import color
import webbrowser

class Myapp():
	def __init__(self):
		# Creando ventana principal
		ventana = Tk()
		ventana.title("Ventana principal")
		ventana.config(bg="skyblue")

		# Icono de la ventana
		absolutepath = os.path.abspath(__file__)
		Directorio = os.path.dirname(absolutepath)  
		path = Directorio + r'/img/logo.png'
		print(path)
		icon = PhotoImage(file=path)
		ventana.wm_iconphoto(True, icon)

		# Centrar la ventana...
		ancho_ventana = ventana.winfo_reqwidth()
		alto_ventana = ventana.winfo_reqheight()
		ancho_pantalla = ventana.winfo_screenwidth()
		alto_pantalla = ventana.winfo_screenheight()
		posicion_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
		posicion_y = (alto_pantalla // 2) - (alto_ventana // 2)
		ventana.geometry("+{}+{}".format(posicion_x, posicion_y))
		
  		# Creado menu desplegable
		menu = Menu(ventana)
		ventana.config(menu = menu)
		ventana.resizable(True, True)
		
  		# Objetos de la ventana principal
		LabelEditor = Label(ventana,text="Editor")
		LabelEditor.grid(row=1, column=1,sticky="w",padx=10,pady=10)
		CuadroEditor = Text(ventana, width=60, height=20)
		CuadroEditor.grid(row=2, column=1,sticky="w",padx=10,pady=10)

		# Sub menus desplegables
		# submenu de archivo
		Archivo = Menu(menu, tearoff=0)
		Archivo.add_command(label="Abrir", command=self.Abrir)
		Archivo.add_command(label="Guardar", command=self.Guardar)
		Archivo.add_command(label="Guardar como...", command=self.GuardarComo)
		Archivo.add_command(label="Analizar", command=self.Analizar)
		Archivo.add_command(label="Errores", command=self.Errores)
		Archivo.add_separator()
		Archivo.add_command(label="Salir", command=ventana.destroy)
		
  		# submenu de ayuda
		Ayuda = Menu(menu, tearoff=0)
		Ayuda.add_command(label="Manual de usuario", command=self.abrirMusuario)
		Ayuda.add_command(label="Manual Tecnico", command=self.abrirMtecnico)
		Ayuda.add_command(label="Temas de Ayuda", command=self.TemasAyuda)

		menu.add_cascade(label="Archivo", menu=Archivo)
		menu.add_cascade(label="Ayuda", menu=Ayuda)

		ventana.mainloop()
  
  	# Lectura del archivo
	def Abrir(self):
		# LEEMOS EL ARCHIVO DE ENTRADA
		absolutepath = os.path.abspath(__file__)
		Directorio = os.path.dirname(absolutepath) 
		#file = Directorio + r"\{}".format(Filename)  
		file = Directorio + r"/entrada.txt"  
		archivo = open(file, "r")
		if archivo:
			tkinter.messagebox.showinfo(title="Cargando archivo", message=("El archivo se cargo correctamente a memoria"))
			archivo.close()  
		else:
			tkinter.messagebox.showinfo(title="Cargando archivo", message=("El archivo no se cargo a memoria"))  
	
	# Guardar archivo
	def Guardar(self):
		pass
	
	# Guardar el archivo como...
	def GuardarComo(self):
		pass

	# Analizar el archivo de entrada
	def Analizar(self):
		pass
	
	# Errores del ultimo archivo
	def Errores(self):
		pass
	
	# Funciones de ayuda
	# Abriendo un pdf del manual de usuario
	def abrirMusuario(self):
		absolutepath = os.path.abspath(__file__)
		Directorio = os.path.dirname(absolutepath) 
		path = Directorio + r"/Manual de usuario.pdf"  
		if webbrowser.open_new(path) is not None:
			tkinter.messagebox.showinfo(title="Archivo encontrado", message=("El Manual de Usuario fue\nabierto en su navegador"))
		else:
			tkinter.messagebox.showinfo(title="Error al abrir el Manual", message=("El Archivo no fu encontrado"))	

	# Abriendo un pdf del manual tecnico
	def abrirMtecnico(self):
		absolutepath = os.path.abspath(__file__)
		Directorio = os.path.dirname(absolutepath)
		path = Directorio + r"/Manual Tecnico.pdf"  
		if webbrowser.open_new(path) is not None:
			tkinter.messagebox.showinfo(title="Archivo encontrado", message=("El Manual Tecnico fue \nabierto en el navegador"))
		else:
			tkinter.messagebox.showinfo(title="Error al abrir el Manual", message=("El Archivo no fu encontrado"))	
	
 	# Creador de la app
	def TemasAyuda(self):
		tkinter.messagebox.showinfo(title="Temas de Ayuda", message=("Nombre: Brayan Estiben Micá Pérez \n Carne:201907343 \n Lenguages Formales de programacion B-"))

# Llamada de la aplicacion
if __name__ == "__main__":
    Myapp()