"""i13 - copy vs deepcopy: clonar una matriz (SOLUCIÓN)
"""

import copy


def clonar_matriz(m):
    return copy.deepcopy(m)
    # equivalente para una matriz de 2 niveles: [fila[:] for fila in m]

# Explicación:
# Copia superficial (`copy.copy`, `list(m)`, `m[:]`) duplica solo el contenedor exterior; los objetos internos se comparten por referencia. `deepcopy` copia recursivamente (y maneja ciclos con un memo). Para solo 2 niveles de números, `[f[:] for f in m]` es O(n*m) y más rápida que deepcopy. Trampa relacionada: `[[0]*3]*3` crea 3 referencias a la MISMA fila; usa `[[0]*3 for _ in range(3)]`.
# Entrevistador: ¿Qué hace `[[0]*3]*3` y por qué es un bug? ¿Cuándo `deepcopy` puede ser problemático (objetos no copiables, rendimiento, ciclos)?


if __name__ == "__main__":
    m = [[1, 2], [3, 4]]
    c = clonar_matriz(m)
    assert c == m, "mismo contenido"
    assert c is not m, "lista exterior distinta"
    assert all(cf is not mf for cf, mf in zip(c, m)), "filas distintas"
    c[0][0] = 99
    assert m[0][0] == 1, "modificar la copia no afecta la original"
    m[1][1] = -1
    assert c[1][1] == 4, "y viceversa"
    assert clonar_matriz([]) == [], "vacía"
    assert clonar_matriz([[]]) == [[]], "una fila vacía"
    un = [[7]]
    cu = clonar_matriz(un)
    cu[0].append(8)
    assert un == [[7]], "un elemento"
    sup = list(m)
    assert sup[0] is m[0], "(comprobación: la copia superficial sí comparte filas)"
    print("OK: todos los tests pasan")
