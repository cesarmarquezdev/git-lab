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

def posiciones(lista, x):
    return [i for i, v in enumerate(lista) if v == x]


def emparejar(claves, valores):
    return dict(zip(claves, valores))


def todos_aprobados(notas, minimo=60):
    return all(n >= minimo for n in notas)


def hay_negativos(nums):
    return any(n < 0 for n in nums)


def resumen(nums):
    if not nums:
        return (None, None, 0, 0)
    return (min(nums), max(nums), sum(nums), len(nums))

# Explicacion: enumerate evita `range(len(lista))`. zip se detiene en el iterable mas corto (zip_longest si no quieres eso). any/all hacen cortocircuito: paran en cuanto saben la respuesta. Todo O(n).
# Pregunta del entrevistador: ¿Por que `all([])` es True? (Verdad vacua: no existe ningun elemento que incumpla la condicion.)

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
