"""Primer caracter no repetido

Escribe `primer_no_repetido(s)` que devuelva el primer caracter que aparece una sola vez en `s`, o None si no existe.
Ejemplos:
`primer_no_repetido("leetcode")` -> "l"
`primer_no_repetido("aabb")` -> None

Pistas:
  1. Necesitas saber cuantas veces aparece cada caracter.
  2. Primera pasada: contar. Segunda pasada: buscar el primero con conteo 1.
  3. El orden original lo da recorrer la cadena de nuevo, no el dict.
"""

def primer_no_repetido(s):
    # tu codigo aqui
    pass


if __name__ == "__main__":
    assert primer_no_repetido("leetcode") == "l"
    assert primer_no_repetido("loveleetcode") == "v"
    assert primer_no_repetido("aabb") is None
    assert primer_no_repetido("") is None, "vacia"
    assert primer_no_repetido("z") == "z", "un caracter"
    print("OK: todos los tests pasan")
