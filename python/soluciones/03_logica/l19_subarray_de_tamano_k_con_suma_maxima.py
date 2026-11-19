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
    if k < 1 or k > len(nums):
        return None
    suma = sum(nums[:k])
    mejor = suma
    for i in range(k, len(nums)):
        suma += nums[i] - nums[i - k]
        mejor = max(mejor, suma)
    return mejor


# Explicacion
# 1) Casos borde a preguntar: k = 0, k mayor que el largo, lista vacia, negativos (no inicializar el maximo en 0), ¿ventana contigua?
# 2) Solucion ingenua: para cada inicio sumar k elementos: O(n*k) tiempo.
# 3) Mejora y trade-off: sliding window: la ventana se desplaza sumando el elemento nuevo y restando el que sale. Trade-off: ninguno, solo requiere ver que las ventanas consecutivas comparten k-1 elementos.
# 4) Codear hablando: narra cada paso en voz alta mientras escribes y nombra las variables con claridad.
# 5) Big-O final: tiempo O(n), espacio O(1).
# Pregunta del entrevistador: ¿Y si la ventana fuera de tamano variable (suma >= S con la menor longitud)?

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
