"""Duplicados: detectar, primero y contar

Implementa tres funciones sobre una lista de enteros:
- `hay_duplicados(nums)` -> True si algun valor se repite.
- `primer_duplicado(nums)` -> el primer valor que se detecta repetido al recorrer de izquierda a derecha, o None si no hay.
- `contar_duplicados(nums)` -> dict `{valor: veces}` solo con los valores que aparecen mas de una vez.
Ejemplos:
`hay_duplicados([1, 2, 3, 1])` -> True
`primer_duplicado([2, 1, 3, 1, 2])` -> 1
`contar_duplicados([1, 2, 2, 3, 3, 3])` -> {2: 2, 3: 3}

Pistas:
  1. Un set recuerda lo ya visto en O(1).
  2. Para `primer_duplicado`: devuelve en cuanto un valor ya este en el set.
  3. Para `contar_duplicados` usa un dict de conteos y filtra los que tengan > 1.
"""

def hay_duplicados(nums):
    return len(set(nums)) != len(nums)


def primer_duplicado(nums):
    vistos = set()
    for n in nums:
        if n in vistos:
            return n
        vistos.add(n)
    return None


def contar_duplicados(nums):
    conteo = {}
    for n in nums:
        conteo[n] = conteo.get(n, 0) + 1
    return {k: v for k, v in conteo.items() if v > 1}


# Explicacion
# 1) Casos borde a preguntar: lista vacia, un elemento, ¿el input se puede modificar?, ¿valores negativos?, ¿que devolver si no hay duplicado?
# 2) Solucion ingenua: doble loop comparando cada par: O(n^2) tiempo, O(1) espacio. Tambien ordenar y comparar vecinos: O(n log n).
# 3) Mejora y trade-off: set de vistos (o dict de conteos): una sola pasada. Trade-off: gastas O(n) de memoria para bajar el tiempo de O(n^2) a O(n).
# 4) Codear hablando: narra cada paso en voz alta mientras escribes y nombra las variables con claridad.
# 5) Big-O final: tiempo O(n), espacio O(n). Si la memoria importa y se puede ordenar, O(n log n) tiempo y O(1) espacio extra.
# Pregunta del entrevistador: ¿Y si no puedes usar memoria extra?

if __name__ == "__main__":
    assert hay_duplicados([1, 2, 3, 1]) is True
    assert hay_duplicados([1, 2, 3]) is False
    assert hay_duplicados([]) is False, "vacia"
    assert hay_duplicados([5]) is False, "un elemento"
    assert primer_duplicado([2, 1, 3, 1, 2]) == 1
    assert primer_duplicado([1, 2, 3]) is None
    assert primer_duplicado([]) is None
    assert contar_duplicados([1, 2, 2, 3, 3, 3]) == {2: 2, 3: 3}
    assert contar_duplicados([1, 2, 3]) == {}
    assert contar_duplicados([]) == {}
    print("OK: todos los tests pasan")
