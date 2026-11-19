"""a07 - Secuencia consecutiva más larga  [extra]

Dada una lista de enteros sin ordenar, devuelve la longitud de la secuencia de números consecutivos más larga (los números no tienen que estar juntos en la lista). Debe ser O(n): no puedes ordenar.

Ejemplos:
`secuencia_consecutiva([100, 4, 200, 1, 3, 2])` -> `4` (1,2,3,4)
`secuencia_consecutiva([0,3,7,2,5,8,4,6,0,1])` -> `9`

En la entrevista te preguntarán: El while anidado parece O(n^2), ¿por qué es O(n)? (cada elemento se visita como máximo dos veces: una en el for y otra dentro de su secuencia). ¿Y si no cabe en memoria? (ordenación externa + barrido, o particionar por rangos). ¿Y si hay que devolver la secuencia en vez de la longitud?
"""

# EXPLICACIÓN
# 1) Ingenua: para cada número buscar x+1, x+2... en la lista (O(n) cada búsqueda) -> O(n^3) peor caso.
# 2) Intermedia: ordenar y barrer -> O(n log n), O(1) extra; correcta pero no cumple O(n).
# 3) Óptima: set + empezar solo en inicios de secuencia (x-1 ausente). Cada número se recorre como mucho una vez dentro de un while (cada secuencia solo se recorre desde su inicio), así que el total es O(n) aunque haya un while anidado. Trade-off: O(n) de memoria a cambio de evitar el log.
# Final: O(n) tiempo, O(n) espacio.
#
# PREGUNTA DEL ENTREVISTADOR
# El while anidado parece O(n^2), ¿por qué es O(n)? (cada elemento se visita como máximo dos veces: una en el for y otra dentro de su secuencia). ¿Y si no cabe en memoria? (ordenación externa + barrido, o particionar por rangos). ¿Y si hay que devolver la secuencia en vez de la longitud?

def secuencia_consecutiva(nums):
    presentes = set(nums)
    mejor = 0
    for x in presentes:
        if x - 1 not in presentes:      # x es el inicio de una secuencia
            largo = 1
            while x + largo in presentes:
                largo += 1
            mejor = max(mejor, largo)
    return mejor


if __name__ == "__main__":
    assert secuencia_consecutiva([100, 4, 200, 1, 3, 2]) == 4
    assert secuencia_consecutiva([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9, "duplicados"
    assert secuencia_consecutiva([]) == 0, "vacío"
    assert secuencia_consecutiva([5]) == 1, "un elemento"
    assert secuencia_consecutiva([1, 2, 0, 1]) == 3, "duplicados en medio"
    assert secuencia_consecutiva([-1, -2, 0, 5]) == 3, "negativos cruzando el cero"
    assert secuencia_consecutiva([10, 30, 20]) == 1, "sin consecutivos"
    assert secuencia_consecutiva(list(range(1000, 0, -1))) == 1000, "grande y desordenado"
    print("OK: todos los tests pasan")
