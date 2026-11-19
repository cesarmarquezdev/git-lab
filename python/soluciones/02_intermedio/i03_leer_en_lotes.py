"""i03 - Generador leer_en_lotes (SOLUCIÓN)
"""

from itertools import islice


def leer_en_lotes(iterable, n):
    if n < 1:
        raise ValueError("n debe ser >= 1")
    it = iter(iterable)
    while True:
        lote = list(islice(it, n))
        if not lote:
            return
        yield lote

# Explicación:
# El generador guarda solo un lote en memoria: espacio O(n) en vez de O(total). `iter()` es clave: con una lista, `islice` sobre la lista misma volvería a empezar; con un iterador sigue donde se quedó. Tiempo O(total). Nota: como contiene `yield`, el `ValueError` se lanza al primer `next()`, no al llamar a la función. Alternativa en 3.12: `itertools.batched`.
# Entrevistador: ¿Cuándo se lanza el ValueError exactamente, al crear el generador o al iterarlo? ¿Cómo lo harías saltar de inmediato?


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
