"""a05 - Top K elementos más frecuentes  [dificil]

Dada una lista de enteros `nums` y un entero `k`, devuelve los `k` elementos más frecuentes (en cualquier orden). Se garantiza que la respuesta es única (no hay empates en el corte).

Ejemplos:
`top_k_frecuentes([1,1,1,2,2,3], 2)` -> `[1, 2]`
`top_k_frecuentes([1], 1)` -> `[1]`

En la entrevista te preguntarán: ¿Y si el stream es infinito y no cabe el Counter? (algoritmos aproximados: Count-Min Sketch + heap, o Misra-Gries / Space-Saving). ¿Y si hay empates en el corte? (definir criterio de desempate, p. ej. por valor).
"""

# Pista 1: Primero cuenta cuántas veces aparece cada número (Counter).
# Pista 2: Ordenar todo es O(n log n). Piensa en un heap de tamaño k, o en 'buckets' indexados por frecuencia.
# Pista 3: Bucket sort: buckets[f] = lista de números con frecuencia f (f va de 1 a n). Recorre de mayor a menor frecuencia hasta juntar k.

def top_k_frecuentes(nums, k):
    # tu código aquí
    pass


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
