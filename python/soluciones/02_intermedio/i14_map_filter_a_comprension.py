"""i14 - map/filter a comprensión (SOLUCIÓN)
"""

def cuadrados_pares(nums):
    return [x * x for x in nums if x % 2 == 0]


def cuadrados_pares_perezoso(nums):
    return (x * x for x in nums if x % 2 == 0)


def longitudes(palabras):
    return {p: len(p) for p in palabras if len(p) > 2}

# Explicación:
# `map`/`filter` con `lambda` son funcionales pero menos legibles; en Python lo idiomático es la comprensión. Complejidad idéntica O(n); `map`/`filter` devuelven iteradores perezosos (por eso el `list(...)`), y su equivalente perezoso es la expresión generadora. `map(str, xs)` con una función ya existente es de los pocos casos donde map sigue siendo razonable (a veces algo más rápido).
# Entrevistador: ¿Cuándo preferirías map con una función nombrada sobre la comprensión? ¿Qué diferencia de memoria hay entre [..] y (..) con 10 millones de elementos?


if __name__ == "__main__":
    import types

    def cuadrados_pares_viejo(nums):
        return list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, nums)))

    for caso in ([1, 2, 3, 4], [], [3], [2], [-2, 0, 5]):
        assert cuadrados_pares(caso) == cuadrados_pares_viejo(caso), caso
    assert cuadrados_pares([1, 2, 3, 4]) == [4, 16]
    g = cuadrados_pares_perezoso([1, 2, 3, 4])
    assert isinstance(g, types.GeneratorType), "debe ser expresión generadora"
    assert list(g) == [4, 16]
    assert list(g) == [], "un generador se agota"
    assert longitudes(["a", "casa", "sol"]) == {"casa": 4, "sol": 3}
    assert longitudes([]) == {}
    assert longitudes(["ab"]) == {}
    print("OK: todos los tests pasan")
