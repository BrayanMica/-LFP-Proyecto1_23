import os
import tkinter
import graphviz

from numpy import double

#from graficador import *

ListaGrafo = []
class Analizador:
    def __init__(self, entrada:str):
        self.lineas = entrada #ENTRADA
        self.index = 0 #POSICION DE CARACTERES EN LA ENTRADA
        self.fila = 0 #FILA ACTUAL
        self.columna = 0 #COLUMNA ACTUAL
        self.ListaErrores = [] # LISTA PARA GUARDAR ERRORES
        
    def _token(self, token:str, estado_actual:str, estado_sig:str):
        if self.lineas[self.index] != " ":
            text = self._juntar(self.index, len(token))
            if self._analizar(token, text):
                self.index += len(token) - 1
                self.columna += len(token) - 1
                return estado_sig
            else:
                return 'ERROR'
        else:
            return estado_actual
        
    def _juntar(self,_index:int, _count:int):
        try:
            tmp = ''
            for i in range(_index, _index + _count):
                tmp += self.lineas[i]
            return tmp
        except:
            return None
        
    def _analizar(self, token, texto):
        try:
            count = 0
            tokem_tmp = ""
            for i in texto:
                #CUANDO LA LETRA HAGA MATCH CON EL TOKEN ENTRA
                #print('COMBINACION -> ',i , '==', token[count])
                if str(i) == str(token[count]):
                    tokem_tmp += i  
                    count += 1 
                else:
                    #print('ERROR1')
                    return False
                
            #print(f'********** ENCONTRE - {tokem_tmp} ***************')
            return True
        except:
            #print('ERROR2')
            return False
        
    def _digito(self, estado_sig):
        estado_actual = 'D0'
        numero = ""
        while self.lineas[self.index] != "":
            #print(f'CARACTER - {self.lineas[self.index] } | ESTADO - {estado_actual} | FILA - {self.fila}  | COLUMNA - {self.columna}')

            # IDENTIFICAR SALTO DE LINEA
            if self.lineas[self.index] == '\n':
                self.fila += 1
                self.columna =0
            
            # PARA SALIRSE
            elif str(self.lineas[self.index])== '"':
                self.index -= 1
                return [estado_sig, numero]
            elif str(self.lineas[self.index])== ']':
                self.index -= 1
                return [estado_sig, numero]
            elif str(self.lineas[self.index])== '}':
                self.index -= 1
                return [estado_sig, numero]

            # VERIFICAR SI ES DECIMAL
            elif self.lineas[self.index] == '.':
                token = "."
                if estado_actual == 'D2' or estado_actual == 'D0':
                    estado_actual = 'ERROR'
                elif self.lineas[self.index] != ' ':
                    text = self._juntar(self.index, len(token))
                    if self._analizar(token, text):
                        numero += text
                        estado_actual = 'D2'
                        self.index += len(token) - 1
                        self.columna += len(token) - 1
                    else:
                        estado_actual = 'ERROR'
                        
            # ************************
            #         ESTADOS
            # ************************

            # D0 -> [0-9] D0 
            elif estado_actual == 'D0' or estado_actual == 'D1':
                if self.lineas[self.index] != ' ':
                    estado_actual = 'ERROR'
                    for i in ['0','1','2','3','4','5','6','7','8','9']:
                        token = i
                        text = self._juntar(self.index, len(token))
                        if self._analizar(token, text):
                            numero += text
                            estado_actual = 'D1'
                            break

            # D2 -> [0-9] D2
            elif estado_actual == 'D2':
                if self.lineas[self.index] != ' ':
                    estado_actual = 'ERROR'
                    for i in ['0','1','2','3','4','5','6','7','8','9']:
                        text = self._juntar(self.index, len(i))
                        if self._analizar(i, text):
                            numero += text
                            estado_actual = 'D2'
                            break

            # ERRORES 
            if estado_actual == 'ERROR':
                return ['ERROR', -1]
            
            #INCREMENTAR POSICION
            if self.index < len(self.lineas) - 1:
                self.index +=1
            else:
                break

    def _operaciones(self, estado_sig):
        
        
        estado_actual = 'S1'
        hijo_derecho = ""
        hijo_izquierdo = ""
        operador = ""
        while self.lineas[self.index] != "":
            #print(f'CARACTER OP - {self.lineas[self.index] } | ESTADO - {estado_actual} | FILA - {self.fila}  | COLUMNA - {self.columna}')
            
            # IDENTIFICAR SALTO DE LINEA
            if self.lineas[self.index] == '\n':
                self.fila += 1
                self.columna =0

            # ************************
            #         ESTADOS
            # ************************

            # S1 -> "Operacion" S2
            elif estado_actual == 'S1':
                estado_actual = self._token('"Operacion"', 'S1', 'S2')
                
            # S2 -> : S3
            elif estado_actual == 'S2':
                estado_actual = self._token(':', 'S2', 'S3')

            # S3 -> OPERADOR S4
            elif estado_actual == 'S3':
                operadores = ['"Suma"','"Resta"','"Multiplicacion"','"Division"', '"Potencia"','"Raiz"','"Inverso"', '"Seno"','"Coseno"','"Tangente"','"Mod"']
                for i in operadores:
                    estado_actual = self._token(i, 'S3', 'S4')
                    if estado_actual != 'ERROR':
                        operador = i
                        break

            # S4 -> "Valor1" S5
            elif estado_actual == 'S4':
                estado_actual = self._token('"Valor1"', 'S4', 'S5')

            # S5 -> : S6
            elif estado_actual == 'S5':
                estado_actual = self._token(':', 'S5', 'S6')

            # S6 -> DIGITO S9 
            #    | [ S7
            elif estado_actual == 'S6':
                estado_actual = self._token('[','S6','S7')
                if estado_actual == 'ERROR':
                    estado_actual = 'S9'
                    a = self._digito('S9')
                    if "ERROR" == a[0]:
                        estado_actual = 'ERROR'
                    elif a[0] == 'S9':
                        hijo_izquierdo = a[1]

            # S7 -> S1 S8
            elif estado_actual == 'S7':
                a = self._operaciones('S8')
                estado_actual = a[0]
                hijo_izquierdo = a[1]

            # S8 -> ] S9
            elif estado_actual == 'S8':
                estado_actual = self._token(']','S8','S9')
                
            # S9 -> "Valor2" S10
            elif estado_actual == 'S9':
                if operador == '"Inverso"' or operador == '"Seno"' or operador =='"Coseno"' or operador=='"Tangente"':
                    self.index -= 1
                    # REALIZAR LA OPERACION ARITMETICA Y DEVOLVER UN SOLO VALOR
                    print("\t*****OPERACION ARITMETICA*****")
                    print('\t',operador ,'(',hijo_izquierdo ,')' )
                    print('\t*******************************\n')
                    op = operador +'('+hijo_izquierdo +')'
                    
                    return ['S8', op]  
                else:
                    estado_actual = self._token('"Valor2"', 'S9', 'S10')

            # S10 -> : S11
            elif estado_actual == 'S10':
                estado_actual = self._token(':', 'S10', 'S11')

            # S11 -> DIGITO S14 
            #    | [ S12
            elif estado_actual == 'S11':
                estado_actual = self._token('[','S11','S12')
                if estado_actual == 'ERROR':
                    estado_actual = 'S14'
                    a = self._digito('S14')
                    if "ERROR" == a[0]:
                        estado_actual = 'ERROR'
                    elif 'S14' == a[0]:
                        hijo_derecho = a[1]
                        # REALIZAR LA OPERACION ARITMETICA Y DEVOLVER UN SOLO VALOR
                        print("\t*****OPERACION ARITMETICA*****")
                        print('\t',hijo_izquierdo , operador, hijo_derecho)
                        print('\t*******************************\n')
                        op = hijo_izquierdo + operador + hijo_derecho
                        # GRAFICA DE OPERACION
                        class Nodo:
                            def __init__(self,_node):
                                self.node = _node
                                self.left = None
                                self.right = None
                        # Cuando nosotros realizamos una operacion con
                        # valor 1 # valor 2
                        # Decimos que valor 1 es nuestro nodo hijo izquierdo
                        # Decimos que valor 2 es nuestro nodo hijo derecho
                        #     5 + 8 
                        # Definimos un nodo raiz
                        class datos:
                            def __init__(self):
                                self.operaciones = ''
                                self.hijo_i = 0
                                self.hijo_d = 0
                                
                            # Getter para Operador
                            @property
                            def  operador(self):
                                return self.operaciones
                            
                            # Setter para operador
                            @operador.setter
                            def operador(self,valor):
                                self.operaciones = valor

                            # Getter para hijo izquierdo
                            @property
                            def  h_izq(self):
                                return self.hijo_i
                            
                            # Setter para hijo izquierdo
                            @h_izq.setter
                            def h_izq(self,valor):
                                self.hijo_i = valor
                                
                            # Getter para hijo derecho
                            @property
                            def  h_der(self):
                                return self.hijo_d
                            
                            # Setter para hijo derecho
                            @h_der.setter
                            def h_der(self,valor):
                                self.hijo_d = valor
                                
                        dato = datos()
                        self.raiz = Nodo(None)
                        dato.operador=operador
                        
                        resultado=0
                        if(str(operador)=='"Suma"'):
                            resultado = double(hijo_izquierdo) + double(hijo_derecho)
                            print(str(resultado))
                        elif (str(operador)=='"Resta"'):
                            resultado = double(hijo_izquierdo) - double(hijo_derecho)
                            print(str(resultado))
                        elif (str(operador)=='"Multiplicacion"'):
                            resultado = double(hijo_izquierdo) * double(hijo_derecho)
                            print(str(resultado))
                        elif (str(operador)=='"Division"'):
                            resultado = double(hijo_izquierdo) / double(hijo_derecho)
                            print(str(resultado))
    
                        self.raiz.node = str(operador) + ' = '+ str(double(resultado))
                        self.raiz.left = Nodo(hijo_izquierdo)
                        self.raiz.right = Nodo(hijo_derecho)
                        operador=operador.strip('"') + ' = ' + str(resultado)
                        def imprimir(_nodo: Nodo):
                            if(_nodo.left != None):
                                #print("RECURSIVIDAD IZQ")
                                imprimir(_nodo.left)
                                print(f' "{operador}" -> "{_nodo.left.node}"')
                                ListaGrafo.append(f' "{operador}" -> "{_nodo.left.node}"')
                            if(_nodo.right != None):
                                #print("RECURSIVIDAD DER")
                                imprimir(_nodo.right)
                                print(f' "{operador}" -> "{_nodo.right.node}"')
                                ListaGrafo.append(f' "{operador}" -> "{_nodo.right.node}"') 
                        imprimir(self.raiz)
                        # Creacion de archivo operacion.dot
                        absolutepath = os.path.abspath(__file__)
                        Directorio = os.path.dirname(absolutepath) 
                        file = Directorio + "/"+"operacion.dot"
                        crear = open(file,"w")
                        cadena =""
                        
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
                        return [estado_sig, op]  
                    
        

            # S12 -> S1 S13
            elif estado_actual == 'S12':
                estado_actual = 'S13'
                a = self._operaciones('S13')
                hijo_derecho = a[1]
                if "ERROR" == a[0]:
                    estado_actual = 'ERROR'

            # S13 -> ] S14
            elif estado_actual == 'S13':
                estado_actual = self._token(']','S13','S14')

                #REALIZAR LA OPERACION ARITMETICA Y DEVOLVER UN SOLO VALOR
                print("\t*****OPERACION ARITMETICA*****")
                print('\t',hijo_izquierdo , operador, hijo_derecho)
                print('\t*******************************\n')
                op = hijo_izquierdo + operador + hijo_derecho
                # GRAFICA DE OPERACION
                
                return [estado_sig, op] 

            # ERRORES 
            if estado_actual == 'ERROR':
                # print("********************************")
                # print("\tERROR")
                # print("********************************")
                # # ERROR
                # print(self.lineas[self.index], "fila ",self.fila, "Columna ",self.columna)
                self.guardarErrores(self.lineas[self.index], self.fila, self.columna)
                return ['ERROR', -1]
            
            #INCREMENTAR POSICION
            if self.index < len(self.lineas) - 1:
                self.index += 1
            else:
                break
        
    def _compile(self):
        self.fila = 1 #FILA ACTUAL
        self.columna = 1 #COLUMNA ACTUAL
        estado_actual = 'S0'
        while self.lineas[self.index] != "":
            #print(f'CARACTER11 - {self.lineas[self.index] } | ESTADO - {estado_actual} | FILA - {self.fila}  | COLUMNA - {self.columna}')
            
            # IDENTIFICAR SALTO DE LINEA
            if self.lineas[self.index] == '\n':
                self.fila += 1
                self.columna +=1

            # ************************
            #         ESTADOS
            # ************************
            
            # S0 -> { S1
            elif estado_actual == 'S0':
                estado_actual = self._token('{', 'S0', 'S1')

            # S1 -> "Operacion" S2
            elif estado_actual == 'S1':
                if self.lineas[self.index] != " ":
                    a = self._operaciones('S14')
                    estado_actual = a[0]
                    # print("\t*****RESULTADO*****")
                    # print('\t',a[1])
                    # print('\t*******************************\n')
                    estado_actual = a[0]
            
            # S14 -> }
            elif estado_actual == 'S14':
                #print("ESTO DE ULTIMO")
                estado_actual = self._token('}', 'S14', 'S15')
            
            # S15 -> ,
            elif estado_actual == 'S15':
                if self.lineas[self.index] != ' ':
                    estado_actual = self._token(',', 'S16', 'S0')
                    
            elif estado_actual == 'S16':  
                break
            
            # ERRORES 
            if estado_actual == 'ERROR':
                #print('\t AQUI OCURRIO UN ERROR')
                estado_actual = 'S0'
            
            #INCREMENTAR POSICION
            if self.index < len(self.lineas) - 1:
                self.index +=1
            else:
                break

    def guardarErrores(self, token, fila, columna):
        self.ListaErrores.append({"token":token, "fila": fila, "columna":columna})

    def GuardarErrores(self):
        absolutepath = os.path.abspath(__file__)
        Directorio = os.path.dirname(absolutepath) 
        path = Directorio + r"/ListaErrores.txt"
        if self.ListaErrores:
            # Abre un archivo en modo de escritura
            with open(path, "w") as f:
                f.truncate(0)
                f.write("-----------------Listado de Errores-----------------\n")
                for diccionario in self.ListaErrores:
                    f.write(str(diccionario)+"\n")
                    diccionario.clear()
            tkinter.messagebox.showinfo(title="Analizador de errores", message=("Existen errores en este texto\nRevisa el archivo ListaErrores.txt\nPara visualizar"))	
        else:
            with open(path, "w") as f:
                f.truncate(0)
                f.write("-----------------Listado de Errores-----------------\n")
            tkinter.messagebox.showinfo(title="Analizador de errores", message=("No existen errores en el texto\nRevisa el archivo ListaErrores.txt\nPara visualizar"))	

