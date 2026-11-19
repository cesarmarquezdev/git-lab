"""a02 - Merge de dos arrays ordenados  [dificil]

Dadas dos listas `a` y `b` ya ordenadas de menor a mayor, devuelve una nueva lista ordenada con todos sus elementos en O(n + m). No uses `sorted()` ni `sort()` sobre el resultado y no modifiques las listas originales.

Ejemplos:
`merge_ordenados([1, 3, 5], [2, 4, 6])` -> `[1, 2, 3, 4, 5, 6]`
`merge_ordenados([], [7])` -> `[7]`

En la entrevista te preguntarán: ¿Y si tienes k listas ordenadas en vez de 2? (heapq.merge o un min-heap con k elementos: O(N log k)). ¿Y si no caben en memoria? (merge externo: lees por bloques de cada archivo y escribes en streaming; heapq.merge es perezoso). ¿Y hacerlo in-place en `a` que tiene hueco al final? (punteros desde atrás).
"""

# EXPLICACIÓN
# 1) Ingenua: concatenar y ordenar -> O((n+m) log(n+m)); ignora que ya vienen ordenadas.
# 2) Óptima: dos punteros. El menor de los dos 'frentes' es siempre el siguiente del resultado. Cada elemento se mira una vez. Trade-off: usa O(n+m) de memoria extra para el resultado (se puede hacer in-place si una lista tiene espacio libre al final, rellenando desde atrás).
# 3) Final: O(n+m) tiempo, O(n+m) espacio. Es exactamente el paso 'merge' de merge sort.
#
# PREGUNTA DEL ENTREVISTADOR
# ¿Y si tienes k listas ordenadas en vez de 2? (heapq.merge o un min-heap con k elementos: O(N log k)). ¿Y si no caben en memoria? (merge externo: lees por bloques de cada archivo y escribes en streaming; heapq.merge es perezoso). ¿Y hacerlo in-place en `a` que tiene hueco al final? (punteros desde atrás).

def merge_ordenados(a, b):
    i = j = 0
    res = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    res.extend(a[i:])
    res.extend(b[j:])
    return res


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
