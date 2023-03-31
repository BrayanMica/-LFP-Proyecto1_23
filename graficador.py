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
        self.operaciones = None
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
    def h_izq(self):
        return self.hijo_i
    
    # Setter para hijo izquierdo
    @h_izq.setter
    def h_izq(self,valor):
        self.hijo_i = valor
        
    # Getter para hijo derecho
    @property
    def h_der(self):
        return self.hijo_d
    
    # Setter para hijo derecho
    @h_der.setter
    def h_der(self,valor):
        self.hijo_d = valor
        


raiz = Nodo(None)
dato = datos()
dato.operador='Suma'
dato.h_izq=5
dato.h_der=8
resultado=dato.h_izq+dato.h_der
raiz.node = str(dato.operador) + ' = '+ str(resultado)
raiz.left = Nodo(dato.h_izq)
raiz.right = Nodo(dato.h_der)

#     50 - (5 + 8) 
# raiz1 = Nodo(None)
# raiz1.node = 'Resta = 37'
# raiz1.left = Nodo(50)
# raiz1.right = raiz

ListaGrafo = []
def imprimir(_nodo: Nodo):
    if(_nodo.left != None):
        #print("RECURSIVIDAD IZQ")
        imprimir(_nodo.left)
        print(f' "{_nodo.node}" -> "{_nodo.left.node}"')
        ListaGrafo.append(f' "{_nodo.node}" -> "{_nodo.left.node}"')
    if(_nodo.right != None):
        #print("RECURSIVIDAD DER")
        imprimir(_nodo.right)
        print(f' "{_nodo.node}" -> "{_nodo.right.node}"')
        ListaGrafo.append(f' "{_nodo.node}" -> "{_nodo.right.node}"')

def ativador():
    imprimir(raiz)
ativador()