"""a04 - Agrupar anagramas  [dificil]

Dada una lista de palabras, agrúpalas en listas de anagramas. Devuelve una lista de grupos (el orden de grupos y de palabras dentro de cada grupo no importa).

Ejemplos:
`agrupar_anagramas(["eat","tea","tan","ate","nat","bat"])` -> `[["eat","tea","ate"],["tan","nat"],["bat"]]`
`agrupar_anagramas([""])` -> `[[""]]`

En la entrevista te preguntarán: ¿Cómo lo haces en O(n*k) sin ordenar? (clave = tupla de conteos de 26 letras). ¿Y si el alfabeto es Unicode? (Counter -> frozenset de items, o tupla ordenada de items). ¿Y si hay millones de palabras que no caben en memoria? (particionar por hash de la clave en archivos y agrupar cada partición).
"""

# Pista 1: Dos palabras son anagramas si tienen las mismas letras. ¿Qué 'firma' común podrían compartir?
# Pista 2: Usa como clave del dict las letras ordenadas, pero ojo: las listas no son hashables, convierte a tupla o string.
# Pista 3: defaultdict(list); clave = tuple(sorted(palabra)); al final devuelve list(d.values()).

def agrupar_anagramas(palabras):
    # tu código aquí
    pass


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
