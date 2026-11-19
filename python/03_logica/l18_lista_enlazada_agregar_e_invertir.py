"""Lista enlazada: agregar e invertir

Implementa `Nodo` (atributos `valor` y `siguiente`) y `ListaEnlazada` con:
- `agregar(valor)`: agrega al final.
- `invertir()`: invierte la lista IN-PLACE (cambiando los punteros, sin crear nodos nuevos).
- `a_lista()`: devuelve los valores como una lista de Python, de cabeza a cola.
Ejemplo: agregar 1, 2, 3 -> `a_lista()` = [1, 2, 3]; tras `invertir()` -> [3, 2, 1].

Pistas:
  1. Guarda `self.cabeza` (None si esta vacia).
  2. Para invertir necesitas tres variables: `previo`, `actual` y `siguiente`.
  3. En cada paso: guarda `siguiente = actual.siguiente`, apunta `actual.siguiente = previo`, avanza ambos. Al final `self.cabeza = previo`.
"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class ListaEnlazada:
    # tu codigo aqui
    pass


if __name__ == "__main__":
    l = ListaEnlazada()
    assert l.a_lista() == [], "vacia"
    l.invertir()
    assert l.a_lista() == [], "invertir vacia no falla"
    l.agregar(1)
    assert l.a_lista() == [1], "un elemento"
    l.invertir()
    assert l.a_lista() == [1]
    l.agregar(2)
    l.agregar(3)
    assert l.a_lista() == [1, 2, 3]
    l.invertir()
    assert l.a_lista() == [3, 2, 1]
    l.agregar(0)
    assert l.a_lista() == [3, 2, 1, 0], "agregar sigue al final tras invertir"
    l.invertir()
    assert l.a_lista() == [0, 1, 2, 3]
    print("OK: todos los tests pasan")
