"""i17 - __eq__ y __hash__ para usar en set (media)

Crea la clase `Punto(x, y)` para que dos puntos con las mismas coordenadas sean **iguales** y puedan usarse en un `set` o como clave de `dict` (sin duplicados). Implementa `__eq__`, `__hash__` y `__repr__` (`Punto(1, 2)`). Comparar con un objeto de otro tipo no debe fallar y debe dar `False`.

Ejemplo:
```
len({Punto(1,2), Punto(1,2), Punto(2,1)})  # 2
Punto(1,2) == (1,2)  # False
```

Pistas (no mires hasta intentarlo):
Pista 1: Por defecto `==` compara identidad (`is`), por eso dos Punto(1,2) son distintos.
Pista 2: `__hash__` debe ser coherente con `__eq__`: objetos iguales => mismo hash. Delega en `hash((self.x, self.y))`.
Pista 3: En `__eq__`, si `otro` no es `Punto` devuelve `NotImplemented`.

Entrevistador: ¿Qué pasa si defino `__eq__` pero no `__hash__`? ¿Y si el objeto es mutable y cambio x después de meterlo al set? ¿Cómo lo resuelve un `@dataclass(frozen=True)`?
"""

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    assert Punto(1, 2) == Punto(1, 2)
    assert Punto(1, 2) != Punto(2, 1)
    assert len({Punto(1, 2), Punto(1, 2), Punto(2, 1)}) == 2, "sin duplicados en el set"
    d = {Punto(0, 0): "origen"}
    assert d[Punto(0, 0)] == "origen", "usable como clave de dict"
    assert Punto(1, 2) in {Punto(1, 2)}
    assert (Punto(1, 2) == (1, 2)) is False, "otro tipo => False, sin error"
    assert Punto(1, 2) != "texto"
    assert hash(Punto(3, 4)) == hash(Punto(3, 4))
    assert repr(Punto(1, 2)) == "Punto(1, 2)"
    assert len(set()) == 0 and Punto(5, 5) not in set()
    print("OK: todos los tests pasan")
