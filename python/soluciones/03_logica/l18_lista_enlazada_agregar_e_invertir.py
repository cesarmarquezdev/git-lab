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
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo
            return
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo

    def invertir(self):
        previo = None
        actual = self.cabeza
        while actual is not None:
            siguiente = actual.siguiente
            actual.siguiente = previo
            previo = actual
            actual = siguiente
        self.cabeza = previo

    def a_lista(self):
        resultado = []
        actual = self.cabeza
        while actual is not None:
            resultado.append(actual.valor)
            actual = actual.siguiente
        return resultado


# Explicacion
# 1) Casos borde a preguntar: lista vacia, un nodo, ¿simple o doble enlazada?, ¿hay ciclos?, ¿in-place?
# 2) Solucion ingenua: volcar a una lista de Python, invertirla y reconstruir nodos: O(n) tiempo y O(n) espacio.
# 3) Mejora y trade-off: invertir punteros con tres variables (previo, actual, siguiente) en una sola pasada. Trade-off: hay que cuidar guardar `siguiente` antes de sobrescribir el puntero, o pierdes el resto de la lista.
# 4) Codear hablando: narra cada paso en voz alta mientras escribes y nombra las variables con claridad.
# 5) Big-O final: invertir O(n) tiempo, O(1) espacio; agregar al final O(n) (se puede O(1) guardando una referencia a la cola); a_lista O(n) / O(n).
# Pregunta del entrevistador: ¿Como lo harias recursivamente? ¿Y como detectas un ciclo en la lista?

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
