"""a15 - Número de islas  [dificil]

`grilla` es una lista de cadenas del mismo largo con `'1'` (tierra) y `'0'` (agua). Una isla es un grupo de `'1'` conectados horizontal o verticalmente (NO en diagonal). Devuelve cuántas islas hay. No modifiques la grilla de entrada.

Ejemplo:
`numero_islas(["11000","11000","00100","00011"])` -> `3`

En la entrevista te preguntarán: ¿Y si la grilla es gigante y no cabe en memoria? (procesar por franjas con Union-Find, fusionando islas en los bordes entre franjas). ¿Y si las celdas cambian dinámicamente (Number of Islands II)? (Union-Find incremental). ¿Qué pasa con la recursión en Python?
"""

# Pista 1: Recorre cada celda; al encontrar un '1' no visitado, has encontrado una isla nueva.
# Pista 2: Desde esa celda 'inunda' (DFS o BFS) todas las celdas de tierra conectadas marcándolas como visitadas.
# Pista 3: Usa un set `visitados` y una pila/cola explícita en lugar de recursión: una isla de 40.000 celdas desborda la recursión de Python (límite ~1000).

def numero_islas(grilla):
    # tu código aquí
    pass


if __name__ == "__main__":
    assert numero_islas(["11000", "11000", "00100", "00011"]) == 3
    assert numero_islas([]) == 0, "grilla vacía"
    assert numero_islas(["0"]) == 0, "solo agua"
    assert numero_islas(["1"]) == 1, "una celda de tierra"
    assert numero_islas(["10", "01"]) == 2, "la diagonal no conecta"
    assert numero_islas(["111", "010", "111"]) == 1, "isla en forma de H"
    assert numero_islas(["101", "000", "101"]) == 4, "cuatro esquinas"
    assert numero_islas(["11111", "10001", "10101", "10001", "11111"]) == 2, "anillo con isla dentro"
    assert numero_islas(["1" * 200] * 200) == 1, "grilla grande: no debe desbordar la recursión"
    g = ["11", "00"]
    numero_islas(g)
    assert g == ["11", "00"], "no debe modificar la entrada"
    print("OK: todos los tests pasan")
