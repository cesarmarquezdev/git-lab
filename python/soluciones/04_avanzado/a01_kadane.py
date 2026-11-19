"""a01 - Máximo subarray (Kadane)  [extra]

Dada una lista de enteros `nums` (pueden ser negativos), devuelve la mayor suma posible de un subarray contiguo no vacío.
Si la lista está vacía devuelve `0`.

Ejemplos:
`max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])` -> `6` (el subarray `[4, -1, 2, 1]`)
`max_subarray([-3, -1, -2])` -> `-1`

En la entrevista te preguntarán: Ahora devuélveme también los índices (inicio, fin) del subarray. ¿Y si los datos llegan en streaming y no caben en memoria? (Kadane ya es una pasada con O(1): solo guardas inicio_actual, y actualizas inicio/fin cuando mejoras el máximo; cuando 'actual' es peor que empezar de nuevo, inicio_actual = i.) Variante: ¿y el máximo subarray circular?
"""

# EXPLICACIÓN
# 1) Ingenua: probar todos los pares (i, j) y sumar -> O(n^3); con sumas prefijas O(n^2) tiempo, O(1) espacio.
# 2) Óptima (Kadane, programación dinámica): la mejor suma que termina en i es max(nums[i], mejor_que_termina_en_i-1 + nums[i]). Si lo anterior es negativo, solo estorba y se descarta. Solo hace falta recordar un número, no una tabla: trade-off, ganamos espacio sin perder nada.
# 3) Final: O(n) tiempo, O(1) espacio, una sola pasada (sirve en streaming).
# Trampa típica: inicializar con 0 rompe el caso de todos negativos.
#
# PREGUNTA DEL ENTREVISTADOR
# Ahora devuélveme también los índices (inicio, fin) del subarray. ¿Y si los datos llegan en streaming y no caben en memoria? (Kadane ya es una pasada con O(1): solo guardas inicio_actual, y actualizas inicio/fin cuando mejoras el máximo; cuando 'actual' es peor que empezar de nuevo, inicio_actual = i.) Variante: ¿y el máximo subarray circular?

def max_subarray(nums):
    if not nums:
        return 0
    actual = mejor = nums[0]
    for x in nums[1:]:
        actual = max(x, actual + x)   # extender o empezar de nuevo
        mejor = max(mejor, actual)
    return mejor


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
