"""Rotar array k posiciones

Escribe `rotar(nums, k)` que rote la lista `k` posiciones hacia la derecha IN-PLACE (modificando la lista original, sin devolver nada). `k` puede ser mayor que el largo.
Ejemplos:
`[1, 2, 3, 4, 5, 6, 7]` con k=3 queda `[5, 6, 7, 1, 2, 3, 4]`
`[1, 2]` con k=3 queda `[2, 1]`

Pistas:
  1. Si k >= len, solo importa `k % len`.
  2. Piensa en invertir: toda la lista, luego los primeros k, luego el resto.
  3. Escribe una funcion auxiliar `invertir(i, j)` con dos punteros. Tambien vale `nums[:] = nums[-k:] + nums[:-k]` si aceptas O(n) de espacio.
"""

def rotar(nums, k):
    n = len(nums)
    if n == 0:
        return
    k %= n

    def invertir(i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    invertir(0, n - 1)
    invertir(0, k - 1)
    invertir(k, n - 1)


# Explicacion
# 1) Casos borde a preguntar: lista vacia, k = 0, k mayor que el largo, k negativo, ¿in-place?, ¿derecha o izquierda?
# 2) Solucion ingenua: rotar de a una posicion k veces (pop + insert): O(n*k) tiempo.
# 3) Mejora y trade-off: con slicing `nums[:] = nums[-k:] + nums[:-k]`: O(n) tiempo pero O(n) espacio. Con triple reversa (todo, primeros k, resto): O(n) tiempo y O(1) espacio. Trade-off: la reversa es menos obvia pero no usa memoria extra.
# 4) Codear hablando: narra cada paso en voz alta mientras escribes y nombra las variables con claridad.
# 5) Big-O final: tiempo O(n), espacio O(1) con triple reversa.
# Pregunta del entrevistador: ¿Por que funciona la triple reversa? ¿Y si k es negativo?

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7]
    r = rotar(a, 3)
    assert a == [5, 6, 7, 1, 2, 3, 4]
    assert r is None, "in-place: no devuelve nada"
    b = [1, 2]
    rotar(b, 3)
    assert b == [2, 1], "k mayor que el largo"
    c = []
    rotar(c, 5)
    assert c == [], "vacia"
    d = [9]
    rotar(d, 4)
    assert d == [9], "un elemento"
    e = [1, 2, 3]
    rotar(e, 0)
    assert e == [1, 2, 3], "k = 0"
    f = [1, 2, 3]
    rotar(f, 3)
    assert f == [1, 2, 3], "k = largo"
    print("OK: todos los tests pasan")
