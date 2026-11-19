"""a19 - Notación polaca inversa  [dificil]

Evalúa una expresión en notación polaca inversa. `tokens` es una lista de cadenas: enteros (pueden ser negativos, como `"-11"`) u operadores `+ - * /`. La división entre enteros se trunca hacia cero (`7 / -2` -> `-3`, no `-4`). Devuelve el resultado como entero. La expresión siempre es válida.

Ejemplos:
`evaluar_rpn(["2","1","+","3","*"])` -> `9`  (es (2+1)*3)
`evaluar_rpn(["4","13","5","/","+"])` -> `6`

En la entrevista te preguntarán: ¿Cómo convertirías de infija a RPN? (algoritmo shunting-yard con una pila de operadores y precedencias). ¿Qué cambia si hay números muy grandes y a/b en float pierde precisión? (usa división entera con signo manual: q = abs(a)//abs(b) y corrige el signo). ¿Y si la expresión puede ser inválida? (validar tamaño de la pila).
"""

# EXPLICACIÓN
# 1) Ingenua: convertir a notación infija con paréntesis y evaluar de forma recursiva buscando el operador de menor precedencia -> más complejo y O(n^2) por los re-escaneos.
# 2) Óptima: la RPN está diseñada para una pila. Cada operador consume los dos últimos valores calculados, así que no hace falta precedencia ni paréntesis. Trade-off: la pila usa O(n) de memoria en el peor caso (muchos números antes de los operadores).
# 3) Final: O(n) tiempo, O(n) espacio. Trampas: orden a-b en operadores no conmutativos y truncado hacia cero (int(a / b)) en vez de //.
#
# PREGUNTA DEL ENTREVISTADOR
# ¿Cómo convertirías de infija a RPN? (algoritmo shunting-yard con una pila de operadores y precedencias). ¿Qué cambia si hay números muy grandes y a/b en float pierde precisión? (usa división entera con signo manual: q = abs(a)//abs(b) y corrige el signo). ¿Y si la expresión puede ser inválida? (validar tamaño de la pila).

def evaluar_rpn(tokens):
    pila = []
    for t in tokens:
        if t in ("+", "-", "*", "/"):
            b = pila.pop()          # operando derecho
            a = pila.pop()          # operando izquierdo
            if t == "+":
                pila.append(a + b)
            elif t == "-":
                pila.append(a - b)
            elif t == "*":
                pila.append(a * b)
            else:
                pila.append(int(a / b))   # trunca hacia cero
        else:
            pila.append(int(t))
    return pila[0]


if __name__ == "__main__":
    assert evaluar_rpn(["2", "1", "+", "3", "*"]) == 9
    assert evaluar_rpn(["4", "13", "5", "/", "+"]) == 6
    assert evaluar_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
    assert evaluar_rpn(["3"]) == 3, "un solo número"
    assert evaluar_rpn(["-3"]) == -3, "un solo negativo"
    assert evaluar_rpn(["7", "-2", "/"]) == -3, "trunca hacia cero (no hacia -inf)"
    assert evaluar_rpn(["-7", "2", "/"]) == -3, "trunca hacia cero con numerador negativo"
    assert evaluar_rpn(["5", "3", "-"]) == 2, "orden de operandos en la resta"
    assert evaluar_rpn(["0", "5", "*"]) == 0
    assert isinstance(evaluar_rpn(["6", "3", "/"]), int), "debe ser int, no float"
    print("OK: todos los tests pasan")
