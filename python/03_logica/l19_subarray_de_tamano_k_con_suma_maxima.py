"""Subarray de tamano k con suma maxima

Escribe `suma_maxima_k(nums, k)` que devuelva la mayor suma de k elementos consecutivos de la lista. Si `k` es menor que 1 o mayor que el largo de la lista, devuelve None. Usa una ventana deslizante (no recalcules la suma completa en cada paso).
Ejemplos:
`suma_maxima_k([2, 1, 5, 1, 3, 2], 3)` -> 9
`suma_maxima_k([4, 2], 2)` -> 6

Pistas:
  1. La fuerza bruta suma k elementos en cada posicion: O(n*k).
  2. Calcula la suma de la primera ventana y luego desliza: suma el que entra y resta el que sale.
  3. `suma += nums[i] - nums[i - k]` y actualiza el maximo.
"""

def suma_maxima_k(nums, k):
    # tu codigo aqui
    pass


if __name__ == "__main__":
    assert suma_maxima_k([2, 1, 5, 1, 3, 2], 3) == 9
    assert suma_maxima_k([4, 2], 2) == 6, "k igual al largo"
    assert suma_maxima_k([], 1) is None, "vacia"
    assert suma_maxima_k([7], 1) == 7, "un elemento"
    assert suma_maxima_k([1, 2], 3) is None, "k mayor que el largo"
    assert suma_maxima_k([1, 2, 3], 0) is None, "k = 0"
    assert suma_maxima_k([-1, -2, -3, -4], 2) == -3, "negativos"
    assert suma_maxima_k([1, 9, -1, 3], 1) == 9
    print("OK: todos los tests pasan")
