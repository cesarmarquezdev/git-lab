"""i09 - Memoización: closure/dict y lru_cache (dificil)

Implementa Fibonacci memoizado de dos maneras:
1. `crear_fib_memo()` devuelve una función `fib(n)` que usa un diccionario `cache` guardado en el closure.
2. `fib_cache(n)` decorada con `functools.lru_cache(maxsize=None)`.

Convención: `fib(0)=0`, `fib(1)=1`. Sin memoización la versión recursiva es O(2^n); con ella O(n).
Ejemplo:
```
crear_fib_memo()(50)  # 12586269025
fib_cache.cache_info().hits  # > 0
```

Pistas (no mires hasta intentarlo):
Pista 1: En el closure: `cache = {}` en la función externa; la interna consulta `if n in cache` antes de calcular.
Pista 2: Guarda el resultado: `cache[n] = fib(n-1) + fib(n-2)` y devuélvelo. Casos base: n < 2.
Pista 3: Con lru_cache: `@lru_cache(maxsize=None)` encima de la función recursiva normal.

Entrevistador: ¿Qué pasa con `fib(5000)` en la versión recursiva memoizada? ¿Cómo evitarías RecursionError? ¿Por qué lru_cache no sirve con argumentos tipo lista?
"""

from functools import lru_cache


def crear_fib_memo():
    # tu código aquí
    pass


def fib_cache(n):
    # tu código aquí
    pass


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
