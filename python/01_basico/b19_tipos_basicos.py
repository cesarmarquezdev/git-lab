r"""b19 - Tipos basicos y bool vs int (facil)

Escribe `contar_tipos(valores)` que reciba una lista de valores y devuelva un dict `{nombre_del_tipo: cantidad}` usando `type(v).__name__`.

Ejemplo: `contar_tipos([1, 2.0, 'a', True, None, [1], (1,), {1}, {'a': 1}, 3])`
-> `{'int': 2, 'float': 1, 'str': 1, 'bool': 1, 'NoneType': 1, 'list': 1, 'tuple': 1, 'set': 1, 'dict': 1}`

Nota: `True` cuenta como `bool`, NO como `int` (bool es subclase de int, asi que `isinstance(True, int)` seria True; `type()` no se confunde).
Casos borde: lista vacia -> `{}`.
"""

# Pista 1: `type(v).__name__` da el nombre como string.
# Pista 2: Cuenta con `d[nombre] = d.get(nombre, 0) + 1`.
# Pista 3: No uses isinstance(v, int) para distinguir bool.

def contar_tipos(valores):
    pass

if __name__ == "__main__":
    r = contar_tipos([1, 2.0, 'a', True, None, [1], (1,), {1}, {'a': 1}, 3])
    assert r == {'int': 2, 'float': 1, 'str': 1, 'bool': 1, 'NoneType': 1,
                 'list': 1, 'tuple': 1, 'set': 1, 'dict': 1}
    assert contar_tipos([]) == {}, "vacia"
    assert contar_tipos([True, False, 1]) == {'bool': 2, 'int': 1}, "bool no es int"
    assert contar_tipos([None]) == {'NoneType': 1}
    print("OK: todos los tests pasan")
