"""a05 - Top K elementos más frecuentes  [dificil]

Dada una lista de enteros `nums` y un entero `k`, devuelve los `k` elementos más frecuentes (en cualquier orden). Se garantiza que la respuesta es única (no hay empates en el corte).

Ejemplos:
`top_k_frecuentes([1,1,1,2,2,3], 2)` -> `[1, 2]`
`top_k_frecuentes([1], 1)` -> `[1]`

En la entrevista te preguntarán: ¿Y si el stream es infinito y no cabe el Counter? (algoritmos aproximados: Count-Min Sketch + heap, o Misra-Gries / Space-Saving). ¿Y si hay empates en el corte? (definir criterio de desempate, p. ej. por valor).
"""

# EXPLICACIÓN
# 1) Ingenua: contar y ordenar todos los pares por frecuencia -> O(n log n).
# 2) Mejor A: heap de tamaño k (heapq.nlargest(k, conteo, key=conteo.get)) -> O(n log k), O(n) espacio. Mejor B: bucket sort, porque la frecuencia máxima es n: se indexa por frecuencia y se recorre de mayor a menor -> O(n). Trade-off: bucket usa un array de tamaño n+1 pero evita el log; el heap es mejor cuando k es pequeño y n enorme (en streaming).
# 3) Final: O(n) tiempo y O(n) espacio con buckets; O(n log k) con heap.
#
# PREGUNTA DEL ENTREVISTADOR
# ¿Y si el stream es infinito y no cabe el Counter? (algoritmos aproximados: Count-Min Sketch + heap, o Misra-Gries / Space-Saving). ¿Y si hay empates en el corte? (definir criterio de desempate, p. ej. por valor).

from collections import Counter

def top_k_frecuentes(nums, k):
    if k <= 0 or not nums:
        return []
    conteo = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]   # buckets[f] = números con frecuencia f
    for num, f in conteo.items():
        buckets[f].append(num)
    res = []
    for f in range(len(buckets) - 1, 0, -1):
        for num in buckets[f]:
            res.append(num)
            if len(res) == k:
                return res
    return res


if __name__ == "__main__":
    assert sorted(top_k_frecuentes([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert top_k_frecuentes([1], 1) == [1], "un elemento"
    assert top_k_frecuentes([], 3) == [], "vacío"
    assert sorted(top_k_frecuentes([-1, -1, 2, 2, 2, 3], 1)) == [2], "negativos y k=1"
    assert sorted(top_k_frecuentes([4, 4, 4, 5, 5, 6], 3)) == [4, 5, 6], "k = cantidad de distintos"
    assert sorted(top_k_frecuentes([1, 2], 5)) == [1, 2], "k mayor que distintos"
    assert sorted(top_k_frecuentes([7, 7, 8, 8, 8, 9, 9, 9, 9], 2)) == [8, 9]
    assert top_k_frecuentes([1, 2, 3], 0) == [], "k = 0"
    print("OK: todos los tests pasan")
