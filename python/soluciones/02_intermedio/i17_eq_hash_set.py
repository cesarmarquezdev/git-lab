"""i17 - __eq__ y __hash__ para usar en set (SOLUCIÓN)
"""

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, otro):
        if not isinstance(otro, Punto):
            return NotImplemented
        return (self.x, self.y) == (otro.x, otro.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Punto({self.x}, {self.y})"

# Explicación:
# Un set/dict usa `hash` para localizar el cubo y `==` para confirmar: contrato = si `a == b` entonces `hash(a) == hash(b)`. Al definir `__eq__` sin `__hash__`, Python pone `__hash__ = None` y la clase deja de ser hasheable. Los objetos usados como clave deberían ser inmutables (si cambias x/y tras insertar, el objeto queda 'perdido' en el set). Operaciones O(1) promedio.
# Entrevistador: ¿Qué pasa si defino `__eq__` pero no `__hash__`? ¿Y si el objeto es mutable y cambio x después de meterlo al set? ¿Cómo lo resuelve un `@dataclass(frozen=True)`?


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
