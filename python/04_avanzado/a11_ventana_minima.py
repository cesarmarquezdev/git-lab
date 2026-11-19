"""a11 - Ventana mínima que contiene todos los caracteres  [extra]

Dadas dos cadenas `s` y `t`, devuelve la subcadena más corta de `s` que contenga todos los caracteres de `t` (con multiplicidad: si `t` tiene dos 'a', la ventana necesita al menos dos 'a'). Si no existe, devuelve `""`. Si hay varias del mismo largo mínimo, devuelve la que aparece primero. Si `t` es vacía devuelve `""`.

Ejemplos:
`ventana_minima("ADOBECODEBANC", "ABC")` -> `"BANC"`
`ventana_minima("a", "aa")` -> `""`

En la entrevista te preguntarán: ¿Por qué sigue siendo O(n) si hay un while dentro del for? (izq nunca retrocede). ¿Y si s llega en streaming? (la ventana solo guarda lo necesario, pero hay que bufferizar la ventana actual). Variante: longest repeating character replacement o subcadena sin repetidos más larga con la misma plantilla.
"""

# Pista 1: Idea: ventana [izq, der]. Expande der hasta que la ventana sea válida; luego contrae izq mientras siga siendo válida.
# Pista 2: Lleva un Counter de lo que FALTA (necesidades de t) y un contador `faltan` de caracteres aún no cubiertos.
# Pista 3: Al añadir s[der]: si need[c] > 0, faltan -= 1; luego need[c] -= 1. Con faltan == 0 contrae: mientras need[s[izq]] < 0 sobra ese carácter, quítalo.

def ventana_minima(s, t):
    # tu código aquí
    pass


if __name__ == "__main__":
    assert ventana_minima("ADOBECODEBANC", "ABC") == "BANC"
    assert ventana_minima("a", "a") == "a", "mínimo posible"
    assert ventana_minima("a", "aa") == "", "no alcanza la multiplicidad"
    assert ventana_minima("", "a") == "", "s vacía"
    assert ventana_minima("abc", "") == "", "t vacía"
    assert ventana_minima("aa", "aa") == "aa", "todo s"
    assert ventana_minima("ab", "b") == "b", "al final"
    assert ventana_minima("bba", "ab") == "ba"
    assert ventana_minima("xyz", "abc") == "", "sin coincidencias"
    assert ventana_minima("abcabdebac", "cda") == "cabd", "con ventanas candidatas más largas"
    assert ventana_minima("aaflslflsldkalskaaa", "aaa") == "aaa", "multiplicidad al final"
    print("OK: todos los tests pasan")
