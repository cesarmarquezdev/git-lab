"""Parentesis balanceados

Escribe `es_balanceado(s)` que devuelva True si los parentesis `()`, corchetes `[]` y llaves `{}` de la cadena estan bien abiertos y cerrados y en el orden correcto. Ignora cualquier otro caracter.
Ejemplos:
`es_balanceado("()[]{}")` -> True
`es_balanceado("([)]")` -> False
`es_balanceado("{[()]}")` -> True

Pistas:
  1. Lo ultimo que se abre debe ser lo primero que se cierre: eso es LIFO.
  2. Al ver un simbolo de apertura, apilalo; al ver uno de cierre, compara con el tope.
  3. Al final la pila debe estar vacia. Usa un dict `{")": "(", ...}` para emparejar.
"""

def es_balanceado(s):
    # tu codigo aqui
    pass


if __name__ == "__main__":
    assert es_balanceado("()[]{}") is True
    assert es_balanceado("([)]") is False
    assert es_balanceado("{[()]}") is True
    assert es_balanceado("") is True, "vacia"
    assert es_balanceado("(") is False, "un solo simbolo abierto"
    assert es_balanceado(")") is False, "cierre sin apertura"
    assert es_balanceado("((") is False, "sobran aperturas"
    assert es_balanceado("a(b)c") is True, "ignora otros caracteres"
    print("OK: todos los tests pasan")
