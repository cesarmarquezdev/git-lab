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
    if len(a) != len(b):
        return False
    conteo = {}
    for c in a:
        conteo[c] = conteo.get(c, 0) + 1
    for c in b:
        if conteo.get(c, 0) == 0:
            return False
        conteo[c] -= 1
    return True


# Explicacion
# 1) Casos borde a preguntar: vacios, longitudes distintas, mayusculas, espacios, ¿solo ASCII o unicode?
# 2) Solucion ingenua: ordenar ambas cadenas y comparar: `sorted(a) == sorted(b)`. Tiempo O(n log n), espacio O(n).
# 3) Mejora y trade-off: contar frecuencias con un hashmap: se recorre cada cadena una vez. Trade-off: usa memoria extra O(k) (k = alfabeto distinto) pero evita ordenar.
# 4) Codear hablando: narra cada paso en voz alta mientras escribes y nombra las variables con claridad.
# 5) Big-O final: tiempo O(n), espacio O(k) donde k es el numero de caracteres distintos (O(1) si el alfabeto es fijo).
# Pregunta del entrevistador: ¿Y si el alfabeto es solo a-z? ¿Puedes usar un array de 26 en vez de un dict?

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
