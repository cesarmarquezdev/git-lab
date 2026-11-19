"""Two Sum

Escribe `two_sum(nums, objetivo)` que devuelva los indices `[i, j]` (con i < j) de dos numeros distintos de la lista cuya suma sea `objetivo`. Si no existe, devuelve `[]`. Asume que a lo sumo hay una solucion y no puedes usar el mismo elemento dos veces.
Ejemplos:
`two_sum([2, 7, 11, 15], 9)` -> [0, 1]
`two_sum([3, 2, 4], 6)` -> [1, 2]
`two_sum([3, 3], 6)` -> [0, 1]

Pistas:
  1. La fuerza bruta prueba todos los pares: ¿cuanto cuesta?
  2. Para cada `n`, necesitas saber si `objetivo - n` ya paso por aqui.
  3. Guarda `{valor: indice}` y consulta el complemento antes de insertar el actual.
"""

def two_sum(nums, objetivo):
    # tu codigo aqui
    pass


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1], "valores repetidos"
    assert two_sum([], 5) == [], "vacia"
    assert two_sum([5], 5) == [], "un elemento"
    assert two_sum([1, 2, 3], 100) == [], "sin solucion"
    assert two_sum([-1, -2, -3, -4], -6) == [1, 3], "negativos"
    assert two_sum([3, 2, 4], 6) != [0, 0], "no reutilizar el mismo elemento"
    print("OK: todos los tests pasan")
