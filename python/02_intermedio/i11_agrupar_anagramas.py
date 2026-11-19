"""i11 - Agrupar anagramas con defaultdict (media)

Escribe `agrupar_anagramas(palabras)` que reciba una lista de palabras y devuelva una lista de grupos (listas) de palabras que son anagramas entre sí. Los grupos aparecen en el orden en que se vio por primera vez cada grupo, y dentro de cada grupo se respeta el orden original.

Ejemplo:
```
agrupar_anagramas(['eat','tea','tan','ate','nat','bat'])
# [['eat','tea','ate'], ['tan','nat'], ['bat']]
```

Pistas (no mires hasta intentarlo):
Pista 1: Dos palabras son anagramas si tienen las mismas letras ordenadas: `''.join(sorted(p))`.
Pista 2: Esa cadena ordenada sirve como clave de un diccionario.
Pista 3: `defaultdict(list)` evita comprobar si la clave existe antes de `.append`.

Entrevistador: ¿Cómo evitarías el log L de ordenar cada palabra? ¿Qué efecto secundario tiene acceder a una clave inexistente en un defaultdict (crea la clave)?
"""

from collections import defaultdict


def agrupar_anagramas(palabras):
    # tu código aquí
    pass


if __name__ == "__main__":
    assert agrupar_anagramas(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    assert agrupar_anagramas([]) == [], "vacío"
    assert agrupar_anagramas(["a"]) == [["a"]], "un elemento"
    assert agrupar_anagramas(["ab", "cd"]) == [["ab"], ["cd"]], "sin anagramas"
    assert agrupar_anagramas(["ab", "ba", "ab"]) == [["ab", "ba", "ab"]], "repetidas"
    print("OK: todos los tests pasan")
