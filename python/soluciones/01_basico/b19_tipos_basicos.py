r"""b19 - Tipos basicos y bool vs int (facil)

Escribe `contar_tipos(valores)` que reciba una lista de valores y devuelva un dict `{nombre_del_tipo: cantidad}` usando `type(v).__name__`.

Ejemplo: `contar_tipos([1, 2.0, 'a', True, None, [1], (1,), {1}, {'a': 1}, 3])`
-> `{'int': 2, 'float': 1, 'str': 1, 'bool': 1, 'NoneType': 1, 'list': 1, 'tuple': 1, 'set': 1, 'dict': 1}`

Nota: `True` cuenta como `bool`, NO como `int` (bool es subclase de int, asi que `isinstance(True, int)` seria True; `type()` no se confunde).
Casos borde: lista vacia -> `{}`.
"""

def contar_tipos(valores):
    conteo = {}
    for v in valores:
        nombre = type(v).__name__
        conteo[nombre] = conteo.get(nombre, 0) + 1
    return conteo

# Explicacion: Todo en Python es un objeto con tipo. type() devuelve el tipo exacto; isinstance considera herencia (isinstance(True, int) es True). Mutables: list, dict, set. Inmutables: int, float, str, bool, tuple, None. O(n).
# Pregunta del entrevistador: ¿Por que una tupla es hashable y una lista no, y que pasa con una tupla que contiene una lista? (Hashable solo si todo su contenido lo es.)

if __name__ == "__main__":
    r = contar_tipos([1, 2.0, 'a', True, None, [1], (1,), {1}, {'a': 1}, 3])
    assert r == {'int': 2, 'float': 1, 'str': 1, 'bool': 1, 'NoneType': 1,
                 'list': 1, 'tuple': 1, 'set': 1, 'dict': 1}
    assert contar_tipos([]) == {}, "vacia"
    assert contar_tipos([True, False, 1]) == {'bool': 2, 'int': 1}, "bool no es int"
    assert contar_tipos([None]) == {'NoneType': 1}
    print("OK: todos los tests pasan")
