"""Anagrama valido

Escribe `es_anagrama(a, b)` que diga si `b` es un anagrama de `a`: mismas letras con la misma cantidad de veces, en cualquier orden. Distingue mayusculas de minusculas.
Ejemplos:
`es_anagrama("listen", "silent")` -> True
`es_anagrama("rat", "car")` -> False
`es_anagrama("aab", "abb")` -> False

Pistas:
  1. Si las longitudes son distintas ya sabes la respuesta.
  2. Cuenta cuantas veces aparece cada letra.
  3. `collections.Counter(a) == Counter(b)` resume la idea; tambien vale un dict a mano.
"""

def es_anagrama(a, b):
    # tu codigo aqui
    pass


if __name__ == "__main__":
    assert es_anagrama("listen", "silent") is True
    assert es_anagrama("rat", "car") is False
    assert es_anagrama("aab", "abb") is False, "mismas letras distinta cantidad"
    assert es_anagrama("", "") is True, "vacios"
    assert es_anagrama("a", "a") is True
    assert es_anagrama("a", "b") is False
    assert es_anagrama("abc", "ab") is False, "longitudes distintas"
    assert es_anagrama("Ab", "ab") is False, "distingue mayusculas"
    print("OK: todos los tests pasan")
