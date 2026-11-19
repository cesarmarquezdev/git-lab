"""a03 - Merge de intervalos  [dificil]

Dada una lista de intervalos `[inicio, fin]` (sin orden), fusiona los que se solapen o se toquen (`[1,4]` y `[4,5]` se fusionan) y devuelve la lista de intervalos disjuntos ordenada por inicio.

Ejemplos:
`merge_intervalos([[1,3],[2,6],[8,10],[15,18]])` -> `[[1,6],[8,10],[15,18]]`
`merge_intervalos([[1,4],[4,5]])` -> `[[1,5]]`

En la entrevista te preguntarán: ¿Y si los intervalos llegan en streaming y debes mantener la lista fusionada? (estructura ordenada + bisect; o un árbol de intervalos). Variante: ¿cuál es el mínimo de salas de reuniones necesarias? (ordenar inicios y fines por separado, o heap de fines).
"""

# EXPLICACIÓN
# 1) Ingenua: comparar cada intervalo con todos los demás y repetir hasta que no haya fusiones -> O(n^2) o peor.
# 2) Óptima: ordenar por inicio. Tras ordenar, un intervalo solo puede solaparse con el último del resultado, así que basta un barrido. Trade-off: pagamos el sort (O(n log n)) para simplificar todo lo demás.
# 3) Final: O(n log n) tiempo (domina el sort), O(n) espacio para el resultado. Detalle: el max() en el fin es lo que cubre el caso de contención.
#
# PREGUNTA DEL ENTREVISTADOR
# ¿Y si los intervalos llegan en streaming y debes mantener la lista fusionada? (estructura ordenada + bisect; o un árbol de intervalos). Variante: ¿cuál es el mínimo de salas de reuniones necesarias? (ordenar inicios y fines por separado, o heap de fines).

def merge_intervalos(intervalos):
    res = []
    for ini, fin in sorted(intervalos):
        if res and ini <= res[-1][1]:
            res[-1][1] = max(res[-1][1], fin)
        else:
            res.append([ini, fin])
    return res


if __name__ == "__main__":
    assert merge_intervalos([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge_intervalos([[1, 4], [4, 5]]) == [[1, 5]], "se tocan en el borde"
    assert merge_intervalos([]) == [], "vacío"
    assert merge_intervalos([[3, 4]]) == [[3, 4]], "un elemento"
    assert merge_intervalos([[1, 4], [2, 3]]) == [[1, 4]], "uno contenido en otro"
    assert merge_intervalos([[5, 6], [1, 2]]) == [[1, 2], [5, 6]], "sin ordenar"
    assert merge_intervalos([[-5, -2], [-3, 1]]) == [[-5, 1]], "negativos"
    assert merge_intervalos([[1, 10], [2, 3], [4, 5], [6, 12]]) == [[1, 12]]
    print("OK: todos los tests pasan")
