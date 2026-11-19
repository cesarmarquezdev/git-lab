r"""b08 - dict.get y recorrer diccionarios (facil)

Implementa:

1. `contar_caracteres(s)`: devuelve un dict `{caracter: veces}` SIN usar Counter (usa `dict.get(k, 0)`).
   `contar_caracteres('hola')` -> `{'h': 1, 'o': 1, 'l': 1, 'a': 1}`
2. `clave_mayor(d)`: devuelve la clave con el valor mas grande; si `d` esta vacio devuelve `None`.
   `clave_mayor({'a': 1, 'b': 5, 'c': 3})` -> `'b'`
3. `valor_o_defecto(d, k)`: devuelve `d[k]` o la cadena `'N/A'` si no existe, sin lanzar KeyError.
"""

def contar_caracteres(s):
    conteo = {}
    for c in s:
        conteo[c] = conteo.get(c, 0) + 1
    return conteo


def clave_mayor(d):
    if not d:
        return None
    return max(d, key=d.get)


def valor_o_defecto(d, k):
    return d.get(k, "N/A")

# Explicacion: get(k, default) evita KeyError y no inserta la clave. Acceso a dict es O(1) promedio, asi que contar es O(n). max(d, key=d.get) itera las claves y compara por valor: O(n).
# Pregunta del entrevistador: ¿Diferencia entre `d.get(k, [])` y `d.setdefault(k, [])`? ¿Y con defaultdict? (setdefault inserta la clave; defaultdict la crea al acceder.)

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
