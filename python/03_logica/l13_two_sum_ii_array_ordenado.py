"""Two Sum II: array ordenado

Dado un array de enteros ya ordenado de menor a mayor, escribe `two_sum_ordenado(nums, objetivo)` que devuelva `[i, j]` (i < j, indices base 0) con `nums[i] + nums[j] == objetivo`, o `[]` si no hay. Hazlo con O(1) de espacio extra.
Ejemplos:
`two_sum_ordenado([2, 7, 11, 15], 9)` -> [0, 1]
`two_sum_ordenado([1, 2, 3, 4, 4, 9], 8)` -> [3, 4]

Pistas:
  1. Como esta ordenado, el menor esta a la izquierda y el mayor a la derecha.
  2. Pon un puntero en cada extremo y mira la suma.
  3. Suma muy grande: baja `j`; suma muy pequena: sube `i`.
"""

def two_sum_ordenado(nums, objetivo):
    # tu codigo aqui
    pass


if __name__ == "__main__":
    assert two_sum_ordenado([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum_ordenado([1, 2, 3, 4, 4, 9], 8) == [3, 4]
    assert two_sum_ordenado([], 3) == [], "vacia"
    assert two_sum_ordenado([4], 4) == [], "un elemento"
    assert two_sum_ordenado([1, 2, 3], 10) == [], "sin solucion"
    assert two_sum_ordenado([-3, -1, 0, 4], 1) == [0, 3], "negativos"
    assert two_sum_ordenado([2, 2], 4) == [0, 1]
    print("OK: todos los tests pasan")
