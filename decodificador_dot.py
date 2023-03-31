import os

import graphviz

                
# Creacion de archivo operacion.dot
absolutepath = os.path.abspath(__file__)
Directorio = os.path.dirname(absolutepath) 
file = Directorio + "/"+"operacion.dot"
crear = open(file,"w")
cadena =""

ListaGrafo=[]

ListaGrafo.append('"Multiplicacion = 54.0" -> "6"')
ListaGrafo.append('"Multiplicacion = 54.0" -> "9"')
for k,operacion in enumerate(ListaGrafo):     
    cadena = cadena+ operacion +'''\n'''


crear.write('''digraph R {\n rankdir=LR \n'''+cadena+'''}''')                
crear.close()

#Cargar archivo .dot
absolutepath = os.path.abspath(__file__)
Directorio = os.path.dirname(absolutepath) 
ruta_actual = Directorio + "/"+"operacion.dot"
with open(ruta_actual) as f:
    dot_graph = f.read()

# Generando imagen del grafico en formato PNG y guardarlo la misma ruta de hubicacion
graph = graphviz.Source(dot_graph)
graph.format = "svg"
graph.render(filename="operacion")