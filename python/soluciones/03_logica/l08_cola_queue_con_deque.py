"""Cola (Queue) con deque

Implementa la clase `Cola` (FIFO) usando `collections.deque`, con los metodos:
- `encolar(x)`: agrega al final.
- `desencolar()`: quita y devuelve el primero; lanza `IndexError` si esta vacia.
- `frente()`: devuelve el primero sin quitarlo; lanza `IndexError` si esta vacia.
- `vacia()` y `len(cola)`.
Ejemplo: encolar(1), encolar(2), desencolar() -> 1.

Pistas:
  1. `deque` permite sacar por la izquierda en O(1) con `popleft()`.
  2. Guarda `self.items = deque()`.
  3. `list.pop(0)` es O(n); por eso se usa deque.
"""

from collections import deque


class Cola:
    def __init__(self):
        self.items = deque()

    def encolar(self, x):
        self.items.append(x)

    def desencolar(self):
        if self.vacia():
            raise IndexError("cola vacia")
        return self.items.popleft()

    def frente(self):
        if self.vacia():
            raise IndexError("cola vacia")
        return self.items[0]

    def vacia(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)


# Explicacion
# 1) Casos borde a preguntar: ¿cola vacia: excepcion o None?, ¿capacidad limitada?, ¿hay prioridades?
# 2) Solucion ingenua: una lista con `pop(0)` para desencolar: cada desencolar es O(n) porque desplaza todo.
# 3) Mejora y trade-off: `deque` (lista doblemente enlazada de bloques) hace append y popleft en O(1). Trade-off: indexar en el medio es O(n).
# 4) Codear hablando: narra cada paso en voz alta mientras escribes y nombra las variables con claridad.
# 5) Big-O final: encolar, desencolar, frente: O(1) tiempo; espacio O(n).
# Pregunta del entrevistador: ¿Como implementarias una cola usando dos pilas?

if __name__ == "__main__":
    c = Cola()
    assert c.vacia() is True
    assert len(c) == 0
    c.encolar(1)
    c.encolar(2)
    c.encolar(3)
    assert c.frente() == 1
    assert len(c) == 3
    assert c.desencolar() == 1, "FIFO"
    assert c.desencolar() == 2
    assert c.desencolar() == 3
    assert c.vacia() is True
    try:
        c.desencolar()
        assert False, "desencolar en vacia debe lanzar IndexError"
    except IndexError:
        pass
    try:
        c.frente()
        assert False, "frente en vacia debe lanzar IndexError"
    except IndexError:
        pass
    print("OK: todos los tests pasan")
