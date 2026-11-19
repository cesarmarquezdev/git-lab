"""a11 - Ventana mínima que contiene todos los caracteres  [extra]

Dadas dos cadenas `s` y `t`, devuelve la subcadena más corta de `s` que contenga todos los caracteres de `t` (con multiplicidad: si `t` tiene dos 'a', la ventana necesita al menos dos 'a'). Si no existe, devuelve `""`. Si hay varias del mismo largo mínimo, devuelve la que aparece primero. Si `t` es vacía devuelve `""`.

Ejemplos:
`ventana_minima("ADOBECODEBANC", "ABC")` -> `"BANC"`
`ventana_minima("a", "aa")` -> `""`

En la entrevista te preguntarán: ¿Por qué sigue siendo O(n) si hay un while dentro del for? (izq nunca retrocede). ¿Y si s llega en streaming? (la ventana solo guarda lo necesario, pero hay que bufferizar la ventana actual). Variante: longest repeating character replacement o subcadena sin repetidos más larga con la misma plantilla.
"""

# EXPLICACIÓN
# 1) Ingenua: probar todas las subcadenas y comprobar cada una con un Counter -> O(n^2 * m) o O(n^3).
# 2) Óptima: ventana deslizante. Expandimos el borde derecho hasta cubrir t y contraemos el izquierdo mientras siga cubriendo; cada puntero avanza como mucho n veces. `need` puede ir negativo: significa 'tengo caracteres de sobra', y `faltan` evita comparar dos Counters en cada paso (que costaría O(alfabeto)). Trade-off: lógica de invariantes delicada a cambio de pasar de polinómico a lineal.
# 3) Final: O(n + m) tiempo, O(alfabeto) espacio.
#
# PREGUNTA DEL ENTREVISTADOR
# ¿Por qué sigue siendo O(n) si hay un while dentro del for? (izq nunca retrocede). ¿Y si s llega en streaming? (la ventana solo guarda lo necesario, pero hay que bufferizar la ventana actual). Variante: longest repeating character replacement o subcadena sin repetidos más larga con la misma plantilla.

from collections import Counter

def ventana_minima(s, t):
    if not s or not t:
        return ""
    need = Counter(t)
    faltan = len(t)
    izq = 0
    mejor_ini, mejor_len = 0, float("inf")
    for der, c in enumerate(s):
        if need[c] > 0:
            faltan -= 1
        need[c] -= 1
        if faltan == 0:
            while need[s[izq]] < 0:          # carácter sobrante: se puede soltar
                need[s[izq]] += 1
                izq += 1
            if der - izq + 1 < mejor_len:
                mejor_ini, mejor_len = izq, der - izq + 1
            need[s[izq]] += 1                # rompemos la validez para seguir buscando
            faltan += 1
            izq += 1
    return "" if mejor_len == float("inf") else s[mejor_ini:mejor_ini + mejor_len]


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
