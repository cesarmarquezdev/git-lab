"""a08 - 3Sum sin duplicados  [extra]

Dada una lista `nums`, devuelve todos los tripletes `[a, b, c]` de elementos en posiciones distintas tales que `a + b + c == 0`. El resultado no debe contener tripletes repetidos (el orden de los tripletes y de los números dentro de cada uno no importa).

Ejemplos:
`tres_suma([-1, 0, 1, 2, -1, -4])` -> `[[-1,-1,2],[-1,0,1]]`
`tres_suma([0, 0, 0, 0])` -> `[[0,0,0]]`

En la entrevista te preguntarán: ¿Cómo evitas los duplicados sin usar un set? (lista ordenada y saltar valores iguales consecutivos). ¿Y 4Sum o kSum? (generaliza con recursión: O(n^(k-1))). ¿Y 3Sum closest (más cercano a un objetivo)?
"""

# Pista 1: Fuerza bruta son tres bucles anidados, O(n^3). Fija un número y reduce el problema a Two Sum.
# Pista 2: Ordena la lista. Para cada i usa dos punteros izq=i+1 y der=n-1 buscando suma = -nums[i].
# Pista 3: Para evitar duplicados: salta i si nums[i] == nums[i-1], y tras encontrar un triplete avanza izq mientras repita valor.

def tres_suma(nums):
    # tu código aquí
    pass


if __name__ == "__main__":
    def norm(r):
        return sorted(sorted(t) for t in r)

    r = tres_suma([-1, 0, 1, 2, -1, -4])
    assert norm(r) == [[-1, -1, 2], [-1, 0, 1]]
    assert norm(tres_suma([0, 0, 0, 0])) == [[0, 0, 0]], "ceros: solo un triplete"
    assert tres_suma([]) == [], "vacío"
    assert tres_suma([0]) == [], "un elemento"
    assert tres_suma([1, 2]) == [], "dos elementos"
    assert tres_suma([1, 2, 3]) == [], "sin solución"
    assert norm(tres_suma([-2, 0, 0, 2, 2])) == [[-2, 0, 2]], "sin repetir tripletes"
    r = tres_suma([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6])
    assert len(r) == len({tuple(sorted(t)) for t in r}), "hay tripletes duplicados"
    assert norm(r) == [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]
    print("OK: todos los tests pasan")
