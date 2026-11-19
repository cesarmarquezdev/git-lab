"""i14 - map/filter a comprensión (media)

Esta función usa `map` y `filter`:
```
def cuadrados_pares_viejo(nums):
    return list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, nums)))
```
Reescribe:
1. `cuadrados_pares(nums)` con una **comprensión de lista** (mismo resultado).
2. `cuadrados_pares_perezoso(nums)` con una **expresión generadora** (devuelve un generador, no una lista).
3. `longitudes(palabras)` con una **comprensión de diccionario** `{palabra: len(palabra)}` solo para palabras de más de 2 letras.

Ejemplo:
```
cuadrados_pares([1,2,3,4])  # [4, 16]
longitudes(['a', 'casa', 'sol'])  # {'casa': 4, 'sol': 3}
```

Pistas (no mires hasta intentarlo):
Pista 1: Forma: `[expresión for x in iterable if condición]`.
Pista 2: La expresión generadora usa paréntesis en vez de corchetes: `(x*x for x in nums if ...)`.
Pista 3: Comprensión de dict: `{k: v for k in ... if ...}`.

Entrevistador: ¿Cuándo preferirías map con una función nombrada sobre la comprensión? ¿Qué diferencia de memoria hay entre [..] y (..) con 10 millones de elementos?
"""

def cuadrados_pares(nums):
    pass


def cuadrados_pares_perezoso(nums):
    pass


def longitudes(palabras):
    pass


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
