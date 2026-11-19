"""i05 - @property con setter que valida (media)

Crea la clase `Temperatura` que guarda grados Celsius. Requisitos:
- `Temperatura(celsius)` inicializa usando el **setter** (para que valide también al construir).
- Propiedad `celsius` con getter y setter; el setter lanza `ValueError` si el valor es menor a -273.15 (cero absoluto).
- Propiedad de solo lectura `fahrenheit` (= celsius * 9/5 + 32); intentar asignarla lanza `AttributeError`.

Ejemplo:
```
t = Temperatura(100); t.fahrenheit  # 212.0
t.celsius = -300  # ValueError
```

Pistas (no mires hasta intentarlo):
Pista 1: Guarda el dato real en un atributo 'privado' como `self._celsius`.
Pista 2: `@property def celsius` devuelve `_celsius`; `@celsius.setter` valida y asigna.
Pista 3: En `__init__` escribe `self.celsius = celsius` (no `self._celsius`) para reutilizar la validación.

Entrevistador: ¿Por qué `self._celsius = celsius` en `__init__` sería un bug sutil? ¿Qué pasa si un `@property` hace algo costoso y se llama en un bucle?
"""

class Temperatura:
    def __init__(self, celsius):
        # tu código aquí
        pass


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
