"""a12 - Sudoku válido  [dificil]

Recibes `tablero`: 9 filas, cada una una cadena de 9 caracteres con dígitos `'1'`-`'9'` o `'.'` para vacío. Devuelve `True` si lo que ya está colocado no viola las reglas: ningún dígito repetido en una fila, columna ni en cada subcuadro 3x3. No hace falta que el sudoku tenga solución, solo que lo puesto sea válido.

Ejemplo: un tablero vacío (`['.........'] * 9`) es válido; si `'5'` aparece dos veces en la misma fila, es inválido.

En la entrevista te preguntarán: ¿Cómo lo resolverías completo (backtracking)? ¿Y para un tablero NxN generalizado? (misma idea con sqrt(N) para las cajas). ¿Cómo codificas filas/columnas/cajas en bitmasks para hacerlo más rápido?
"""

# Pista 1: Necesitas recordar qué dígitos ya viste en cada fila, cada columna y cada caja.
# Pista 2: Usa 27 sets (9 filas, 9 columnas, 9 cajas), o un solo set de tuplas como ('f', i, d).
# Pista 3: El índice de la caja de (f, c) es (f // 3) * 3 + c // 3. Si el dígito ya está en alguno de los tres sets -> False.

def sudoku_valido(tablero):
    # tu código aquí
    pass


if __name__ == "__main__":
    base = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
    assert sudoku_valido(base) is True
    assert sudoku_valido(["........."] * 9) is True, "vacío"
    f = list(base); f[0] = "53..7...5"
    assert sudoku_valido(f) is False, "repetido en fila"
    c = list(base); c[0] = "83..7...."
    assert sudoku_valido(c) is False, "repetido en columna"
    caja = ["........."] * 9
    caja = ["1........", ".1.......", "........."] + ["........."] * 6
    assert sudoku_valido(caja) is False, "repetido solo en la caja 3x3"
    ok = ["1........", "...1.....", "........."] + ["........."] * 6
    assert sudoku_valido(ok) is True, "mismo dígito en cajas distintas, fila y columna distintas"
    print("OK: todos los tests pasan")
