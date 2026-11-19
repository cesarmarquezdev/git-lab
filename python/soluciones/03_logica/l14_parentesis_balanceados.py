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
    pares = {")": "(", "]": "[", "}": "{"}
    pila = []
    for c in s:
        if c in pares.values():
            pila.append(c)
        elif c in pares:
            if not pila or pila.pop() != pares[c]:
                return False
    return not pila


# Explicacion
# 1) Casos borde a preguntar: cadena vacia (¿balanceada?), un solo simbolo, cierre sin apertura, sobran aperturas, otros caracteres.
# 2) Solucion ingenua: borrar repetidamente pares adyacentes `()`, `[]`, `{}` hasta que no cambie: O(n^2) en el peor caso.
# 3) Mejora y trade-off: una pila: apilar aperturas y validar cada cierre contra el tope. Trade-off: O(n) de memoria en el peor caso (todo aperturas) a cambio de una sola pasada.
# 4) Codear hablando: narra cada paso en voz alta mientras escribes y nombra las variables con claridad.
# 5) Big-O final: tiempo O(n), espacio O(n).
# Pregunta del entrevistador: ¿Y si solo hubiera un tipo de parentesis? ¿Puedes hacerlo con O(1) de espacio?

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
