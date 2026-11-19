"""i12 - Deque: ventana de los últimos N y rotar (SOLUCIÓN)
"""

from collections import deque


class UltimosN:
    def __init__(self, n):
        self._datos = deque(maxlen=n)

    def agregar(self, x):
        self._datos.append(x)

    def valores(self):
        return list(self._datos)

    def promedio(self):
        if not self._datos:
            return None
        return sum(self._datos) / len(self._datos)


def rotar(lista, k):
    d = deque(lista)
    d.rotate(k)
    return list(d)

# Explicación:
# `deque` es una lista doblemente enlazada por bloques: append/pop/popleft/appendleft en O(1), mientras que `list.insert(0, x)` o `pop(0)` son O(n). Con `maxlen` es un buffer circular perfecto para ventanas deslizantes (agregar O(1)). `rotate` es O(k mod n). Contrapartida: indexar en el medio es O(n). `promedio` es O(n); podrías mantener una suma acumulada para O(1).
# Entrevistador: ¿Cómo harías promedio() en O(1)? ¿Por qué no usar una lista con `pop(0)` para la ventana? ¿Cuándo es mejor una lista que un deque?


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
