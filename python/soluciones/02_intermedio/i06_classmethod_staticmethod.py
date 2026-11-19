"""i06 - @classmethod vs @staticmethod (SOLUCIÓN)
"""

class Fecha:
    def __init__(self, dia, mes, anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio

    @classmethod
    def desde_cadena(cls, texto):
        dia, mes, anio = (int(p) for p in texto.split("/"))
        return cls(dia, mes, anio)

    @staticmethod
    def es_bisiesto(anio):
        return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

    def __eq__(self, otra):
        if not isinstance(otra, Fecha):
            return NotImplemented
        return (self.dia, self.mes, self.anio) == (otra.dia, otra.mes, otra.anio)

# Explicación:
# `@classmethod` recibe la clase (`cls`): sirve para constructores alternativos y funciona con herencia porque `cls` es la subclase real. `@staticmethod` no recibe nada: es una función normal que vive en el espacio de nombres de la clase por organización. `__eq__` devuelve `NotImplemented` ante tipos ajenos para que Python pruebe el otro lado y caiga en `False`. Todo O(1).
# Entrevistador: Si defino `__eq__` sin `__hash__`, ¿puedo meter fechas en un set? ¿Por qué? ¿Cuándo preferirías una función de módulo en vez de un staticmethod?


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
