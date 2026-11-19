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
    i, j = 0, len(nums) - 1
    while i < j:
        suma = nums[i] + nums[j]
        if suma == objetivo:
            return [i, j]
        if suma < objetivo:
            i += 1
        else:
            j -= 1
    return []


# Explicacion
# 1) Casos borde a preguntar: ¿esta realmente ordenado?, ¿puede haber duplicados?, ¿indices base 0 o 1?, vacio y un elemento.
# 2) Solucion ingenua: doble loop O(n^2), o hashmap O(n) tiempo y O(n) espacio (ignora que esta ordenado).
# 3) Mejora y trade-off: two pointers aprovechando el orden: cada paso descarta un candidato. Trade-off: exige entrada ordenada; si no, ordenar cuesta O(n log n) y pierdes los indices originales.
# 4) Codear hablando: narra cada paso en voz alta mientras escribes y nombra las variables con claridad.
# 5) Big-O final: tiempo O(n), espacio O(1).
# Pregunta del entrevistador: Ahora quiero tres numeros que sumen cero (3Sum): ¿como lo extiendes?

if __name__ == "__main__":
    assert two_sum_ordenado([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum_ordenado([1, 2, 3, 4, 4, 9], 8) == [3, 4]
    assert two_sum_ordenado([], 3) == [], "vacia"
    assert two_sum_ordenado([4], 4) == [], "un elemento"
    assert two_sum_ordenado([1, 2, 3], 10) == [], "sin solucion"
    assert two_sum_ordenado([-3, -1, 0, 4], 1) == [0, 3], "negativos"
    assert two_sum_ordenado([2, 2], 4) == [0, 1]
    print("OK: todos los tests pasan")
