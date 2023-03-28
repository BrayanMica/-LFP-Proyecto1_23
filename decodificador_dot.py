import os

import graphviz


print("---------- Mostrar imagen -----------")
                
# Creacion de archivo peliculas.dot
absolutepath = os.path.abspath(__file__)
Directorio = os.path.dirname(absolutepath) 
file = Directorio + "/"+"peliculas.dot"
crear = open(file,"w")
cadena =""

for i,peliculas in enumerate(nueva): 
    cadena = cadena + "p" + str(i) + '''[fillcolor=chartreuse, style=filled, shape="record", label="{ ''' + str(peliculas.nombre) +'''|'''+ str(peliculas.anio) + '''|''' + str(peliculas.genero) + '''}"];\n'''

listaaux=[]
for i,peliculas in enumerate(nueva): 
    
    for j,peli in enumerate(peliculas.autores):
        if peli not in listaaux:
            listaaux.append(peli) 


for k,peli in enumerate(listaaux):     
    cadena = cadena + "a" + str(k) + '''[color="#000000", fillcolor=pink, style="filled", shape=box, label=" ''' + str(peli)+''' "];\n'''


for i,peliculas in enumerate(nueva):
    for j in peliculas.autores:  
        for k,peli in enumerate(listaaux):
            if peli == j:
                cadena = cadena + "\na" + str(k) + "-> p" + str(i) 


crear.write('''digraph R {\n rankdir=LR \n'''+cadena+'''}''')                
crear.close()

#Cargar archivo .dot
absolutepath = os.path.abspath(__file__)
Directorio = os.path.dirname(absolutepath) 
ruta_actual = Directorio + "/"+"peliculas.dot"
with open(ruta_actual) as f:
    dot_graph = f.read()

# Generando imagen del grafico en formato PNG y guardarlo la misma ruta de hubicacion
graph = graphviz.Source(dot_graph)
graph.format = "svg"
graph.render(filename="peliculas")
print("Archivo fue creado exitosamente")
input("Presiona la tecla enter para continuar")