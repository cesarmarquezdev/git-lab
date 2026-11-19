"""i02 - Decorador con argumentos: reintentar(n) (SOLUCIÓN)
"""

import functools


def reintentar(n):
    def decorador(func):
        @functools.wraps(func)
        def envoltura(*args, **kwargs):
            ultima = None
            for _ in range(n):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    ultima = e
            raise ultima

        return envoltura

    return decorador

# Explicación:
# `@reintentar(3)` primero evalúa `reintentar(3)` (devuelve el decorador) y luego aplica ese decorador a la función: por eso hay 3 niveles de funciones anidadas. Capturamos `Exception` (no `BaseException`, para no tragar Ctrl+C). Tiempo O(n) llamadas a func, espacio O(1). Mejora real: backoff exponencial y reintentar solo ciertas excepciones.
# Entrevistador: ¿Cómo harías que solo reintente ante ciertas excepciones, o que espere entre intentos? ¿Es seguro reintentar una función con efectos secundarios (no idempotente)?


if __name__ == "__main__":
    llamadas = []

    @reintentar(3)
    def inestable():
        llamadas.append(1)
        if len(llamadas) < 3:
            raise ValueError("falla")
        return "ok"

    assert inestable() == "ok"
    assert len(llamadas) == 3, "se detiene al tener éxito"
    assert inestable.__name__ == "inestable"

    intentos = []

    @reintentar(2)
    def siempre_falla():
        intentos.append(1)
        raise KeyError("x")

    try:
        siempre_falla()
        assert False, "debía relanzar la excepción"
    except KeyError:
        pass
    assert len(intentos) == 2, "exactamente n intentos"

    @reintentar(1)
    def bien(a, b=1):
        return a + b

    assert bien(2, b=3) == 5, "pasa args y kwargs"
    print("OK: todos los tests pasan")
