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
    # tu codigo aqui
    pass


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
