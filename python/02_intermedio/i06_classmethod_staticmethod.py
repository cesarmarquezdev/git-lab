"""i06 - @classmethod vs @staticmethod (media)

Completa la clase `Fecha(dia, mes, anio)`:
- `@classmethod desde_cadena(cls, texto)`: constructor alternativo que recibe `'25/12/2024'` y devuelve una instancia **de `cls`** (debe funcionar bien en subclases).
- `@staticmethod es_bisiesto(anio)`: True si el año es bisiesto (no necesita ni `self` ni `cls`).
- `__eq__` para comparar fechas por valor.

Ejemplo:
```
Fecha.desde_cadena('25/12/2024') == Fecha(25, 12, 2024)  # True
Fecha.es_bisiesto(1900)  # False
```

Pistas (no mires hasta intentarlo):
Pista 1: `desde_cadena` debe separar con `.split('/')` y convertir cada parte con `int`.
Pista 2: Devuelve `cls(dia, mes, anio)`, no `Fecha(...)`, para respetar las subclases.
Pista 3: Bisiesto: divisible entre 4 y (no divisible entre 100 o divisible entre 400).

Entrevistador: Si defino `__eq__` sin `__hash__`, ¿puedo meter fechas en un set? ¿Por qué? ¿Cuándo preferirías una función de módulo en vez de un staticmethod?
"""

class Fecha:
    def __init__(self, dia, mes, anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio

    @classmethod
    def desde_cadena(cls, texto):
        pass

    @staticmethod
    def es_bisiesto(anio):
        pass

    def __eq__(self, otra):
        pass


if __name__ == "__main__":
    f = Fecha.desde_cadena("25/12/2024")
    assert (f.dia, f.mes, f.anio) == (25, 12, 2024)
    assert f == Fecha(25, 12, 2024)
    assert f != Fecha(1, 1, 2024)
    assert Fecha.es_bisiesto(2024) is True
    assert Fecha.es_bisiesto(1900) is False, "100 no, salvo 400"
    assert Fecha.es_bisiesto(2000) is True
    assert Fecha.es_bisiesto(2023) is False
    assert f.es_bisiesto(2024) is True, "también se puede llamar desde la instancia"

    class FechaEspecial(Fecha):
        pass

    g = FechaEspecial.desde_cadena("1/1/2000")
    assert type(g) is FechaEspecial, "classmethod debe respetar la subclase (usa cls)"
    assert (f == 5) is False, "comparar con otro tipo no debe fallar"
    print("OK: todos los tests pasan")
