r"""b10 - Comprensiones de dict y set (facil)

Implementa:

1. `longitudes(palabras)`: dict `{palabra: len(palabra)}` con una dict comprehension.
   `longitudes(['hola', 'a'])` -> `{'hola': 4, 'a': 1}`
2. `iniciales_unicas(palabras)`: set con las primeras letras en MINUSCULA de las palabras (ignora palabras vacias).
   `iniciales_unicas(['Ana', 'abel', 'Bea', ''])` -> `{'a', 'b'}`
3. `invertir_dict(d)`: dict con claves y valores intercambiados (asume que los valores son unicos).
   `invertir_dict({'a': 1, 'b': 2})` -> `{1: 'a', 2: 'b'}`
"""

def longitudes(palabras):
    return {p: len(p) for p in palabras}


def iniciales_unicas(palabras):
    return {p[0].lower() for p in palabras if p}


def invertir_dict(d):
    return {v: k for k, v in d.items()}

# Explicacion: Las tres son O(n). El set elimina duplicados automaticamente. Si los valores de invertir_dict se repiten, la ultima clave gana (se pierden datos).
# Pregunta del entrevistador: En invertir_dict, ¿que pasa si hay valores repetidos o no hashables? (Se pisan las claves; una lista como valor da TypeError al usarse de clave.)

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
