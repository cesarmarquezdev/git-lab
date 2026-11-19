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
    # tu codigo aqui
    pass


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
