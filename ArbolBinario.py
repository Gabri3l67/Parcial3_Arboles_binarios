
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def amplitud(self):
        if not self.raiz:
            return []
        cola = [self.raiz]
        resultado = []
        while cola:
            nodo = cola.pop(0)
            resultado.append(nodo.valor)
            if nodo.izquierdo:
                cola.append(nodo.izquierdo)
            if nodo.derecho:
                cola.append(nodo.derecho)
        return resultado

    def preorden(self, nodo, resultado):
        if nodo:
            resultado.append(nodo.valor)
            self.preorden(nodo.izquierdo, resultado)
            self.preorden(nodo.derecho, resultado)
        return resultado

    def inorden(self, nodo, resultado):
        if nodo:
            self.inorden(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self.inorden(nodo.derecho, resultado)
        return resultado

    def postorden(self, nodo, resultado):
        if nodo:
            self.postorden(nodo.izquierdo, resultado)
            self.postorden(nodo.derecho, resultado)
            resultado.append(nodo.valor)
        return resultado

def crear_arbol(tipo):
    arbol = ArbolBinario()
    if tipo == 1:
        # Árbol 1 (h → i → m → e → a)
        arbol.raiz = Nodo('h')
        arbol.raiz.izquierdo = Nodo('i')
        arbol.raiz.derecho = Nodo('m')
        arbol.raiz.izquierdo.izquierdo = Nodo('e')
        arbol.raiz.derecho.izquierdo = Nodo('a')
    elif tipo == 2:
        # Árbol 2 (F → B → G → A → D → I → C → E → H)
        arbol.raiz = Nodo('F')
        arbol.raiz.izquierdo = Nodo('B')
        arbol.raiz.derecho = Nodo('G')
        arbol.raiz.izquierdo.izquierdo = Nodo('A')
        arbol.raiz.izquierdo.derecho = Nodo('D')
        arbol.raiz.izquierdo.derecho.izquierdo = Nodo('C')
        arbol.raiz.izquierdo.derecho.derecho = Nodo('E')
        arbol.raiz.derecho.derecho = Nodo('I')
        arbol.raiz.derecho.derecho.izquierdo = Nodo('H')
    elif tipo == 3:
        # Árbol 3 (55 → 53 → 59 → 48 → 54 → 56 → 63 → 51 → 57 → 61 → 70)
        arbol.raiz = Nodo(55)
        arbol.raiz.izquierdo = Nodo(53)
        arbol.raiz.derecho = Nodo(59)
        arbol.raiz.izquierdo.izquierdo = Nodo(48)
        arbol.raiz.izquierdo.derecho = Nodo(54)
        arbol.raiz.izquierdo.izquierdo.derecho = Nodo(51)
        arbol.raiz.derecho.izquierdo = Nodo(56)
        arbol.raiz.derecho.izquierdo.derecho = Nodo(57)
        arbol.raiz.derecho.derecho = Nodo(63)
        arbol.raiz.derecho.derecho.izquierdo = Nodo(61)
        arbol.raiz.derecho.derecho.derecho = Nodo(70)
    elif tipo == 4:
        # Árbol 4 (A → B → C → D → E → ...)
        arbol.raiz = Nodo('A')
        arbol.raiz.izquierdo = Nodo('B')
        arbol.raiz.derecho = Nodo('C')
        arbol.raiz.izquierdo.izquierdo = Nodo('D')
        arbol.raiz.izquierdo.derecho = Nodo('E')
        arbol.raiz.derecho.izquierdo = Nodo('F')
        arbol.raiz.derecho.derecho = Nodo('G')
        arbol.raiz.izquierdo.derecho.izquierdo = Nodo('J')
        arbol.raiz.izquierdo.derecho.derecho = Nodo('K')
        arbol.raiz.derecho.izquierdo.izquierdo = Nodo('L')
        arbol.raiz.derecho.izquierdo.derecho = Nodo('M')
        arbol.raiz.derecho.derecho.izquierdo = Nodo('N')
        arbol.raiz.derecho.derecho.derecho = Nodo('O')
    return arbol