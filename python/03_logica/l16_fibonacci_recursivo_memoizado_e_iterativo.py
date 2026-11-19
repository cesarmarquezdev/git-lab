"""Fibonacci: recursivo, memoizado e iterativo

Implementa tres funciones que calculen el n-esimo Fibonacci (fib(0)=0, fib(1)=1, fib(n)=fib(n-1)+fib(n-2)):
- `fib_recursivo(n)`: recursion ingenua.
- `fib_memo(n)`: recursion con memoizacion (guarda resultados ya calculados).
- `fib_iterativo(n)`: con un loop y dos variables.
Ejemplos: `fib_recursivo(6)` -> 8, `fib_memo(50)` -> 12586269025, `fib_iterativo(0)` -> 0.

Pistas:
  1. Define bien los casos base: n = 0 y n = 1.
  2. La version ingenua repite calculos; guarda cada fib(k) en un dict la primera vez.
  3. Iterativo: `a, b = 0, 1` y avanza `a, b = b, a + b` n veces.
"""

def fib_recursivo(n):
    # tu codigo aqui
    pass


def fib_memo(n):
    # tu codigo aqui
    pass


def fib_iterativo(n):
    # tu codigo aqui
    pass


if __name__ == "__main__":
    for n, esperado in [(0, 0), (1, 1), (2, 1), (6, 8), (10, 55), (20, 6765)]:
        assert fib_recursivo(n) == esperado, f"fib_recursivo({n})"
        assert fib_memo(n) == esperado, f"fib_memo({n})"
        assert fib_iterativo(n) == esperado, f"fib_iterativo({n})"
    assert fib_memo(50) == 12586269025
    assert fib_iterativo(50) == 12586269025
    assert fib_memo(300) == fib_iterativo(300), "memo debe ser rapido y correcto en n grande"
    assert fib_iterativo(90) == 2880067194370816120
    print("OK: todos los tests pasan")
