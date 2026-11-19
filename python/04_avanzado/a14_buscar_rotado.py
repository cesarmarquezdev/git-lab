"""a14 - Búsqueda en array rotado  [extra]

Una lista ordenada ascendente y SIN duplicados fue rotada en algún punto (p. ej. `[0,1,2,4,5,6,7]` -> `[4,5,6,7,0,1,2]`). Devuelve el índice de `objetivo`, o `-1` si no está. Debe ser O(log n).

Ejemplos:
`buscar_rotado([4,5,6,7,0,1,2], 0)` -> `4`
`buscar_rotado([4,5,6,7,0,1,2], 3)` -> `-1`

En la entrevista te preguntarán: ¿Y si hay duplicados? (el peor caso degrada a O(n): cuando nums[izq] == nums[med] == nums[der] no sabes qué mitad está ordenada y debes avanzar izq y der en 1). Variante: encuentra el mínimo del array rotado.
"""

# Pista 1: Haz binary search normal, pero en cada paso una de las dos mitades SIEMPRE está ordenada.
# Pista 2: Compara nums[izq] <= nums[med] para saber si la mitad izquierda es la ordenada.
# Pista 3: Si el objetivo cae dentro del rango de la mitad ordenada, quédate con ella; si no, con la otra.

def buscar_rotado(nums, objetivo):
    # tu código aquí
    pass


if __name__ == "__main__":
    assert buscar_rotado([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert buscar_rotado([4, 5, 6, 7, 0, 1, 2], 3) == -1, "no está"
    assert buscar_rotado([], 1) == -1, "vacío"
    assert buscar_rotado([1], 1) == 0, "un elemento, está"
    assert buscar_rotado([1], 0) == -1, "un elemento, no está"
    assert buscar_rotado([3, 1], 1) == 1, "dos elementos rotados"
    assert buscar_rotado([1, 3], 3) == 1, "sin rotar, dos elementos"
    assert buscar_rotado([1, 2, 3, 4, 5], 4) == 3, "rotación 0"
    assert buscar_rotado([5, 1, 2, 3, 4], 5) == 0, "el pivote al inicio"
    assert buscar_rotado([-3, -1, 0, 2, -9, -7], -9) == 4, "negativos"
    for i, v in enumerate([6, 7, 8, 1, 2, 3, 4, 5]):
        assert buscar_rotado([6, 7, 8, 1, 2, 3, 4, 5], v) == i
    print("OK: todos los tests pasan")
