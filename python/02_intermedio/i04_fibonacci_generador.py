"""i04 - Fibonacci infinito con generador (media)

Escribe el generador `fibonacci()` sin argumentos que produzca indefinidamente la sucesión 0, 1, 1, 2, 3, 5, 8... Dos generadores creados por separado deben ser independientes.

Ejemplo:
```
from itertools import islice
list(islice(fibonacci(), 7))  # [0, 1, 1, 2, 3, 5, 8]
```

Pistas (no mires hasta intentarlo):
Pista 1: Necesitas dos variables, `a` y `b`, y un `while True`.
Pista 2: En cada vuelta `yield a` y luego avanza el par.
Pista 3: `a, b = b, a + b` hace la actualización simultánea.

Entrevistador: ¿Qué pasa si hago `for x in fibonacci(): print(x)` sin `break`? ¿Y cómo obtendrías el n-ésimo con islice sin guardar todos?
"""

def fibonacci():
    # tu código aquí
    pass


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
