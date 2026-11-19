"""i16 - Context managers propios (SOLUCIÓN)
"""

import time
from contextlib import contextmanager


class Temporizador:
    def __enter__(self):
        self._inicio = time.perf_counter()
        return self

    def __exit__(self, tipo, valor, traza):
        self.segundos = time.perf_counter() - self._inicio
        return False  # no suprime excepciones


@contextmanager
def temporalmente(d, clave, valor):
    ausente = object()
    anterior = d.get(clave, ausente)
    d[clave] = valor
    try:
        yield d
    finally:
        if anterior is ausente:
            d.pop(clave, None)
        else:
            d[clave] = anterior

# Explicación:
# `with` garantiza la limpieza como un `try/finally`. En la versión de clase, `__exit__` devuelve truthy solo si quieres SUPRIMIR la excepción: casi nunca. Con `@contextmanager` el generador debe tener un solo `yield`; sin `try/finally` alrededor, una excepción en el cuerpo se relanza en el yield y saltaría la restauración. Usamos un centinela `object()` en vez de `None` para distinguir 'clave ausente' de 'valor None'. Todo O(1).
# Entrevistador: ¿Qué pasa si `__exit__` devuelve True? ¿Qué diferencia hay entre `with open(...)` y abrir/cerrar a mano ante una excepción? ¿Por qué un centinela y no None?


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
