r"""b07 - sort vs sorted (facil)

Implementa:

1. `ordenada_desc(lista)`: devuelve una lista NUEVA ordenada de mayor a menor SIN modificar la original (usa `sorted`).
2. `ordenar_en_sitio(lista)`: ordena `lista` de menor a mayor modificandola (usa `.sort()`); devuelve `None`.
3. `por_longitud(palabras)`: devuelve una lista nueva de palabras ordenada por longitud y, en empate, alfabeticamente. Usa `key=` (con lambda o tupla).

Ejemplos:
`ordenada_desc([3, 1, 2])` -> `[3, 2, 1]` (la original queda `[3, 1, 2]`)
`por_longitud(['pez', 'a', 'gato', 'ave'])` -> `['a', 'ave', 'pez', 'gato']`
"""

# Pista 1: `sorted(x, reverse=True)` no toca x. `x.sort()` si, y devuelve None.
# Pista 2: Error clasico: `return lista.sort()` devuelve None.
# Pista 3: `key=lambda p: (len(p), p)`

def ordenada_desc(lista):
    pass


def ordenar_en_sitio(lista):
    pass


def por_longitud(palabras):
    pass

if __name__ == "__main__":
    orig = [3, 1, 2]
    assert ordenada_desc(orig) == [3, 2, 1]
    assert orig == [3, 1, 2], "sorted no muta la original"
    assert ordenada_desc([]) == [], "vacia"
    assert ordenada_desc([5]) == [5]
    l = [3, 1, 2]
    assert ordenar_en_sitio(l) is None, ".sort() devuelve None"
    assert l == [1, 2, 3]
    l = []
    ordenar_en_sitio(l)
    assert l == []
    assert por_longitud(['pez', 'a', 'gato', 'ave']) == ['a', 'ave', 'pez', 'gato']
    assert por_longitud([]) == []
    print("OK: todos los tests pasan")
