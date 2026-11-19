"""i13 - copy vs deepcopy: clonar una matriz (media)

Escribe `clonar_matriz(m)` que devuelva una copia de una matriz (lista de listas) **sin compartir ninguna fila** con la original: modificar la copia no debe afectar a la original y viceversa. No modifiques la original. Una matriz vacía devuelve `[]`.

Ejemplo:
```
m = [[1,2],[3,4]]; c = clonar_matriz(m); c[0][0] = 99; m[0][0]  # 1
```

Pistas (no mires hasta intentarlo):
Pista 1: `list(m)`, `m[:]` y `copy.copy(m)` son copias superficiales: las filas siguen siendo las mismas.
Pista 2: Copia cada fila: `[fila[:] for fila in m]`.
Pista 3: Para estructuras con anidación arbitraria usa `copy.deepcopy(m)`.

Entrevistador: ¿Qué hace `[[0]*3]*3` y por qué es un bug? ¿Cuándo `deepcopy` puede ser problemático (objetos no copiables, rendimiento, ciclos)?
"""

import copy


def clonar_matriz(m):
    # tu código aquí
    pass


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
