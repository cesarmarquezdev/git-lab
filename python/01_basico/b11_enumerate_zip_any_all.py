r"""b11 - enumerate, zip, any y all (facil)

Implementa:

1. `posiciones(lista, x)`: lista de indices donde aparece `x` (usa `enumerate`).
   `posiciones([1, 2, 1], 1)` -> `[0, 2]`
2. `emparejar(claves, valores)`: dict que une ambas listas con `zip`; si tienen distinto largo, se corta a la mas corta.
   `emparejar(['a', 'b'], [1, 2, 3])` -> `{'a': 1, 'b': 2}`
3. `todos_aprobados(notas, minimo=60)`: `True` si TODAS las notas son >= minimo (usa `all`). Lista vacia -> `True`.
4. `hay_negativos(nums)`: `True` si ALGUN numero es negativo (usa `any`). Lista vacia -> `False`.
5. `resumen(nums)`: tupla `(minimo, maximo, suma, cantidad)`; para lista vacia devuelve `(None, None, 0, 0)`.
"""

# Pista 1: `for i, v in enumerate(lista)`.
# Pista 2: `dict(zip(claves, valores))`.
# Pista 3: `all([])` es True y `any([])` es False. Para resumen, comprueba la lista vacia antes de `min`/`max` (lanzan ValueError).

def posiciones(lista, x):
    pass


def emparejar(claves, valores):
    pass


def todos_aprobados(notas, minimo=60):
    pass


def hay_negativos(nums):
    pass


def resumen(nums):
    pass

if __name__ == "__main__":
    assert posiciones([1, 2, 1], 1) == [0, 2]
    assert posiciones([], 1) == [], "vacia"
    assert posiciones([5], 9) == [], "no esta"
    assert emparejar(['a', 'b'], [1, 2, 3]) == {'a': 1, 'b': 2}
    assert emparejar([], [1]) == {}
    assert todos_aprobados([70, 60, 90]) is True
    assert todos_aprobados([70, 59]) is False
    assert todos_aprobados([]) is True, "all de vacio es True"
    assert todos_aprobados([5, 6], minimo=5) is True, "keyword"
    assert hay_negativos([1, -1]) is True
    assert hay_negativos([0, 1]) is False
    assert hay_negativos([]) is False, "any de vacio es False"
    assert resumen([3, 1, 2]) == (1, 3, 6, 3)
    assert resumen([]) == (None, None, 0, 0)
    assert resumen([4]) == (4, 4, 4, 1)
    print("OK: todos los tests pasan")
