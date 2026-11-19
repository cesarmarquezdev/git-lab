"""a12 - Sudoku válido  [dificil]

Recibes `tablero`: 9 filas, cada una una cadena de 9 caracteres con dígitos `'1'`-`'9'` o `'.'` para vacío. Devuelve `True` si lo que ya está colocado no viola las reglas: ningún dígito repetido en una fila, columna ni en cada subcuadro 3x3. No hace falta que el sudoku tenga solución, solo que lo puesto sea válido.

Ejemplo: un tablero vacío (`['.........'] * 9`) es válido; si `'5'` aparece dos veces en la misma fila, es inválido.

En la entrevista te preguntarán: ¿Cómo lo resolverías completo (backtracking)? ¿Y para un tablero NxN generalizado? (misma idea con sqrt(N) para las cajas). ¿Cómo codificas filas/columnas/cajas en bitmasks para hacerlo más rápido?
"""

# EXPLICACIÓN
# 1) Ingenua: para cada celda comparar con las otras 20 que comparten fila/columna/caja -> O(81 * 20); o validar cada fila, columna y caja con tres pasadas distintas.
# 2) Óptima: una sola pasada con sets por fila, columna y caja; cada celda hace 3 búsquedas O(1). Trade-off: memoria extra (27 sets) a cambio de una única pasada y código claro.
# 3) Final: O(81) = O(1) tiempo y espacio (tablero de tamaño fijo); en general O(n^2) para un tablero n x n.
#
# PREGUNTA DEL ENTREVISTADOR
# ¿Cómo lo resolverías completo (backtracking)? ¿Y para un tablero NxN generalizado? (misma idea con sqrt(N) para las cajas). ¿Cómo codificas filas/columnas/cajas en bitmasks para hacerlo más rápido?

def sudoku_valido(tablero):
    filas = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    cajas = [set() for _ in range(9)]
    for f in range(9):
        for c in range(9):
            d = tablero[f][c]
            if d == ".":
                continue
            b = (f // 3) * 3 + c // 3
            if d in filas[f] or d in cols[c] or d in cajas[b]:
                return False
            filas[f].add(d)
            cols[c].add(d)
            cajas[b].add(d)
    return True


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
