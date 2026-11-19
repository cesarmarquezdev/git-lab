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
    # tu codigo aqui
    pass


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
