"""Pila (Stack) a mano

Implementa la clase `Pila` (LIFO) usando una lista interna, con los metodos:
- `push(x)`: agrega al tope.
- `pop()`: quita y devuelve el tope; lanza `IndexError` si esta vacia.
- `peek()`: devuelve el tope sin quitarlo; lanza `IndexError` si esta vacia.
- `vacia()`: True si no hay elementos.
- `len(pila)` debe funcionar (`__len__`).
Ejemplo: push(1), push(2), pop() -> 2.

Pistas:
  1. El tope es el final de la lista: `append` y `pop()` son O(1).
  2. Guarda la lista en `self.items` dentro de `__init__`.
  3. Para el error: `if self.vacia(): raise IndexError("pila vacia")`.
"""

class Pila:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.vacia():
            raise IndexError("pila vacia")
        return self.items.pop()

    def peek(self):
        if self.vacia():
            raise IndexError("pila vacia")
        return self.items[-1]

    def vacia(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)


# Explicacion
# 1) Casos borde a preguntar: ¿que pasa al hacer pop/peek en vacia (excepcion o None)?, ¿capacidad maxima?, ¿tipos de elementos?
# 2) Solucion ingenua: una lista donde insertas y quitas al inicio: `insert(0, x)` y `pop(0)` son O(n).
# 3) Mejora y trade-off: usar el final de la lista como tope: `append`/`pop()` son O(1) amortizado. Trade-off: ninguno relevante; la lista de Python ya es un array dinamico.
# 4) Codear hablando: narra cada paso en voz alta mientras escribes y nombra las variables con claridad.
# 5) Big-O final: push, pop, peek, vacia: O(1) tiempo; espacio O(n) para n elementos.
# Pregunta del entrevistador: ¿Como harias que ademas devolviera el minimo en O(1) (min stack)?

if __name__ == "__main__":
    p = Pila()
    assert p.vacia() is True
    assert len(p) == 0
    p.push(1)
    p.push(2)
    assert p.peek() == 2
    assert len(p) == 2
    assert p.pop() == 2
    assert p.pop() == 1, "LIFO"
    assert p.vacia() is True
    try:
        p.pop()
        assert False, "pop en pila vacia debe lanzar IndexError"
    except IndexError:
        pass
    try:
        p.peek()
        assert False, "peek en pila vacia debe lanzar IndexError"
    except IndexError:
        pass
    print("OK: todos los tests pasan")
