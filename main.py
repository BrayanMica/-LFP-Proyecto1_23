import os
from analizador import Analizador
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
from turtle import color
import webbrowser

class Myapp():
	def __init__(self):
		self.texto = ''
		# Creando ventana principal
		ventana = tk.Tk()
		ventana.title("Ventana principal")
		ventana.config(bg="purple")

		# Icono de la ventana
		absolutepath = os.path.abspath(__file__)
		Directorio = os.path.dirname(absolutepath)  
		path = Directorio + r'/img/logo.png'	
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
		self.CuadroEditor = tk.Text(ventana, width=60, height=20)
		self.CuadroEditor.grid(row=2, column=1,sticky="w",padx=10,pady=10)

		# Sub menus desplegables
		# submenu de archivo
		Archivo = Menu(menu, tearoff=0)
		Archivo.add_command(label="Abrir", command=self.Abrir)
		Archivo.add_command(label="Guardar", command=self.Guardar)
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
		file = filedialog.askopenfilename(defaultextension=".json",
		filetypes=[("Archivos de texto", "*.json")])

		if file:
			with open(file, 'r') as archivo:
				# 2. Leer el contenido del archivo
				lineas = archivo.readlines()
				# 3. Cerrar el archivo
				archivo.close()
				self.CuadroEditor.delete(1.0, tk.END)
				for linea in lineas:
					self.CuadroEditor.insert(tk.END,linea)
					self.texto = self.texto + linea
				tkinter.messagebox.showinfo(title="Cargando archivo", message=("El archivo se cargo correctamente a memoria"))
		else:
			tkinter.messagebox.showinfo(title="Cargando archivo", message=("No seleccionaste ningun archivo"))  
			
	
	# Guardar archivo
	def Guardar(self):
		archivo = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Archivos de texto", "*.json")])
		if archivo:
			with open(archivo, 'w') as f:
				text = self.CuadroEditor.get('1.0', tk.END)
				f.write(text)

	# Analizar el archivo de entrada
	def Analizar(self):
		if self.texto:
			self.analizar = Analizador(self.texto)
			self.analizar._compile()
			tkinter.messagebox.showinfo(title="Analizando el Texto", message=("El texto fue analizado correctamente"))	
		else:
			tkinter.messagebox.showinfo(title="Analizando el Texto", message=("No existe texto para analizar"))	
      
      
	# Errores del ultimo archivo
	def Errores(self):
		self.analizar.GuardarErrores()
	
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