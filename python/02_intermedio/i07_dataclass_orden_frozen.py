"""i07 - Dataclasses: orden, frozen y default_factory (media)

Usando `@dataclass` define:
1. `Version(major, minor, patch)` con enteros: **ordenable** (`<`, `>`) y **inmutable** (frozen), por tanto hasheable.
2. `Carrito(dueno: str, items: list[str])` donde `items` por defecto es una lista **vacía propia de cada instancia**, con un método `agregar(item)` que añade a `items`.

Ejemplo:
```
Version(1,2,3) < Version(1,10,0)  # True
Carrito('ana').items  # []
```

Pistas (no mires hasta intentarlo):
Pista 1: Los parámetros del decorador: `@dataclass(order=True, frozen=True)`.
Pista 2: No pongas `items: list = []`: dataclass lo rechaza porque sería compartido. Usa `field(default_factory=list)`.
Pista 3: `order=True` compara como tuplas siguiendo el orden de declaración de los campos.

Entrevistador: ¿Por qué dataclass rechaza `items: list = []`? ¿Qué diferencia hay entre `frozen=True` y 'inmutable de verdad' si el campo contiene una lista?
"""

from dataclasses import dataclass, field


class Version:
    pass


class Carrito:
    pass


if __name__ == "__main__":
    import dataclasses

    assert Version(1, 2, 3) < Version(1, 10, 0), "compara por campos en orden"
    assert Version(2, 0, 0) > Version(1, 99, 99)
    assert Version(1, 0, 0) == Version(1, 0, 0)
    assert sorted([Version(1, 2, 0), Version(0, 9, 9), Version(1, 0, 5)]) == [Version(0, 9, 9), Version(1, 0, 5), Version(1, 2, 0)]
    v = Version(1, 0, 0)
    try:
        v.major = 5
        assert False, "debía ser frozen"
    except dataclasses.FrozenInstanceError:
        pass
    assert len({Version(1, 0, 0), Version(1, 0, 0), Version(1, 0, 1)}) == 2, "frozen + eq => hasheable"
    c1, c2 = Carrito("ana"), Carrito("luis")
    c1.agregar("pan")
    assert c1.items == ["pan"]
    assert c2.items == [], "cada carrito tiene su propia lista"
    assert Carrito("x", ["a"]).items == ["a"]
    assert "Carrito(dueno='ana'" in repr(c1), "repr automático"
    print("OK: todos los tests pasan")
