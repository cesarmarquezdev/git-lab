"""a04 - Agrupar anagramas  [dificil]

Dada una lista de palabras, agrúpalas en listas de anagramas. Devuelve una lista de grupos (el orden de grupos y de palabras dentro de cada grupo no importa).

Ejemplos:
`agrupar_anagramas(["eat","tea","tan","ate","nat","bat"])` -> `[["eat","tea","ate"],["tan","nat"],["bat"]]`
`agrupar_anagramas([""])` -> `[[""]]`

En la entrevista te preguntarán: ¿Cómo lo haces en O(n*k) sin ordenar? (clave = tupla de conteos de 26 letras). ¿Y si el alfabeto es Unicode? (Counter -> frozenset de items, o tupla ordenada de items). ¿Y si hay millones de palabras que no caben en memoria? (particionar por hash de la clave en archivos y agrupar cada partición).
"""

# EXPLICACIÓN
# 1) Ingenua: comparar cada palabra con todas las demás (cada comparación ordena o cuenta) -> O(n^2 * k log k).
# 2) Mejor: una clave canónica por palabra. Ordenar las letras da la misma clave a todos los anagramas -> O(n * k log k), con k = longitud máxima. Alternativa: clave = tupla de 26 conteos -> O(n * k) pero más verbosa. Trade-off: más memoria (el dict) a cambio de pasar de cuadrático a lineal en n.
# 3) Final: O(n * k log k) tiempo, O(n * k) espacio.
#
# PREGUNTA DEL ENTREVISTADOR
# ¿Cómo lo haces en O(n*k) sin ordenar? (clave = tupla de conteos de 26 letras). ¿Y si el alfabeto es Unicode? (Counter -> frozenset de items, o tupla ordenada de items). ¿Y si hay millones de palabras que no caben en memoria? (particionar por hash de la clave en archivos y agrupar cada partición).

from collections import defaultdict

def agrupar_anagramas(palabras):
    grupos = defaultdict(list)
    for p in palabras:
        grupos[tuple(sorted(p))].append(p)
    return list(grupos.values())


if __name__ == "__main__":
    def norm(r):
        return sorted(sorted(g) for g in r)

    assert norm(agrupar_anagramas(["eat", "tea", "tan", "ate", "nat", "bat"])) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    assert norm(agrupar_anagramas([""])) == [[""]], "cadena vacía"
    assert norm(agrupar_anagramas([])) == [], "lista vacía"
    assert norm(agrupar_anagramas(["a"])) == [["a"]], "un elemento"
    assert norm(agrupar_anagramas(["ab", "ba", "ab"])) == [["ab", "ab", "ba"]], "duplicados se conservan"
    assert norm(agrupar_anagramas(["abc", "def"])) == [["abc"], ["def"]], "sin anagramas"
    assert norm(agrupar_anagramas(["", "", "a"])) == [["", ""], ["a"]]
    print("OK: todos los tests pasan")
