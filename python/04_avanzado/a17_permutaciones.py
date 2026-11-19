"""a17 - Permutaciones  [dificil]

Dada una lista `nums` de enteros DISTINTOS, devuelve todas sus permutaciones (el orden de las permutaciones no importa).

Ejemplos:
`permutaciones([1, 2, 3])` -> `[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`
`permutaciones([])` -> `[[]]`

En la entrevista te preguntarán: ¿Y con elementos repetidos sin generar permutaciones duplicadas? (ordenar y saltar si nums[i] == nums[i-1] y el anterior no está usado). ¿Cómo generas la k-ésima permutación sin generar todas? (sistema factorial). ¿Podrías usar un generador (yield) para no guardar n! resultados?
"""

# Pista 1: Construye la permutación posición por posición: en cada paso, ¿qué elementos aún no usaste?
# Pista 2: Mantén una lista `actual` y un set/lista de booleanos `usados`. Caso base: len(actual) == n -> guarda copia.
# Pista 3: Elegir (append + marcar usado) -> recursión -> deshacer (pop + desmarcar).

def permutaciones(nums):
    # tu código aquí
    pass


if __name__ == "__main__":
    assert sorted(permutaciones([1, 2, 3])) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert permutaciones([]) == [[]], "vacío: una permutación (la vacía)"
    assert permutaciones([7]) == [[7]], "un elemento"
    assert sorted(permutaciones([0, 1])) == [[0, 1], [1, 0]]
    assert sorted(permutaciones([-1, 5])) == [[-1, 5], [5, -1]], "negativos"
    r = permutaciones([1, 2, 3, 4, 5])
    assert len(r) == 120 and len({tuple(p) for p in r}) == 120, "5! sin repetidas"
    print("OK: todos los tests pasan")
