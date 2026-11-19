"""i09 - Memoización: closure/dict y lru_cache (SOLUCIÓN)
"""

from functools import lru_cache


def crear_fib_memo():
    cache = {}

    def fib(n):
        if n < 2:
            return n
        if n not in cache:
            cache[n] = fib(n - 1) + fib(n - 2)
        return cache[n]

    return fib


@lru_cache(maxsize=None)
def fib_cache(n):
    if n < 2:
        return n
    return fib_cache(n - 1) + fib_cache(n - 2)

# Explicación:
# Sin caché, `fib(n)` recalcula los mismos subproblemas: O(2^n). Con diccionario cada n se calcula una vez: O(n) tiempo y O(n) espacio (más la pila de recursión, O(n)). `lru_cache` hace lo mismo como decorador y añade `cache_info()`/`cache_clear()`; requiere argumentos hasheables. `maxsize=None` = sin límite (desde 3.9 también existe `functools.cache`). Versión iterativa: O(n) tiempo, O(1) espacio y sin límite de recursión.
# Entrevistador: ¿Qué pasa con `fib(5000)` en la versión recursiva memoizada? ¿Cómo evitarías RecursionError? ¿Por qué lru_cache no sirve con argumentos tipo lista?


if __name__ == "__main__":
    fib = crear_fib_memo()
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(10) == 55
    assert fib(50) == 12586269025, "debe ser rápido (memoizado)"
    fib2 = crear_fib_memo()
    assert fib2(5) == 5, "cada closure tiene su propia caché"

    assert fib_cache(0) == 0
    assert fib_cache(1) == 1
    assert fib_cache(80) == 23416728348467685
    info = fib_cache.cache_info()
    assert info.hits > 0, "lru_cache debe haber reutilizado resultados"
    assert info.misses == 81, "cada n distinto se calcula una sola vez"
    fib_cache.cache_clear()
    assert fib_cache.cache_info().currsize == 0
    print("OK: todos los tests pasan")
