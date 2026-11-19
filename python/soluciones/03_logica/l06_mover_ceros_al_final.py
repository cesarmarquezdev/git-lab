"""Mover ceros al final

Escribe `mover_ceros(nums)` que mueva todos los 0 al final de la lista modificandola in-place (sin crear otra lista), conservando el orden relativo de los demas. No devuelve nada.
Ejemplo: `[0, 1, 0, 3, 12]` queda `[1, 3, 12, 0, 0]`.

Pistas:
  1. Un puntero escribe, otro lee.
  2. Recorre con `i`; cada valor distinto de 0 se coloca en la posicion `escribir`.
  3. Intercambia `nums[escribir], nums[i] = nums[i], nums[escribir]` y avanza `escribir`.
"""

def mover_ceros(nums):
    escribir = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[escribir], nums[i] = nums[i], nums[escribir]
            escribir += 1


# Explicacion
# 1) Casos borde a preguntar: lista vacia, todos ceros, sin ceros, ¿hay que conservar el orden?, ¿in-place obligatorio?
# 2) Solucion ingenua: crear una lista con los no-ceros y rellenar con ceros: O(n) tiempo pero O(n) espacio.
# 3) Mejora y trade-off: two pointers (lector y escritor) con swap in-place. Trade-off: modifica la entrada, pero usa memoria constante.
# 4) Codear hablando: narra cada paso en voz alta mientras escribes y nombra las variables con claridad.
# 5) Big-O final: tiempo O(n), espacio O(1).
# Pregunta del entrevistador: ¿Puedes minimizar el numero de escrituras cuando hay pocos ceros?

if __name__ == "__main__":
    a = [0, 1, 0, 3, 12]
    r = mover_ceros(a)
    assert a == [1, 3, 12, 0, 0]
    assert r is None, "debe ser in-place y no devolver nada"
    b = []
    mover_ceros(b)
    assert b == [], "vacia"
    c = [0]
    mover_ceros(c)
    assert c == [0], "un elemento"
    d = [0, 0, 0]
    mover_ceros(d)
    assert d == [0, 0, 0]
    e = [1, 2, 3]
    mover_ceros(e)
    assert e == [1, 2, 3], "sin ceros"
    f = [4, 0, 5]
    mover_ceros(f)
    assert f == [4, 5, 0]
    print("OK: todos los tests pasan")
