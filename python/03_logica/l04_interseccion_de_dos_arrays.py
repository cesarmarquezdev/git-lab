"""Interseccion de dos arrays

Escribe `interseccion(a, b)` que devuelva una lista ordenada con los elementos que estan en ambas listas, sin repetidos.
Ejemplos:
`interseccion([1, 2, 2, 1], [2, 2])` -> [2]
`interseccion([4, 9, 5], [9, 4, 9, 8, 4])` -> [4, 9]

Pistas:
  1. Convertir a set permite buscar en O(1).
  2. La interseccion de sets se escribe con `&`.
  3. `sorted(set(a) & set(b))`.
"""

def interseccion(a, b):
    # tu codigo aqui
    pass


if __name__ == "__main__":
    assert interseccion([1, 2, 2, 1], [2, 2]) == [2]
    assert interseccion([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9]
    assert interseccion([], [1, 2]) == [], "una vacia"
    assert interseccion([], []) == []
    assert interseccion([1], [1]) == [1], "un elemento"
    assert interseccion([1, 2], [3, 4]) == [], "sin comunes"
    print("OK: todos los tests pasan")
