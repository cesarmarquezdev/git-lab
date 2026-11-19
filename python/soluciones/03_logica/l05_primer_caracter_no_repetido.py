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
    conteo = {}
    for c in s:
        conteo[c] = conteo.get(c, 0) + 1
    for c in s:
        if conteo[c] == 1:
            return c
    return None


# Explicacion
# 1) Casos borde a preguntar: cadena vacia, todos repetidos, mayusculas distintas de minusculas, ¿devolver caracter o indice?
# 2) Solucion ingenua: para cada caracter usar `s.count(c)`: O(n^2) tiempo.
# 3) Mejora y trade-off: dos pasadas con hashmap de conteos. Trade-off: O(k) memoria a cambio de pasar de O(n^2) a O(n).
# 4) Codear hablando: narra cada paso en voz alta mientras escribes y nombra las variables con claridad.
# 5) Big-O final: tiempo O(n), espacio O(k) con k caracteres distintos.
# Pregunta del entrevistador: ¿Y si el texto llega como un stream y solo puedes verlo una vez?

if __name__ == "__main__":
    assert primer_no_repetido("leetcode") == "l"
    assert primer_no_repetido("loveleetcode") == "v"
    assert primer_no_repetido("aabb") is None
    assert primer_no_repetido("") is None, "vacia"
    assert primer_no_repetido("z") == "z", "un caracter"
    print("OK: todos los tests pasan")
