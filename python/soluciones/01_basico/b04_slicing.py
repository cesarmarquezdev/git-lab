r"""b04 - Slicing de listas (facil)

Escribe `rebanadas(lista)` que devuelva una tupla de 3 elementos:
1. los elementos de las posiciones 1 a 3 (`[1:4]`),
2. la lista invertida,
3. los elementos de posicion par (0, 2, 4...).

Ejemplo: `rebanadas([10, 20, 30, 40, 50])` -> `([20, 30, 40], [50, 40, 30, 20, 10], [10, 30, 50])`

No debe modificar la lista original. Casos borde: lista vacia -> `([], [], [])`; con 2 elementos el primer trozo tiene solo el elemento 1 (el slicing no lanza IndexError).
"""

def rebanadas(lista):
    return (lista[1:4], lista[::-1], lista[::2])

# Explicacion: El slice crea una copia superficial, por eso no se muta el original. Cada slice es O(k) en tiempo y espacio. El fin es exclusivo: [1:4] da indices 1,2,3.
# Pregunta del entrevistador: ¿Que devuelve `lista[::-1]` vs `lista.reverse()` y `reversed(lista)`? (copia nueva / in-place devuelve None / iterador).

if __name__ == "__main__":
    assert rebanadas([10, 20, 30, 40, 50]) == ([20, 30, 40], [50, 40, 30, 20, 10], [10, 30, 50])
    assert rebanadas([]) == ([], [], []), "vacia"
    assert rebanadas([7]) == ([], [7], [7]), "un elemento"
    assert rebanadas([1, 2]) == ([2], [2, 1], [1]), "dos elementos"
    orig = [1, 2, 3]
    rebanadas(orig)
    assert orig == [1, 2, 3], "no debe mutar"
    print("OK: todos los tests pasan")
