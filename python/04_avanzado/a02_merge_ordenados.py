"""a02 - Merge de dos arrays ordenados  [dificil]

Dadas dos listas `a` y `b` ya ordenadas de menor a mayor, devuelve una nueva lista ordenada con todos sus elementos en O(n + m). No uses `sorted()` ni `sort()` sobre el resultado y no modifiques las listas originales.

Ejemplos:
`merge_ordenados([1, 3, 5], [2, 4, 6])` -> `[1, 2, 3, 4, 5, 6]`
`merge_ordenados([], [7])` -> `[7]`

En la entrevista te preguntarán: ¿Y si tienes k listas ordenadas en vez de 2? (heapq.merge o un min-heap con k elementos: O(N log k)). ¿Y si no caben en memoria? (merge externo: lees por bloques de cada archivo y escribes en streaming; heapq.merge es perezoso). ¿Y hacerlo in-place en `a` que tiene hueco al final? (punteros desde atrás).
"""

# Pista 1: Usa dos índices, uno por lista, y compara los elementos actuales.
# Pista 2: Copia el menor y avanza solo ese índice. Cuando una lista se acabe, ¿qué queda?
# Pista 3: Al terminar el bucle, extiende el resultado con lo que sobre de a[i:] y b[j:]. Usa <= para que sea estable con duplicados.

def merge_ordenados(a, b):
    # tu código aquí
    pass


if __name__ == "__main__":
    assert merge_ordenados([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_ordenados([], []) == [], "ambas vacías"
    assert merge_ordenados([], [7]) == [7]
    assert merge_ordenados([7], []) == [7]
    assert merge_ordenados([1, 1, 2], [1, 3]) == [1, 1, 1, 2, 3], "duplicados"
    assert merge_ordenados([-5, -1, 0], [-3, 2]) == [-5, -3, -1, 0, 2], "negativos"
    assert merge_ordenados([1, 2, 3], [10, 20]) == [1, 2, 3, 10, 20], "una lista entera antes"
    x, y = [1, 4], [2, 3]
    merge_ordenados(x, y)
    assert x == [1, 4] and y == [2, 3], "no debe modificar las entradas"
    print("OK: todos los tests pasan")
