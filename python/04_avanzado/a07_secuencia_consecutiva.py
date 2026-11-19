"""a07 - Secuencia consecutiva más larga  [extra]

Dada una lista de enteros sin ordenar, devuelve la longitud de la secuencia de números consecutivos más larga (los números no tienen que estar juntos en la lista). Debe ser O(n): no puedes ordenar.

Ejemplos:
`secuencia_consecutiva([100, 4, 200, 1, 3, 2])` -> `4` (1,2,3,4)
`secuencia_consecutiva([0,3,7,2,5,8,4,6,0,1])` -> `9`

En la entrevista te preguntarán: El while anidado parece O(n^2), ¿por qué es O(n)? (cada elemento se visita como máximo dos veces: una en el for y otra dentro de su secuencia). ¿Y si no cabe en memoria? (ordenación externa + barrido, o particionar por rangos). ¿Y si hay que devolver la secuencia en vez de la longitud?
"""

# Pista 1: Meter todo en un set da búsquedas O(1). ¿Qué pregunta puedes hacerle a ese set sobre cada número?
# Pista 2: Solo tiene sentido empezar a contar desde el INICIO de una secuencia: aquel número x tal que x-1 NO está en el set.
# Pista 3: Para cada x con x-1 ausente, avanza mientras x+1, x+2... estén en el set y lleva el máximo.

def secuencia_consecutiva(nums):
    # tu código aquí
    pass


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
