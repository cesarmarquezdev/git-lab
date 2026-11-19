"""Palindromo

Escribe `es_palindromo(s)` que devuelva True si el texto se lee igual al derecho y al reves, ignorando mayusculas, espacios y signos de puntuacion (solo cuentan letras y digitos).
Usa dos punteros (uno al inicio, otro al final), sin crear la cadena invertida.
Ejemplos:
`es_palindromo("Anita lava la tina")` -> True
`es_palindromo("A man, a plan, a canal: Panama")` -> True
`es_palindromo("hola")` -> False

Pistas:
  1. Compara el caracter de la izquierda con el de la derecha y acercalos.
  2. Antes de comparar, salta los caracteres que no sean `c.isalnum()`.
  3. Usa `i, j = 0, len(s) - 1` y `while i < j:`; compara con `.lower()`.
"""

def es_palindromo(s):
    i, j = 0, len(s) - 1
    while i < j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1
    return True


# Explicacion
# 1) Casos borde a preguntar: cadena vacia, un solo caracter, solo signos, mayusculas mezcladas, ¿digitos cuentan? ¿unicode?
# 2) Solucion ingenua: limpiar el texto, crear `limpio[::-1]` y comparar. Tiempo O(n), espacio O(n).
# 3) Mejora y trade-off: dos punteros que se acercan desde los extremos saltando signos: mismo tiempo O(n) pero sin copias. Trade-off: codigo un poco mas largo a cambio de memoria constante.
# 4) Codear hablando: narra cada paso en voz alta mientras escribes y nombra las variables con claridad.
# 5) Big-O final: tiempo O(n), espacio O(1). La version ingenua es O(n) en espacio.
# Pregunta del entrevistador: ¿Como lo harias sin usar `isalnum` ni `lower`, o con un stream de caracteres que no cabe en memoria?

if __name__ == "__main__":
    assert es_palindromo("Anita lava la tina") is True
    assert es_palindromo("A man, a plan, a canal: Panama") is True
    assert es_palindromo("hola") is False
    assert es_palindromo("") is True, "cadena vacia"
    assert es_palindromo("a") is True, "un caracter"
    assert es_palindromo(".,!") is True, "solo signos"
    assert es_palindromo("ab") is False
    assert es_palindromo("0P") is False
    print("OK: todos los tests pasan")
