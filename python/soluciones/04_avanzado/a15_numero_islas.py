"""a15 - Número de islas  [dificil]

`grilla` es una lista de cadenas del mismo largo con `'1'` (tierra) y `'0'` (agua). Una isla es un grupo de `'1'` conectados horizontal o verticalmente (NO en diagonal). Devuelve cuántas islas hay. No modifiques la grilla de entrada.

Ejemplo:
`numero_islas(["11000","11000","00100","00011"])` -> `3`

En la entrevista te preguntarán: ¿Y si la grilla es gigante y no cabe en memoria? (procesar por franjas con Union-Find, fusionando islas en los bordes entre franjas). ¿Y si las celdas cambian dinámicamente (Number of Islands II)? (Union-Find incremental). ¿Qué pasa con la recursión en Python?
"""

# EXPLICACIÓN
# 1) Ingenua: no hay una versión 'fuerza bruta' razonable; la idea base ya es contar componentes conexas: recorrer la grilla y, en cada tierra nueva, explorar su isla.
# 2) DFS recursivo: simple y elegante pero con la recursión de Python (~1000 niveles) falla en islas grandes. DFS/BFS iterativo con pila o cola: mismo coste, sin límite de recursión. Se puede ahorrar el set `visitados` mutando la grilla (poner '0'), a cambio de destruir la entrada: trade-off típico que debes mencionar.
# 3) Final: O(filas*cols) tiempo (cada celda se mete una sola vez), O(filas*cols) espacio por visitados y la pila.
#
# PREGUNTA DEL ENTREVISTADOR
# ¿Y si la grilla es gigante y no cabe en memoria? (procesar por franjas con Union-Find, fusionando islas en los bordes entre franjas). ¿Y si las celdas cambian dinámicamente (Number of Islands II)? (Union-Find incremental). ¿Qué pasa con la recursión en Python?

def numero_islas(grilla):
    if not grilla:
        return 0
    filas, cols = len(grilla), len(grilla[0])
    visitados = set()
    islas = 0
    for f in range(filas):
        for c in range(cols):
            if grilla[f][c] == "1" and (f, c) not in visitados:
                islas += 1
                visitados.add((f, c))
                pila = [(f, c)]
                while pila:                       # DFS iterativo
                    x, y = pila.pop()
                    for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                        if (0 <= nx < filas and 0 <= ny < cols
                                and grilla[nx][ny] == "1" and (nx, ny) not in visitados):
                            visitados.add((nx, ny))
                            pila.append((nx, ny))
    return islas


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
