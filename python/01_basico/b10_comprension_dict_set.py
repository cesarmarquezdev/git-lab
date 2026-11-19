r"""b10 - Comprensiones de dict y set (facil)

Implementa:

1. `longitudes(palabras)`: dict `{palabra: len(palabra)}` con una dict comprehension.
   `longitudes(['hola', 'a'])` -> `{'hola': 4, 'a': 1}`
2. `iniciales_unicas(palabras)`: set con las primeras letras en MINUSCULA de las palabras (ignora palabras vacias).
   `iniciales_unicas(['Ana', 'abel', 'Bea', ''])` -> `{'a', 'b'}`
3. `invertir_dict(d)`: dict con claves y valores intercambiados (asume que los valores son unicos).
   `invertir_dict({'a': 1, 'b': 2})` -> `{1: 'a', 2: 'b'}`
"""

# Pista 1: dict comprehension: `{k: v for ... }`; set comprehension: `{x for ...}` (ojo: `{}` vacio es un dict).
# Pista 2: Para ignorar vacias, añade `if p`.
# Pista 3: `{v: k for k, v in d.items()}`

def longitudes(palabras):
    pass


def iniciales_unicas(palabras):
    pass


def invertir_dict(d):
    pass

if __name__ == "__main__":
    assert longitudes(['hola', 'a']) == {'hola': 4, 'a': 1}
    assert longitudes([]) == {}
    assert iniciales_unicas(['Ana', 'abel', 'Bea', '']) == {'a', 'b'}
    assert iniciales_unicas([]) == set(), "set vacio, no dict"
    assert type(iniciales_unicas([])) is set
    assert iniciales_unicas(['x']) == {'x'}
    assert invertir_dict({'a': 1, 'b': 2}) == {1: 'a', 2: 'b'}
    assert invertir_dict({}) == {}
    print("OK: todos los tests pasan")
