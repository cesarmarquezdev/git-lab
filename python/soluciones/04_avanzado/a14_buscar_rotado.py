"""a14 - Búsqueda en array rotado  [extra]

Una lista ordenada ascendente y SIN duplicados fue rotada en algún punto (p. ej. `[0,1,2,4,5,6,7]` -> `[4,5,6,7,0,1,2]`). Devuelve el índice de `objetivo`, o `-1` si no está. Debe ser O(log n).

Ejemplos:
`buscar_rotado([4,5,6,7,0,1,2], 0)` -> `4`
`buscar_rotado([4,5,6,7,0,1,2], 3)` -> `-1`

En la entrevista te preguntarán: ¿Y si hay duplicados? (el peor caso degrada a O(n): cuando nums[izq] == nums[med] == nums[der] no sabes qué mitad está ordenada y debes avanzar izq y der en 1). Variante: encuentra el mínimo del array rotado.
"""

# EXPLICACIÓN
# 1) Ingenua: búsqueda lineal -> O(n); ignora que casi todo está ordenado.
# 2) Dos pasadas: hallar el pivote con binary search y luego binary search en la mitad correcta -> O(log n) pero más código. Una pasada: en cada paso, al menos una mitad está ordenada; se decide en cuál puede estar el objetivo por sus extremos y se descarta la otra mitad. Trade-off: condiciones de borde delicadas (<= vs <), por eso los tests de dos elementos.
# 3) Final: O(log n) tiempo, O(1) espacio.
#
# PREGUNTA DEL ENTREVISTADOR
# ¿Y si hay duplicados? (el peor caso degrada a O(n): cuando nums[izq] == nums[med] == nums[der] no sabes qué mitad está ordenada y debes avanzar izq y der en 1). Variante: encuentra el mínimo del array rotado.

def buscar_rotado(nums, objetivo):
    izq, der = 0, len(nums) - 1
    while izq <= der:
        med = (izq + der) // 2
        if nums[med] == objetivo:
            return med
        if nums[izq] <= nums[med]:                    # mitad izquierda ordenada
            if nums[izq] <= objetivo < nums[med]:
                der = med - 1
            else:
                izq = med + 1
        else:                                         # mitad derecha ordenada
            if nums[med] < objetivo <= nums[der]:
                izq = med + 1
            else:
                der = med - 1
    return -1


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
