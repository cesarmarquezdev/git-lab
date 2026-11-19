r"""b06 - append vs extend, insert, pop y remove (facil)

Implementa estas funciones que MODIFICAN la lista recibida (in-place) y no devuelven nada:

1. `agregar_uno(lista, elem)`: añade `elem` como UN solo elemento al final (aunque sea una lista).
2. `agregar_varios(lista, otros)`: añade cada elemento de `otros` al final.
3. `rotar_izquierda(lista)`: saca el primer elemento y lo pone al final. Con lista vacia no hace nada.
4. `quitar_primero(lista, x)`: quita la primera aparicion de `x`; si no esta, no hace nada (sin lanzar error).

Ejemplos:
`l=[1]; agregar_uno(l, [2, 3])` -> `l == [1, [2, 3]]`
`l=[1]; agregar_varios(l, [2, 3])` -> `l == [1, 2, 3]`
`l=[1, 2, 3]; rotar_izquierda(l)` -> `l == [2, 3, 1]`
"""

# Pista 1: append añade un objeto; extend itera y añade cada elemento.
# Pista 2: `pop(0)` quita y devuelve el primero. Ojo con lista vacia (`if lista:`).
# Pista 3: `remove` lanza ValueError si no existe: compruebalo antes con `in` o usa try/except.

def agregar_uno(lista, elem):
    pass


def agregar_varios(lista, otros):
    pass


def rotar_izquierda(lista):
    pass


def quitar_primero(lista, x):
    pass

if __name__ == "__main__":
    l = [1]
    agregar_uno(l, [2, 3])
    assert l == [1, [2, 3]], "append añade un solo objeto"
    l = [1]
    agregar_varios(l, [2, 3])
    assert l == [1, 2, 3], "extend añade cada elemento"
    l = [1]
    agregar_varios(l, [])
    assert l == [1], "extend con vacio"
    l = [1, 2, 3]
    rotar_izquierda(l)
    assert l == [2, 3, 1]
    l = []
    rotar_izquierda(l)
    assert l == [], "rotar vacia"
    l = [5]
    rotar_izquierda(l)
    assert l == [5], "rotar un elemento"
    l = [1, 2, 1]
    quitar_primero(l, 1)
    assert l == [2, 1], "solo la primera aparicion"
    quitar_primero(l, 99)
    assert l == [2, 1], "no existe: sin error"
    print("OK: todos los tests pasan")
