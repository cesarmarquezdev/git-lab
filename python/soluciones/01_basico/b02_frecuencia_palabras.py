r"""b02 - Frecuencia de palabras con Counter (facil)

Escribe `top_palabras(texto, n)` que devuelva una lista de tuplas `(palabra, veces)` con las `n` palabras mas frecuentes de `texto`, de mayor a menor. Ignora mayusculas/minusculas y separa por espacios en blanco (`split()`). En empates, mantén el orden de primera aparicion (es lo que hace `most_common`).

Ejemplo:
`top_palabras("el gato y el perro y el pez", 2)` -> `[('el', 3), ('y', 2)]`

Casos borde: texto vacio -> `[]`; `n` mayor que palabras distintas -> devuelve todas.
"""

from collections import Counter


def top_palabras(texto, n):
    return Counter(texto.lower().split()).most_common(n)

# Explicacion: Counter es un dict especializado para contar; construirlo es O(m) para m palabras y most_common(n) es O(k log n) con k distintas. Sin Counter: dict + `d[p] = d.get(p, 0) + 1` y luego `sorted(d.items(), key=lambda kv: -kv[1])` (sorted es estable, por eso mantiene el orden de aparicion en empates).
# Pregunta del entrevistador: ¿Y si el texto tiene signos de puntuacion ('hola,' vs 'hola')? ¿Como lo limpiarias? (re.findall(r'\w+') o str.strip(puntuacion).)

if __name__ == "__main__":
    assert top_palabras("el gato y el perro y el pez", 2) == [('el', 3), ('y', 2)]
    assert top_palabras("", 3) == [], "texto vacio"
    assert top_palabras("Hola hola HOLA", 1) == [('hola', 3)], "ignora mayusculas"
    assert top_palabras("a b", 10) == [('a', 1), ('b', 1)], "n mayor que distintas"
    assert top_palabras("  a   a  ", 1) == [('a', 2)], "espacios extra"
    print("OK: todos los tests pasan")
