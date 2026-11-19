"""a03 - Merge de intervalos  [dificil]

Dada una lista de intervalos `[inicio, fin]` (sin orden), fusiona los que se solapen o se toquen (`[1,4]` y `[4,5]` se fusionan) y devuelve la lista de intervalos disjuntos ordenada por inicio.

Ejemplos:
`merge_intervalos([[1,3],[2,6],[8,10],[15,18]])` -> `[[1,6],[8,10],[15,18]]`
`merge_intervalos([[1,4],[4,5]])` -> `[[1,5]]`

En la entrevista te preguntarán: ¿Y si los intervalos llegan en streaming y debes mantener la lista fusionada? (estructura ordenada + bisect; o un árbol de intervalos). Variante: ¿cuál es el mínimo de salas de reuniones necesarias? (ordenar inicios y fines por separado, o heap de fines).
"""

# Pista 1: Si los ordenas por inicio, los que se solapan quedan consecutivos.
# Pista 2: Recorre y compara el inicio del actual con el fin del último intervalo del resultado.
# Pista 3: Si inicio <= fin_ultimo: fin_ultimo = max(fin_ultimo, fin). Si no, añade uno nuevo. Ojo con [1,4] y [2,3] (uno contiene al otro).

def merge_intervalos(intervalos):
    # tu código aquí
    pass


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
