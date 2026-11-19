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
    return sorted(set(a) & set(b))


# Explicacion
# 1) Casos borde a preguntar: listas vacias, repetidos (¿se conservan?), ¿ya ordenadas?, ¿tamanos muy distintos?
# 2) Solucion ingenua: para cada x de a revisar `x in b` (lista): O(n*m) tiempo.
# 3) Mejora y trade-off: pasar la mas pequena a set y recorrer la otra: O(n+m). Trade-off: memoria extra O(min(n,m)). Si ambas estan ordenadas, two pointers da O(n+m) con O(1) extra.
# 4) Codear hablando: narra cada paso en voz alta mientras escribes y nombra las variables con claridad.
# 5) Big-O final: tiempo O(n + m) (mas O(k log k) por ordenar el resultado), espacio O(n + m).
# Pregunta del entrevistador: Si ambas listas ya vienen ordenadas, ¿como evitas usar sets?

if __name__ == "__main__":
    assert interseccion([1, 2, 2, 1], [2, 2]) == [2]
    assert interseccion([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9]
    assert interseccion([], [1, 2]) == [], "una vacia"
    assert interseccion([], []) == []
    assert interseccion([1], [1]) == [1], "un elemento"
    assert interseccion([1, 2], [3, 4]) == [], "sin comunes"
    print("OK: todos los tests pasan")
