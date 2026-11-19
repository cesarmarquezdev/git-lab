"""i16 - Context managers propios (dificil)

Implementa dos context managers:
1. Clase `Temporizador` con `__enter__`/`__exit__`: al salir del `with` guarda en `self.segundos` (float >= 0) el tiempo transcurrido (usa `time.perf_counter()`). `__enter__` devuelve `self`. **No debe tragarse las excepciones** (deben propagarse), pero `segundos` debe quedar guardado aun así.
2. Función `temporalmente(d, clave, valor)` con `@contextlib.contextmanager`: dentro del `with`, `d[clave] = valor`; al salir (incluso si hubo excepción) se restaura el valor anterior, o se elimina la clave si no existía.

Ejemplo:
```
d = {'a': 1}
with temporalmente(d, 'a', 2): d['a']  # 2
d['a']  # 1
```

Pistas (no mires hasta intentarlo):
Pista 1: `__exit__(self, tipo, valor, traza)`: devolver `False`/`None` deja propagar la excepción.
Pista 2: Con `@contextmanager` el código antes del `yield` es el enter y el de después es el exit.
Pista 3: Usa `try/finally` alrededor del `yield` para restaurar aunque haya excepción.

Entrevistador: ¿Qué pasa si `__exit__` devuelve True? ¿Qué diferencia hay entre `with open(...)` y abrir/cerrar a mano ante una excepción? ¿Por qué un centinela y no None?
"""

import time
from contextlib import contextmanager


class Temporizador:
    pass


@contextmanager
def temporalmente(d, clave, valor):
    pass


if __name__ == "__main__":
    with Temporizador() as t:
        suma = sum(range(1000))
    assert isinstance(t.segundos, float) and t.segundos >= 0
    t2 = Temporizador()
    try:
        with t2:
            raise ValueError("boom")
        assert False, "no debe tragarse la excepción"
    except ValueError:
        pass
    assert t2.segundos >= 0, "segundos se guarda aunque haya excepción"

    d = {"a": 1}
    with temporalmente(d, "a", 2):
        assert d["a"] == 2
    assert d == {"a": 1}, "restaura el valor previo"
    with temporalmente(d, "nueva", 9):
        assert d["nueva"] == 9
    assert "nueva" not in d, "elimina la clave que no existía"
    try:
        with temporalmente(d, "a", 5):
            raise RuntimeError("x")
    except RuntimeError:
        pass
    assert d == {"a": 1}, "restaura incluso con excepción"
    print("OK: todos los tests pasan")
