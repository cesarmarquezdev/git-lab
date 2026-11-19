"""i11 - Agrupar anagramas con defaultdict (SOLUCIÓN)
"""

from collections import defaultdict


def agrupar_anagramas(palabras):
    grupos = defaultdict(list)
    for palabra in palabras:
        grupos["".join(sorted(palabra))].append(palabra)
    return list(grupos.values())

# Explicación:
# `defaultdict(list)` crea la lista vacía automáticamente al acceder a una clave ausente. Los dicts conservan el orden de inserción (3.7+), así que `values()` ya respeta el orden de primera aparición. Tiempo O(n * L log L) con L = longitud media de palabra; espacio O(n*L). Alternativa en O(n*L): clave = tupla de 26 conteos en vez de ordenar.
# Entrevistador: ¿Cómo evitarías el log L de ordenar cada palabra? ¿Qué efecto secundario tiene acceder a una clave inexistente en un defaultdict (crea la clave)?


if __name__ == "__main__":
    assert agrupar_anagramas(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    assert agrupar_anagramas([]) == [], "vacío"
    assert agrupar_anagramas(["a"]) == [["a"]], "un elemento"
    assert agrupar_anagramas(["ab", "cd"]) == [["ab"], ["cd"]], "sin anagramas"
    assert agrupar_anagramas(["ab", "ba", "ab"]) == [["ab", "ba", "ab"]], "repetidas"
    print("OK: todos los tests pasan")
