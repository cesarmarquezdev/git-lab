"""i04 - Fibonacci infinito con generador (SOLUCIÓN)
"""

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Explicación:
# El estado (a, b) vive en el frame del generador, suspendido entre cada `yield`. Cada elemento cuesta O(1) sumas (en bignums O(dígitos)); espacio O(1) frente a O(n) de construir una lista. Un generador infinito solo se puede consumir con `islice`, `next` o cortando el bucle: `list(fibonacci())` nunca terminaría.
# Entrevistador: ¿Qué pasa si hago `for x in fibonacci(): print(x)` sin `break`? ¿Y cómo obtendrías el n-ésimo con islice sin guardar todos?


if __name__ == "__main__":
    from itertools import islice

    assert list(islice(fibonacci(), 0)) == [], "cero elementos"
    assert list(islice(fibonacci(), 1)) == [0], "un elemento"
    assert list(islice(fibonacci(), 10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    g1, g2 = fibonacci(), fibonacci()
    next(g1); next(g1); next(g1)
    assert next(g2) == 0, "generadores independientes"
    assert next(g1) == 2
    assert list(islice(fibonacci(), 100))[-1] == 218922995834555169026
    print("OK: todos los tests pasan")
