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
    # tu codigo aqui
    pass


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
