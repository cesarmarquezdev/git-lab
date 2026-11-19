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
    # tu codigo aqui
    pass


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
