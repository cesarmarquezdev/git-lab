"""a08 - 3Sum sin duplicados  [extra]

Dada una lista `nums`, devuelve todos los tripletes `[a, b, c]` de elementos en posiciones distintas tales que `a + b + c == 0`. El resultado no debe contener tripletes repetidos (el orden de los tripletes y de los números dentro de cada uno no importa).

Ejemplos:
`tres_suma([-1, 0, 1, 2, -1, -4])` -> `[[-1,-1,2],[-1,0,1]]`
`tres_suma([0, 0, 0, 0])` -> `[[0,0,0]]`

En la entrevista te preguntarán: ¿Cómo evitas los duplicados sin usar un set? (lista ordenada y saltar valores iguales consecutivos). ¿Y 4Sum o kSum? (generaliza con recursión: O(n^(k-1))). ¿Y 3Sum closest (más cercano a un objetivo)?
"""

# EXPLICACIÓN
# 1) Ingenua: tres bucles, y un set de tuplas ordenadas para quitar repetidos -> O(n^3).
# 2) Mejor: ordenar y fijar un elemento; el resto es Two Sum con dos punteros sobre una lista ordenada (suma baja -> mueve izq, suma alta -> mueve der). Un hashmap por cada i también da O(n^2) pero el manejo de duplicados es más incómodo. Trade-off: el sort permite O(1) espacio y deduplicar saltando valores iguales.
# 3) Final: O(n^2) tiempo (el sort O(n log n) queda dominado), O(1) espacio extra sin contar la salida (O(log n) o O(n) por el sort).
#
# PREGUNTA DEL ENTREVISTADOR
# ¿Cómo evitas los duplicados sin usar un set? (lista ordenada y saltar valores iguales consecutivos). ¿Y 4Sum o kSum? (generaliza con recursión: O(n^(k-1))). ¿Y 3Sum closest (más cercano a un objetivo)?

def tres_suma(nums):
    nums = sorted(nums)
    res = []
    n = len(nums)
    for i in range(n - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue                      # mismo valor fijo: ya probado
        izq, der = i + 1, n - 1
        while izq < der:
            s = nums[i] + nums[izq] + nums[der]
            if s < 0:
                izq += 1
            elif s > 0:
                der -= 1
            else:
                res.append([nums[i], nums[izq], nums[der]])
                izq += 1
                while izq < der and nums[izq] == nums[izq - 1]:
                    izq += 1              # saltar duplicados del segundo número
    return res


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
