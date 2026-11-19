"""i12 - Deque: ventana de los últimos N y rotar (media)

1. Clase `UltimosN(n)`: mantiene solo los últimos `n` valores agregados. Métodos: `agregar(x)`, `valores()` (lista, del más viejo al más nuevo) y `promedio()` (float, o `None` si no hay valores).
2. Función `rotar(lista, k)`: devuelve una **nueva** lista con los elementos desplazados `k` posiciones a la derecha (`k` puede ser negativo o mayor que la longitud).

Ejemplo:
```
u = UltimosN(3); [u.agregar(i) for i in range(5)]; u.valores()  # [2, 3, 4]
rotar([1,2,3,4,5], 2)  # [4, 5, 1, 2, 3]
```

Pistas (no mires hasta intentarlo):
Pista 1: `collections.deque(maxlen=n)` descarta automáticamente por el extremo opuesto al agregar.
Pista 2: `deque.append` y `popleft` son O(1); `list.pop(0)` es O(n).
Pista 3: `deque.rotate(k)` rota a la derecha con k positivo. Maneja lista vacía.

Entrevistador: ¿Cómo harías promedio() en O(1)? ¿Por qué no usar una lista con `pop(0)` para la ventana? ¿Cuándo es mejor una lista que un deque?
"""

from collections import deque


class UltimosN:
    def __init__(self, n):
        pass

    def agregar(self, x):
        pass

    def valores(self):
        pass

    def promedio(self):
        pass


def rotar(lista, k):
    pass


if __name__ == "__main__":
    u = UltimosN(3)
    assert u.valores() == [], "vacío"
    assert u.promedio() is None, "promedio sin datos"
    u.agregar(10)
    assert u.valores() == [10] and u.promedio() == 10, "un elemento"
    for i in range(5):
        u.agregar(i)
    assert u.valores() == [2, 3, 4], "solo los últimos 3"
    assert u.promedio() == 3.0
    assert rotar([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert rotar([1, 2, 3], -1) == [2, 3, 1], "k negativo"
    assert rotar([1, 2, 3], 7) == [3, 1, 2], "k mayor que la longitud"
    assert rotar([], 3) == [], "lista vacía"
    original = [1, 2, 3]
    rotar(original, 1)
    assert original == [1, 2, 3], "no modifica la original"
    print("OK: todos los tests pasan")
