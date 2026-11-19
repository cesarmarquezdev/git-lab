"""a19 - Notación polaca inversa  [dificil]

Evalúa una expresión en notación polaca inversa. `tokens` es una lista de cadenas: enteros (pueden ser negativos, como `"-11"`) u operadores `+ - * /`. La división entre enteros se trunca hacia cero (`7 / -2` -> `-3`, no `-4`). Devuelve el resultado como entero. La expresión siempre es válida.

Ejemplos:
`evaluar_rpn(["2","1","+","3","*"])` -> `9`  (es (2+1)*3)
`evaluar_rpn(["4","13","5","/","+"])` -> `6`

En la entrevista te preguntarán: ¿Cómo convertirías de infija a RPN? (algoritmo shunting-yard con una pila de operadores y precedencias). ¿Qué cambia si hay números muy grandes y a/b en float pierde precisión? (usa división entera con signo manual: q = abs(a)//abs(b) y corrige el signo). ¿Y si la expresión puede ser inválida? (validar tamaño de la pila).
"""

# Pista 1: Recorre los tokens: si es número, empílalo; si es operador, desapila dos operandos y empila el resultado.
# Pista 2: Cuidado con el orden: el primer desapilado es el operando DERECHO. Importa en - y /.
# Pista 3: La división de Python // redondea hacia abajo (-4 para 7//-2). Usa int(a / b) para truncar hacia cero.

def evaluar_rpn(tokens):
    # tu código aquí
    pass


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
