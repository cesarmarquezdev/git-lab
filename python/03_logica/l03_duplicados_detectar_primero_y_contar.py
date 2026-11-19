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
    # tu codigo aqui
    pass


def primer_duplicado(nums):
    # tu codigo aqui
    pass


def contar_duplicados(nums):
    # tu codigo aqui
    pass


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
