"""i05 - @property con setter que valida (SOLUCIÓN)
"""

class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius  # pasa por el setter

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("por debajo del cero absoluto")
        self._celsius = valor

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

# Explicación:
# `@property` convierte un método en atributo calculado; sin setter es de solo lectura. Asignar en `__init__` vía `self.celsius = ...` garantiza que el invariante se cumpla desde el principio. La API pública no cambia si más tarde pasas de atributo simple a property (por eso en Python no se escriben getters/setters 'por si acaso'). Acceso O(1).
# Entrevistador: ¿Por qué `self._celsius = celsius` en `__init__` sería un bug sutil? ¿Qué pasa si un `@property` hace algo costoso y se llama en un bucle?


if __name__ == "__main__":
    t = Temperatura(100)
    assert t.celsius == 100
    assert t.fahrenheit == 212.0
    t.celsius = 0
    assert t.fahrenheit == 32.0
    t.celsius = -273.15
    assert t.celsius == -273.15, "el borde es válido"
    try:
        t.celsius = -300
        assert False, "debía lanzar ValueError"
    except ValueError:
        pass
    assert t.celsius == -273.15, "un valor inválido no modifica el estado"
    try:
        Temperatura(-500)
        assert False, "el constructor también valida"
    except ValueError:
        pass
    try:
        t.fahrenheit = 10
        assert False, "fahrenheit es de solo lectura"
    except AttributeError:
        pass
    print("OK: todos los tests pasan")
