"""Binary search a mano + primer indice

Implementa dos funciones sobre una lista ordenada ascendente:
- `busqueda_binaria(nums, objetivo)` -> un indice donde este el valor, o -1. Iterativa, sin usar `bisect` ni `.index`.
- `primer_indice(nums, objetivo)` -> el indice de la PRIMERA aparicion del valor cuando hay repetidos, o -1.
Ejemplos:
`busqueda_binaria([1, 3, 5, 7], 5)` -> 2
`primer_indice([1, 2, 2, 2, 3], 2)` -> 1

Pistas:
  1. Mantén `izq` y `der`; mira el elemento del medio `medio = (izq + der) // 2`.
  2. Si el medio es menor que el objetivo, descarta la mitad izquierda; si es mayor, la derecha.
  3. Para el primero: cuando lo encuentres guarda `medio` como respuesta y sigue buscando a la izquierda (`der = medio - 1`).
"""

def busqueda_binaria(nums, objetivo):
    # tu codigo aqui
    pass


def primer_indice(nums, objetivo):
    # tu codigo aqui
    pass


if __name__ == "__main__":
    assert busqueda_binaria([1, 3, 5, 7], 5) == 2
    assert busqueda_binaria([1, 3, 5, 7], 1) == 0, "primer elemento"
    assert busqueda_binaria([1, 3, 5, 7], 7) == 3, "ultimo elemento"
    assert busqueda_binaria([1, 3, 5, 7], 4) == -1, "no esta"
    assert busqueda_binaria([], 1) == -1, "vacia"
    assert busqueda_binaria([9], 9) == 0, "un elemento"
    assert busqueda_binaria([9], 3) == -1
    assert busqueda_binaria(list(range(0, 1000, 2)), 998) == 499
    assert primer_indice([1, 2, 2, 2, 3], 2) == 1
    assert primer_indice([2, 2, 2, 2], 2) == 0, "todos iguales"
    assert primer_indice([1, 2, 3], 3) == 2
    assert primer_indice([1, 2, 3], 5) == -1
    assert primer_indice([], 1) == -1
    assert primer_indice([1, 1, 2, 2, 2, 2], 2) == 2
    print("OK: todos los tests pasan")
