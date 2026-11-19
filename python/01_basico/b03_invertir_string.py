r"""b03 - Invertir un string de 3 formas (facil)

Implementa tres funciones que inviertan un string, cada una con una tecnica distinta:
1. `invertir_slicing(s)` usando slicing.
2. `invertir_loop(s)` usando un bucle `for` que va construyendo el resultado.
3. `invertir_reversed(s)` usando `reversed()` y `''.join`.

Ejemplos: `'hola'` -> `'aloh'`, `'ab'` -> `'ba'`.
Casos borde: string vacio -> `''`, un caracter -> el mismo.
"""

# Pista 1: Slicing con paso negativo: `s[::-1]`.
# Pista 2: En el bucle, ve prependiendo: `resultado = c + resultado`.
# Pista 3: `reversed(s)` devuelve un iterador de caracteres; `''.join(...)` los une.

def invertir_slicing(s):
    pass


def invertir_loop(s):
    pass


def invertir_reversed(s):
    pass

if __name__ == "__main__":
    for f in (invertir_slicing, invertir_loop, invertir_reversed):
        assert f('hola') == 'aloh', f.__name__
        assert f('') == '', f.__name__ + " vacio"
        assert f('a') == 'a', f.__name__ + " un caracter"
        assert f('ab cd') == 'dc ba', f.__name__ + " con espacio"
    print("OK: todos los tests pasan")
