"""Binary search a mano + primer indice

Implementa dos funciones sobre una lista ordenada ascendente:
- `busqueda_binaria(nums, objetivo)` -> un indice donde este el valor, o -1. Iterativa, sin usar `bisect` ni `.index`.
- `primer_indice(nums, objetivo)` -> el indice de la PRIMERA aparicion del valor cuando hay repetidos, o -1.
Ejemplos:
`busqueda_binaria([1, 3, 5, 7], 5)` -> 2
`primer_indice([1, 2, 2, 2, 3], 2)` -> 1

Pistas:
  1. Mantén `izq` y `der`; mira el elemento del medio `medio = (izq + der) // 2`.
  2. Si el medio es menor que el objetivo, descarta la mitad izquierda; si es mayor, la derecha.
  3. Para el primero: cuando lo encuentres guarda `medio` como respuesta y sigue buscando a la izquierda (`der = medio - 1`).
"""

def busqueda_binaria(nums, objetivo):
    izq, der = 0, len(nums) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if nums[medio] == objetivo:
            return medio
        if nums[medio] < objetivo:
            izq = medio + 1
        else:
            der = medio - 1
    return -1


def primer_indice(nums, objetivo):
    izq, der = 0, len(nums) - 1
    respuesta = -1
    while izq <= der:
        medio = (izq + der) // 2
        if nums[medio] == objetivo:
            respuesta = medio
            der = medio - 1
        elif nums[medio] < objetivo:
            izq = medio + 1
        else:
            der = medio - 1
    return respuesta


# Explicacion
# 1) Casos borde a preguntar: lista vacia, un elemento, valor en los extremos, valor ausente, repetidos, ¿esta ordenada y en que sentido?
# 2) Solucion ingenua: busqueda lineal recorriendo la lista: O(n) tiempo.
# 3) Mejora y trade-off: binary search: cada comparacion descarta la mitad. Trade-off: exige datos ordenados (ordenar cuesta O(n log n), no vale la pena para una sola busqueda). Para el primer indice no se corta al encontrarlo: se sigue hacia la izquierda.
# 4) Codear hablando: usa `izq <= der` y actualiza con `medio + 1` / `medio - 1` para evitar bucles infinitos. En otros lenguajes `(izq + der)` puede desbordar; en Python no.
# 5) Big-O final: tiempo O(log n), espacio O(1) en la version iterativa (la recursiva usaria O(log n) de pila).
# Pregunta del entrevistador: ¿Por que `izq <= der` y no `<`? ¿Que pasa con el overflow de `(izq+der)//2` en otros lenguajes?

if __name__ == "__main__":
    assert busqueda_binaria([1, 3, 5, 7], 5) == 2
    assert busqueda_binaria([1, 3, 5, 7], 1) == 0, "primer elemento"
    assert busqueda_binaria([1, 3, 5, 7], 7) == 3, "ultimo elemento"
    assert busqueda_binaria([1, 3, 5, 7], 4) == -1, "no esta"
    assert busqueda_binaria([], 1) == -1, "vacia"
    assert busqueda_binaria([9], 9) == 0, "un elemento"
    assert busqueda_binaria([9], 3) == -1
    assert busqueda_binaria(list(range(0, 1000, 2)), 998) == 499
    assert primer_indice([1, 2, 2, 2, 3], 2) == 1
    assert primer_indice([2, 2, 2, 2], 2) == 0, "todos iguales"
    assert primer_indice([1, 2, 3], 3) == 2
    assert primer_indice([1, 2, 3], 5) == -1
    assert primer_indice([], 1) == -1
    assert primer_indice([1, 1, 2, 2, 2, 2], 2) == 2
    print("OK: todos los tests pasan")
