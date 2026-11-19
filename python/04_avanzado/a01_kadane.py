"""a01 - Máximo subarray (Kadane)  [extra]

Dada una lista de enteros `nums` (pueden ser negativos), devuelve la mayor suma posible de un subarray contiguo no vacío.
Si la lista está vacía devuelve `0`.

Ejemplos:
`max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])` -> `6` (el subarray `[4, -1, 2, 1]`)
`max_subarray([-3, -1, -2])` -> `-1`

En la entrevista te preguntarán: Ahora devuélveme también los índices (inicio, fin) del subarray. ¿Y si los datos llegan en streaming y no caben en memoria? (Kadane ya es una pasada con O(1): solo guardas inicio_actual, y actualizas inicio/fin cuando mejoras el máximo; cuando 'actual' es peor que empezar de nuevo, inicio_actual = i.) Variante: ¿y el máximo subarray circular?
"""

# Pista 1: Pregunta clave: en cada posición, ¿conviene extender el subarray anterior o empezar uno nuevo aquí?
# Pista 2: Mantén dos variables: la mejor suma que TERMINA en el elemento actual y la mejor global.
# Pista 3: actual = max(x, actual + x); mejor = max(mejor, actual). Inicializa con nums[0], no con 0 (por los negativos).

def max_subarray(nums):
    # tu código aquí
    pass


if __name__ == "__main__":
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray([1]) == 1, "un elemento"
    assert max_subarray([-5]) == -5, "un solo negativo"
    assert max_subarray([-3, -1, -2]) == -1, "todos negativos: no devolver 0"
    assert max_subarray([5, 4, -1, 7, 8]) == 23, "todo el array"
    assert max_subarray([]) == 0, "vacío"
    assert max_subarray([0, 0, 0]) == 0
    assert max_subarray([-1, 2, -1, 2, -1]) == 3
    print("OK: todos los tests pasan")
