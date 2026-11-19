"""i03 - Generador leer_en_lotes (media)

Escribe el generador `leer_en_lotes(iterable, n)` que produzca listas de hasta `n` elementos del iterable. El último lote puede ser más corto. Debe ser **perezoso** (no convertir todo a lista) y funcionar con iterables infinitos. Si `n < 1` lanza `ValueError`.

Ejemplo:
```
list(leer_en_lotes([1,2,3,4,5], 2))  # [[1,2],[3,4],[5]]
list(leer_en_lotes([], 3))  # []
```

Pistas (no mires hasta intentarlo):
Pista 1: Convierte el iterable en iterador con `iter(...)` para ir consumiéndolo.
Pista 2: `itertools.islice(it, n)` toma hasta n elementos del iterador.
Pista 3: Bucle infinito: `lote = list(islice(it, n)); if not lote: return; yield lote`.

Entrevistador: ¿Cuándo se lanza el ValueError exactamente, al crear el generador o al iterarlo? ¿Cómo lo harías saltar de inmediato?
"""

from itertools import islice


def leer_en_lotes(iterable, n):
    # tu código aquí
    pass


if __name__ == "__main__":
    import types
    from itertools import count, islice

    assert list(leer_en_lotes([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]
    assert list(leer_en_lotes([], 3)) == [], "vacío"
    assert list(leer_en_lotes([7], 3)) == [[7]], "un elemento"
    assert list(leer_en_lotes("abcd", 2)) == [["a", "b"], ["c", "d"]], "múltiplo exacto"
    assert list(leer_en_lotes(range(3), 1)) == [[0], [1], [2]]
    assert isinstance(leer_en_lotes([1], 1), types.GeneratorType), "debe ser generador"
    primeros = list(islice(leer_en_lotes(count(), 3), 2))
    assert primeros == [[0, 1, 2], [3, 4, 5]], "debe funcionar con iterables infinitos"
    try:
        list(leer_en_lotes([1, 2], 0))
        assert False, "n=0 debe lanzar ValueError"
    except ValueError:
        pass
    print("OK: todos los tests pasan")
