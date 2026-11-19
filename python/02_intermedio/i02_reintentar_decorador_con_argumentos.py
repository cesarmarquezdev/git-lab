"""i02 - Decorador con argumentos: reintentar(n) (dificil)

Escribe `reintentar(n)`, un decorador **con argumentos**. La función decorada se intenta hasta `n` veces: si lanza una excepción se reintenta; si tiene éxito se devuelve su resultado. Si falla las `n` veces, se vuelve a lanzar la **última** excepción. Conserva `__name__`.

Ejemplo:
```
@reintentar(3)
def inestable(): ...  # falla 2 veces y a la tercera devuelve 'ok'
inestable()  # 'ok'
```

Pistas (no mires hasta intentarlo):
Pista 1: Necesitas tres niveles: `reintentar(n)` -> `decorador(func)` -> `envoltura(*args, **kwargs)`.
Pista 2: Dentro de la envoltura usa un `for` de `n` intentos con `try/except Exception as e`.
Pista 3: Guarda la última excepción y haz `raise` de ella al terminar el bucle.

Entrevistador: ¿Cómo harías que solo reintente ante ciertas excepciones, o que espere entre intentos? ¿Es seguro reintentar una función con efectos secundarios (no idempotente)?
"""

import functools


def reintentar(n):
    # tu código aquí
    pass


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
