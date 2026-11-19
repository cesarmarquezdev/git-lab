"""a16 - Subconjuntos (subsets)  [dificil]

Dada una lista `nums` de enteros DISTINTOS, devuelve todos los subconjuntos posibles (el conjunto potencia), incluido el vacío. El orden no importa.

Ejemplos:
`subconjuntos([1, 2])` -> `[[], [1], [2], [1, 2]]`
`subconjuntos([])` -> `[[]]`

En la entrevista te preguntarán: ¿Y si hay elementos duplicados y no quieres subconjuntos repetidos? (ordenar y saltar duplicados en el mismo nivel). ¿Y si n es 30 y no cabe todo en memoria? (generador con yield, o bitmask del 0 al 2^n-1 generando uno a uno). ¿Por qué no puedes bajar de O(2^n)?
"""

# Pista 1: Para cada elemento hay dos decisiones: lo incluyes o no. Eso da 2^n subconjuntos.
# Pista 2: Backtracking: función auxiliar(i, actual). Caso base: i == n -> guarda una COPIA de actual.
# Pista 3: Incluir: actual.append(nums[i]); auxiliar(i+1); actual.pop() (deshacer). No incluir: auxiliar(i+1). Cuidado: guarda actual[:] y no actual.

def subconjuntos(nums):
    # tu código aquí
    pass


if __name__ == "__main__":
    def norm(r):
        return sorted(sorted(s) for s in r)

    assert norm(subconjuntos([1, 2, 3])) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    assert subconjuntos([]) == [[]], "vacío: solo el conjunto vacío"
    assert norm(subconjuntos([0])) == [[], [0]], "un elemento"
    assert len(subconjuntos(list(range(10)))) == 1024, "2^10"
    assert norm(subconjuntos([-1, 1])) == [[], [-1], [-1, 1], [1]], "negativos"
    r = subconjuntos([1, 2])
    assert all(isinstance(s, list) for s in r) and len({tuple(s) for s in r}) == 4, "copias independientes"
    print("OK: todos los tests pasan")
