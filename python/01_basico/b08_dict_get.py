r"""b08 - dict.get y recorrer diccionarios (facil)

Implementa:

1. `contar_caracteres(s)`: devuelve un dict `{caracter: veces}` SIN usar Counter (usa `dict.get(k, 0)`).
   `contar_caracteres('hola')` -> `{'h': 1, 'o': 1, 'l': 1, 'a': 1}`
2. `clave_mayor(d)`: devuelve la clave con el valor mas grande; si `d` esta vacio devuelve `None`.
   `clave_mayor({'a': 1, 'b': 5, 'c': 3})` -> `'b'`
3. `valor_o_defecto(d, k)`: devuelve `d[k]` o la cadena `'N/A'` si no existe, sin lanzar KeyError.
"""

# Pista 1: `d[c] = d.get(c, 0) + 1`.
# Pista 2: Recorre con `for k, v in d.items():` y guarda el maximo.
# Pista 3: `max(d, key=d.get)` funciona pero falla con dict vacio (ValueError): maneja ese caso antes.

def contar_caracteres(s):
    pass


def clave_mayor(d):
    pass


def valor_o_defecto(d, k):
    pass

if __name__ == "__main__":
    assert contar_caracteres('hola') == {'h': 1, 'o': 1, 'l': 1, 'a': 1}
    assert contar_caracteres('aab') == {'a': 2, 'b': 1}
    assert contar_caracteres('') == {}, "vacio"
    assert clave_mayor({'a': 1, 'b': 5, 'c': 3}) == 'b'
    assert clave_mayor({'x': 0}) == 'x', "un elemento"
    assert clave_mayor({}) is None, "dict vacio"
    assert valor_o_defecto({'a': 1}, 'a') == 1
    assert valor_o_defecto({'a': 1}, 'z') == 'N/A'
    assert valor_o_defecto({'a': None}, 'a') is None, "valor None existente no es 'N/A'"
    print("OK: todos los tests pasan")
