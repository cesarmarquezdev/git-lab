r"""b14 - Excepciones: raise y except especifico (facil)

Implementa:

1. `dividir(a, b)`: devuelve `a / b`. Si `b == 0` debe lanzar `ValueError('no se puede dividir entre cero')` (captura `ZeroDivisionError` y relanza como `ValueError`).
2. `a_entero(texto, defecto=None)`: convierte con `int()`; si el texto no es un entero valido devuelve `defecto`. Captura SOLO `ValueError`: si `texto` es `None`, el `TypeError` debe propagarse.
3. `intentar(funcion)`: llama a `funcion()` y devuelve `('ok', resultado)` si no falla, o `('error', 'NombreDeLaExcepcion')` si falla (usa `try/except/else`, y `type(e).__name__`).

Ejemplos: `dividir(6, 3)` -> `2.0`; `a_entero('12')` -> `12`; `a_entero('x', 0)` -> `0`.
"""

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("no se puede dividir entre cero")


def a_entero(texto, defecto=None):
    try:
        return int(texto)
    except ValueError:
        return defecto


def intentar(funcion):
    try:
        resultado = funcion()
    except Exception as e:
        return ("error", type(e).__name__)
    else:
        return ("ok", resultado)

# Explicacion: Captura la excepcion mas especifica posible: un except demasiado ancho esconde bugs reales (como el TypeError de None). `else` se ejecuta solo si no hubo excepcion; `finally` siempre. En `dividir`, `raise ... from None` evitaria el encadenado en el traceback.
# Pregunta del entrevistador: ¿Cuando usarias `finally` y que pasa si hay un `return` dentro del try? (finally se ejecuta igual, antes de devolver; un return en finally pisa el del try.)

if __name__ == "__main__":
    assert dividir(6, 3) == 2.0
    try:
        dividir(1, 0)
    except ValueError as e:
        assert 'cero' in str(e)
    else:
        assert False, "dividir(1, 0) debia lanzar ValueError"
    assert a_entero('12') == 12
    assert a_entero(' 7 ') == 7, "int tolera espacios"
    assert a_entero('x') is None
    assert a_entero('x', 0) == 0
    assert a_entero('') is None, "vacio"
    try:
        a_entero(None)
    except TypeError:
        pass
    else:
        assert False, "TypeError debia propagarse (solo se captura ValueError)"
    assert intentar(lambda: 5) == ('ok', 5)
    assert intentar(lambda: 1 / 0) == ('error', 'ZeroDivisionError')
    assert intentar(lambda: int('x')) == ('error', 'ValueError')
    assert intentar(lambda: [][0]) == ('error', 'IndexError')
    print("OK: todos los tests pasan")
