"""i01 - Decorador contar_llamadas (SOLUCIÓN)
"""

import functools


def contar_llamadas(func):
    @functools.wraps(func)
    def envoltura(*args, **kwargs):
        envoltura.llamadas += 1
        return func(*args, **kwargs)

    envoltura.llamadas = 0
    return envoltura

# Explicación:
# `@contar_llamadas` equivale a `suma = contar_llamadas(suma)`. La envoltura es un closure que ve `func`; como las funciones son objetos, guardamos el contador como atributo (evita `nonlocal`/globales). `functools.wraps` copia `__name__`, `__doc__`, etc. (sin él, todas las funciones decoradas se llamarían 'envoltura'). Tiempo O(1) extra por llamada, espacio O(1). Alternativa: clase con `__call__`.
# Entrevistador: ¿Y si decoro un método de una clase? ¿El contador es por instancia o global? ¿Qué pasa en un entorno con hilos?


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
