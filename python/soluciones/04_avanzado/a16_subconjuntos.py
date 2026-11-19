"""a16 - Subconjuntos (subsets)  [dificil]

Dada una lista `nums` de enteros DISTINTOS, devuelve todos los subconjuntos posibles (el conjunto potencia), incluido el vacío. El orden no importa.

Ejemplos:
`subconjuntos([1, 2])` -> `[[], [1], [2], [1, 2]]`
`subconjuntos([])` -> `[[]]`

En la entrevista te preguntarán: ¿Y si hay elementos duplicados y no quieres subconjuntos repetidos? (ordenar y saltar duplicados en el mismo nivel). ¿Y si n es 30 y no cabe todo en memoria? (generador con yield, o bitmask del 0 al 2^n-1 generando uno a uno). ¿Por qué no puedes bajar de O(2^n)?
"""

# EXPLICACIÓN
# 1) Idea ingenua/iterativa: empezar con [[]] y, por cada elemento, duplicar todos los subconjuntos existentes añadiéndoles ese elemento: res += [s + [x] for s in res]. Es correcta y corta.
# 2) Backtracking: árbol de decisiones incluir/no incluir; el patrón elegir -> explorar -> deshacer es la plantilla de permutaciones, combinaciones y N-reinas. Trade-off: usa pila de recursión O(n) pero reutiliza una sola lista de trabajo (se copia solo al guardar).
# 3) Final: O(n * 2^n) tiempo (2^n subconjuntos, copiar cada uno cuesta hasta n), O(n) espacio auxiliar sin contar la salida. No se puede hacer mejor porque la salida ya mide eso.
#
# PREGUNTA DEL ENTREVISTADOR
# ¿Y si hay elementos duplicados y no quieres subconjuntos repetidos? (ordenar y saltar duplicados en el mismo nivel). ¿Y si n es 30 y no cabe todo en memoria? (generador con yield, o bitmask del 0 al 2^n-1 generando uno a uno). ¿Por qué no puedes bajar de O(2^n)?

def subconjuntos(nums):
    res = []
    actual = []

    def backtrack(i):
        if i == len(nums):
            res.append(actual[:])        # copia, no la referencia
            return
        actual.append(nums[i])           # decisión 1: incluir
        backtrack(i + 1)
        actual.pop()                     # deshacer
        backtrack(i + 1)                 # decisión 2: no incluir

    backtrack(0)
    return res


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
