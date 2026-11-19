"""BST: insertar, buscar, inorden y altura

Implementa un arbol binario de busqueda con la clase `BST` (y `NodoBST` con `valor`, `izq`, `der`):
- `insertar(valor)`: inserta; si el valor ya existe, lo ignora.
- `buscar(valor)`: True/False.
- `inorden()`: lista de valores en orden izquierda-raiz-derecha (sale ordenada).
- `altura()`: numero de niveles (arbol vacio = 0, un solo nodo = 1).
Ejemplo: insertar 5, 3, 8, 1 -> `inorden()` = [1, 3, 5, 8], `altura()` = 3.

Pistas:
  1. Menores van a la izquierda, mayores a la derecha.
  2. Recorrer inorden recursivamente: izquierda, la raiz, derecha.
  3. altura(nodo) = 0 si es None, si no 1 + max(altura(izq), altura(der)).
"""

class NodoBST:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None


class BST:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        nuevo = NodoBST(valor)
        if self.raiz is None:
            self.raiz = nuevo
            return
        actual = self.raiz
        while True:
            if valor == actual.valor:
                return
            if valor < actual.valor:
                if actual.izq is None:
                    actual.izq = nuevo
                    return
                actual = actual.izq
            else:
                if actual.der is None:
                    actual.der = nuevo
                    return
                actual = actual.der

    def buscar(self, valor):
        actual = self.raiz
        while actual is not None:
            if valor == actual.valor:
                return True
            actual = actual.izq if valor < actual.valor else actual.der
        return False

    def inorden(self):
        resultado = []

        def visitar(nodo):
            if nodo is None:
                return
            visitar(nodo.izq)
            resultado.append(nodo.valor)
            visitar(nodo.der)

        visitar(self.raiz)
        return resultado

    def altura(self):
        def h(nodo):
            if nodo is None:
                return 0
            return 1 + max(h(nodo.izq), h(nodo.der))

        return h(self.raiz)


# Explicacion
# 1) Casos borde a preguntar: arbol vacio, duplicados (¿ignorar, contar o permitir?), arbol degenerado (lista), ¿altura en nodos o aristas?
# 2) Solucion ingenua: guardar los valores en una lista y buscar linealmente: buscar O(n); mantenerla ordenada cuesta O(n) por insercion.
# 3) Mejora y trade-off: BST: cada comparacion descarta un subarbol. Trade-off: solo es O(log n) si el arbol esta balanceado; con datos ya ordenados degenera en lista (O(n)). Los arboles AVL o rojo-negro garantizan el balance a cambio de mas complejidad.
# 4) Codear hablando: narra cada paso en voz alta mientras escribes y nombra las variables con claridad.
# 5) Big-O final: insertar/buscar O(h) con h la altura (O(log n) promedio, O(n) peor caso); inorden y altura O(n) tiempo y O(h) espacio de pila; espacio total O(n).
# Pregunta del entrevistador: ¿Que pasa si insertas 1, 2, 3, 4, 5 en orden? ¿Como lo arreglas? ¿Como validas que un arbol es un BST?

if __name__ == "__main__":
    t = BST()
    assert t.inorden() == [], "arbol vacio"
    assert t.altura() == 0, "altura vacio"
    assert t.buscar(1) is False, "buscar en vacio"
    t.insertar(5)
    assert t.altura() == 1, "un nodo"
    assert t.inorden() == [5]
    for v in [3, 8, 1, 4, 7, 9, 3]:
        t.insertar(v)
    assert t.inorden() == [1, 3, 4, 5, 7, 8, 9], "inorden ordenado y sin duplicados"
    assert t.buscar(7) is True
    assert t.buscar(1) is True
    assert t.buscar(6) is False
    assert t.altura() == 3
    cadena = BST()
    for v in [1, 2, 3, 4]:
        cadena.insertar(v)
    assert cadena.altura() == 4, "arbol degenerado"
    assert cadena.inorden() == [1, 2, 3, 4]
    print("OK: todos los tests pasan")
