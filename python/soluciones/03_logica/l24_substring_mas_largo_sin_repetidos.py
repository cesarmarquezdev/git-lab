"""Substring mas largo sin repetidos

Escribe `longitud_substring_unico(s)` que devuelva la longitud del substring (caracteres contiguos) mas largo que no repite ningun caracter.
Ejemplos:
`longitud_substring_unico("abcabcbb")` -> 3 ("abc")
`longitud_substring_unico("bbbbb")` -> 1
`longitud_substring_unico("pwwkew")` -> 3 ("wke")

Pistas:
  1. Una ventana [izq, der] que siempre contiene caracteres unicos.
  2. Si el nuevo caracter ya esta en la ventana, mueve `izq` hasta pasar su aparicion anterior.
  3. Guarda en un dict la ultima posicion de cada caracter; `izq = max(izq, ultima[c] + 1)`.
"""

def longitud_substring_unico(s):
    ultima = {}
    izq = 0
    mejor = 0
    for der, c in enumerate(s):
        if c in ultima and ultima[c] >= izq:
            izq = ultima[c] + 1
        ultima[c] = der
        mejor = max(mejor, der - izq + 1)
    return mejor


# Explicacion
# 1) Casos borde a preguntar: cadena vacia, un caracter, todos iguales, todos distintos, ¿distingue mayusculas?, ¿espacios?
# 2) Solucion ingenua: probar todos los substrings y verificar si tienen repetidos: O(n^3) (o O(n^2) con early break).
# 3) Mejora y trade-off: sliding window con dict de ultima posicion: `der` avanza siempre y `izq` salta justo despues de la repeticion. Trade-off: O(k) memoria extra por el dict. Cuidado con 'abba': `izq` nunca debe retroceder, de ahi `ultima[c] >= izq`.
# 4) Codear hablando: narra cada paso en voz alta mientras escribes y nombra las variables con claridad.
# 5) Big-O final: tiempo O(n), espacio O(min(n, k)) con k el tamano del alfabeto.
# Pregunta del entrevistador: ¿Por que cada caracter se visita solo una vez aunque haya un `izq` y un `der`? ¿Y si pides el substring y no solo la longitud?

if __name__ == "__main__":
    assert longitud_substring_unico("abcabcbb") == 3
    assert longitud_substring_unico("bbbbb") == 1
    assert longitud_substring_unico("pwwkew") == 3
    assert longitud_substring_unico("") == 0, "vacia"
    assert longitud_substring_unico("a") == 1, "un caracter"
    assert longitud_substring_unico("abcdef") == 6, "todos distintos"
    assert longitud_substring_unico("abba") == 2, "el puntero izq nunca retrocede"
    assert longitud_substring_unico("dvdf") == 3
    assert longitud_substring_unico("a b a") == 3, "el espacio cuenta como caracter"
    print("OK: todos los tests pasan")
