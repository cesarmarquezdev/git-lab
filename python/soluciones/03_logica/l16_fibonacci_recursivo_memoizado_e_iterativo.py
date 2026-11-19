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
    if n < 2:
        return n
    return fib_recursivo(n - 1) + fib_recursivo(n - 2)


def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n < 2:
        return n
    if n not in memo:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


def fib_iterativo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# Explicacion
# 1) Casos borde a preguntar: ¿n negativo?, n = 0 y 1 como casos base, ¿que tan grande puede ser n?, limite de recursion de Python.
# 2) Solucion ingenua: recursion directa: cada llamada genera dos mas, el arbol crece como 2^n. Tiempo O(2^n), espacio O(n) de pila.
# 3) Mejora y trade-off: memoizar evita recalcular subproblemas (programacion dinamica top-down): O(n) tiempo y O(n) espacio. Iterativo bottom-up con dos variables: O(n) tiempo y O(1) espacio. Trade-off: el memo es mas legible pero consume pila y memoria.
# 4) Codear hablando: narra cada paso en voz alta mientras escribes y nombra las variables con claridad.
# 5) Big-O final: recursivo O(2^n) tiempo / O(n) espacio; memo O(n) / O(n); iterativo O(n) / O(1). Ojo: fib_memo(300) con recursion se acerca al limite de recursion de Python (1000).
# Pregunta del entrevistador: ¿Por que la version ingenua es exponencial? Dibuja el arbol de llamadas de fib(5). ¿Se puede en O(log n)?

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
