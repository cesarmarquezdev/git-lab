"""a17 - Permutaciones  [dificil]

Dada una lista `nums` de enteros DISTINTOS, devuelve todas sus permutaciones (el orden de las permutaciones no importa).

Ejemplos:
`permutaciones([1, 2, 3])` -> `[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`
`permutaciones([])` -> `[[]]`

En la entrevista te preguntarán: ¿Y con elementos repetidos sin generar permutaciones duplicadas? (ordenar y saltar si nums[i] == nums[i-1] y el anterior no está usado). ¿Cómo generas la k-ésima permutación sin generar todas? (sistema factorial). ¿Podrías usar un generador (yield) para no guardar n! resultados?
"""

# EXPLICACIÓN
# 1) Ingenua: itertools.permutations (válido en la vida real, pero en entrevista piden implementarlo). Otra: generar todas las listas con repetición y filtrar -> O(n^n).
# 2) Backtracking: en cada nivel probar cada elemento no usado. Hay n! hojas, y cada una cuesta O(n) copiarla. Variante: intercambiar elementos in-place (swap con el índice actual) para no necesitar `usados`. Trade-off: recursión de profundidad n con O(n) de memoria auxiliar.
# 3) Final: O(n * n!) tiempo, O(n) espacio auxiliar sin contar la salida.
#
# PREGUNTA DEL ENTREVISTADOR
# ¿Y con elementos repetidos sin generar permutaciones duplicadas? (ordenar y saltar si nums[i] == nums[i-1] y el anterior no está usado). ¿Cómo generas la k-ésima permutación sin generar todas? (sistema factorial). ¿Podrías usar un generador (yield) para no guardar n! resultados?

def permutaciones(nums):
    n = len(nums)
    res = []
    actual = []
    usados = [False] * n

    def backtrack():
        if len(actual) == n:
            res.append(actual[:])
            return
        for i in range(n):
            if usados[i]:
                continue
            usados[i] = True
            actual.append(nums[i])      # elegir
            backtrack()                 # explorar
            actual.pop()                # deshacer
            usados[i] = False

    backtrack()
    return res


if __name__ == "__main__":
    assert sorted(permutaciones([1, 2, 3])) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert permutaciones([]) == [[]], "vacío: una permutación (la vacía)"
    assert permutaciones([7]) == [[7]], "un elemento"
    assert sorted(permutaciones([0, 1])) == [[0, 1], [1, 0]]
    assert sorted(permutaciones([-1, 5])) == [[-1, 5], [5, -1]], "negativos"
    r = permutaciones([1, 2, 3, 4, 5])
    assert len(r) == 120 and len({tuple(p) for p in r}) == 120, "5! sin repetidas"
    print("OK: todos los tests pasan")
