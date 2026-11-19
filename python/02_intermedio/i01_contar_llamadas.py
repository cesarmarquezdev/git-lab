"""i01 - Decorador contar_llamadas (media)

Escribe el decorador `contar_llamadas` que cuente cuántas veces se llama a la función decorada. El contador debe estar disponible como atributo `llamadas` de la función decorada (empieza en 0). Debe aceptar cualquier combinación de `*args` y `**kwargs`, devolver el resultado original y conservar `__name__` y `__doc__` de la función original.

Ejemplo:
```
@contar_llamadas
def suma(a, b=0): return a + b
suma(1, 2); suma(1, b=5)
suma.llamadas  # 2
```

Pistas (no mires hasta intentarlo):
Pista 1: Un decorador es una función que recibe una función y devuelve otra (la envoltura).
Pista 2: La envoltura es un objeto: puedes asignarle atributos, como `envoltura.llamadas = 0`.
Pista 3: Usa `functools.wraps(func)` sobre la envoltura para conservar nombre y docstring.

Entrevistador: ¿Y si decoro un método de una clase? ¿El contador es por instancia o global? ¿Qué pasa en un entorno con hilos?
"""

import functools


def contar_llamadas(func):
    # tu código aquí
    pass


if __name__ == "__main__":
    @contar_llamadas
    def suma(a, b=0):
        """Suma dos números."""
        return a + b

    assert suma.llamadas == 0, "empieza en 0"
    assert suma(1, 2) == 3
    assert suma(1, b=5) == 6
    assert suma.llamadas == 2, "cuenta posicionales y keyword"
    assert suma.__name__ == "suma", "usa functools.wraps"
    assert suma.__doc__ == "Suma dos números."

    @contar_llamadas
    def saluda():
        return "hola"

    assert saluda.llamadas == 0 and suma.llamadas == 2, "contadores independientes"
    saluda(); saluda(); saluda()
    assert saluda.llamadas == 3
    print("OK: todos los tests pasan")
