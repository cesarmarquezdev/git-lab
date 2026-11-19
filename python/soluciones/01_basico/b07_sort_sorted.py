r"""b07 - sort vs sorted (facil)

Implementa:

1. `ordenada_desc(lista)`: devuelve una lista NUEVA ordenada de mayor a menor SIN modificar la original (usa `sorted`).
2. `ordenar_en_sitio(lista)`: ordena `lista` de menor a mayor modificandola (usa `.sort()`); devuelve `None`.
3. `por_longitud(palabras)`: devuelve una lista nueva de palabras ordenada por longitud y, en empate, alfabeticamente. Usa `key=` (con lambda o tupla).

Ejemplos:
`ordenada_desc([3, 1, 2])` -> `[3, 2, 1]` (la original queda `[3, 1, 2]`)
`por_longitud(['pez', 'a', 'gato', 'ave'])` -> `['a', 'ave', 'pez', 'gato']`
"""

def ordenada_desc(lista):
    return sorted(lista, reverse=True)


def ordenar_en_sitio(lista):
    lista.sort()


def por_longitud(palabras):
    return sorted(palabras, key=lambda p: (len(p), p))

# Explicacion: sorted acepta cualquier iterable y devuelve lista nueva (O(n) espacio); sort es in-place, solo listas. Ambos usan Timsort: O(n log n) y estables. key recibe una funcion que extrae la clave de comparacion; una tupla ordena por multiples criterios.
# Pregunta del entrevistador: ¿Que significa que el sort sea estable y por que importa? (Elementos con la misma clave conservan su orden relativo; permite ordenar por varias claves en pasadas.)

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
