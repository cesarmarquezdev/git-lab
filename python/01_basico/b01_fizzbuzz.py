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

# Pista 1: Recorre `range(1, n + 1)`.
# Pista 2: Comprueba primero el caso de 15 (o `i % 3 == 0 and i % 5 == 0`).
# Pista 3: Alternativa: construye el texto con `texto = ''`, añade 'Fizz' si %3, 'Buzz' si %5, y si queda vacío usa `str(i)`.

def fizzbuzz(n):
    # tu código aquí
    pass

if __name__ == "__main__":
    assert fizzbuzz(5) == ['1', '2', 'Fizz', '4', 'Buzz']
    assert fizzbuzz(0) == [], "con n = 0"
    assert fizzbuzz(1) == ['1'], "un elemento"
    r = fizzbuzz(15)
    assert len(r) == 15
    assert r[-1] == 'FizzBuzz' and r[2] == 'Fizz' and r[4] == 'Buzz' and r[9] == 'Buzz'
    assert r[14 - 3] == 'Fizz'
    print("OK: todos los tests pasan")
