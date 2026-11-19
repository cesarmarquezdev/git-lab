r"""b02 - Frecuencia de palabras con Counter (facil)

Escribe `top_palabras(texto, n)` que devuelva una lista de tuplas `(palabra, veces)` con las `n` palabras mas frecuentes de `texto`, de mayor a menor. Ignora mayusculas/minusculas y separa por espacios en blanco (`split()`). En empates, mantén el orden de primera aparicion (es lo que hace `most_common`).

Ejemplo:
`top_palabras("el gato y el perro y el pez", 2)` -> `[('el', 3), ('y', 2)]`

Casos borde: texto vacio -> `[]`; `n` mayor que palabras distintas -> devuelve todas.
"""

# Pista 1: `from collections import Counter`.
# Pista 2: Normaliza con `.lower().split()` antes de contar.
# Pista 3: `Counter(palabras).most_common(n)`.

from collections import Counter


def top_palabras(texto, n):
    # tu código aquí
    pass

if __name__ == "__main__":
    assert top_palabras("el gato y el perro y el pez", 2) == [('el', 3), ('y', 2)]
    assert top_palabras("", 3) == [], "texto vacio"
    assert top_palabras("Hola hola HOLA", 1) == [('hola', 3)], "ignora mayusculas"
    assert top_palabras("a b", 10) == [('a', 1), ('b', 1)], "n mayor que distintas"
    assert top_palabras("  a   a  ", 1) == [('a', 2)], "espacios extra"
    print("OK: todos los tests pasan")
