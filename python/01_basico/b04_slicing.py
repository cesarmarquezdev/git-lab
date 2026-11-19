r"""b04 - Slicing de listas (facil)

Escribe `rebanadas(lista)` que devuelva una tupla de 3 elementos:
1. los elementos de las posiciones 1 a 3 (`[1:4]`),
2. la lista invertida,
3. los elementos de posicion par (0, 2, 4...).

Ejemplo: `rebanadas([10, 20, 30, 40, 50])` -> `([20, 30, 40], [50, 40, 30, 20, 10], [10, 30, 50])`

No debe modificar la lista original. Casos borde: lista vacia -> `([], [], [])`; con 2 elementos el primer trozo tiene solo el elemento 1 (el slicing no lanza IndexError).
"""

# Pista 1: El slicing nunca lanza IndexError: se recorta al tamaño de la lista.
# Pista 2: `lista[inicio:fin:paso]`; paso negativo recorre al reves.
# Pista 3: `return (lista[1:4], lista[::-1], lista[::2])`

def rebanadas(lista):
    # tu código aquí
    pass

if __name__ == "__main__":
    assert rebanadas([10, 20, 30, 40, 50]) == ([20, 30, 40], [50, 40, 30, 20, 10], [10, 30, 50])
    assert rebanadas([]) == ([], [], []), "vacia"
    assert rebanadas([7]) == ([], [7], [7]), "un elemento"
    assert rebanadas([1, 2]) == ([2], [2, 1], [1]), "dos elementos"
    orig = [1, 2, 3]
    rebanadas(orig)
    assert orig == [1, 2, 3], "no debe mutar"
    print("OK: todos los tests pasan")
