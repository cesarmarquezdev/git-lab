r"""b01 - FizzBuzz (facil)

Escribe `fizzbuzz(n)` que devuelva una lista de strings del 1 al `n` (inclusive):
- múltiplos de 3 -> `"Fizz"`
- múltiplos de 5 -> `"Buzz"`
- múltiplos de 3 y de 5 -> `"FizzBuzz"`
- el resto -> el número como string

Ejemplos:
`fizzbuzz(5)` -> `['1', '2', 'Fizz', '4', 'Buzz']`
`fizzbuzz(15)[-1]` -> `'FizzBuzz'`

Casos borde: `n = 0` devuelve `[]`.
"""

def fizzbuzz(n):
    resultado = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            resultado.append("FizzBuzz")
        elif i % 3 == 0:
            resultado.append("Fizz")
        elif i % 5 == 0:
            resultado.append("Buzz")
        else:
            resultado.append(str(i))
    return resultado

# Explicacion: El orden de los if importa: el caso mas especifico (15) va primero, si no 15 caeria en 'Fizz'. Tiempo O(n), espacio O(n) por la lista. Alternativa sin 'if 15': concatenar 'Fizz' + 'Buzz' y usar `texto or str(i)`, que escala mejor si añaden mas reglas.
# Pregunta del entrevistador: Si ahora piden tambien 7 -> 'Bazz', ¿como lo harias sin explotar en ifs? (Respuesta: lista de reglas (divisor, palabra) y concatenar.)

if __name__ == "__main__":
    assert fizzbuzz(5) == ['1', '2', 'Fizz', '4', 'Buzz']
    assert fizzbuzz(0) == [], "con n = 0"
    assert fizzbuzz(1) == ['1'], "un elemento"
    r = fizzbuzz(15)
    assert len(r) == 15
    assert r[-1] == 'FizzBuzz' and r[2] == 'Fizz' and r[4] == 'Buzz' and r[9] == 'Buzz'
    assert r[14 - 3] == 'Fizz'
    print("OK: todos los tests pasan")
