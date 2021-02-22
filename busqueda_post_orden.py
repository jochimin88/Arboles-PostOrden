


# Mi clase Nodo post-orden


class Nodo:
    """
    Recorre en postorden el subarbol izquierdo
    Recorre en postorden el subarbol derecho
    Visita la raiz del arbol.
    """
    def __init__(self, dato):
        self.izquierda = None
        self.derecha = None
        self.dato = dato
 
def insertar(raiz, nodo):


    if raiz is None:
        raiz = nodo
    else:
        if raiz.dato < nodo.dato:
            if raiz.derecha is None:
                raiz.derecha = nodo
            else:
                insertar(raiz.derecha, nodo)
        else:
            if raiz.izquierda is None:
                raiz.izquierda = nodo
            else:
                insertar(raiz.izquierda, nodo)

def postorden(raiz):
    if raiz is not None:
        postorden(raiz.izquierda)
        postorden(raiz.derecha)
        print(raiz.dato)

raiz = Nodo(21)
insertar(raiz, Nodo(13))
insertar(raiz, Nodo(10))
insertar(raiz, Nodo(33))
insertar(raiz, Nodo(18))
insertar(raiz, Nodo(25))
insertar(raiz, Nodo(40))

postorden(raiz)

