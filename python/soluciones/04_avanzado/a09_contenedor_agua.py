"""a09 - Contenedor con más agua  [dificil]

Tienes una lista `alturas` donde cada elemento es una barra vertical en la posición i. Elige dos barras que, junto con el eje x, formen un contenedor; devuelve el máximo volumen (área) de agua que puede guardar: `min(alturas[i], alturas[j]) * (j - i)`.

Ejemplo:
`contenedor_agua([1,8,6,2,5,4,8,3,7])` -> `49`

En la entrevista te preguntarán: Demuéstrame por qué es correcto mover el puntero de la barra baja (argumento de descarte). ¿Y si quisieras el volumen de agua atrapada tras la lluvia (trapping rain water)? (two pointers con max_izq/max_der, también O(n)).
"""

# EXPLICACIÓN
# 1) Ingenua: todos los pares -> O(n^2) tiempo, O(1) espacio.
# 2) Óptima: dos punteros desde los extremos. Argumento de corrección: con la barra baja h en un extremo, cualquier contenedor que la mantenga y use una barra más cercana tiene menos anchura y altura <= h, así que es peor; por tanto la barra baja ya no puede dar nada mejor y se descarta. Trade-off: ninguno en memoria; solo hay que justificar el descarte.
# 3) Final: O(n) tiempo, O(1) espacio.
#
# PREGUNTA DEL ENTREVISTADOR
# Demuéstrame por qué es correcto mover el puntero de la barra baja (argumento de descarte). ¿Y si quisieras el volumen de agua atrapada tras la lluvia (trapping rain water)? (two pointers con max_izq/max_der, también O(n)).

def contenedor_agua(alturas):
    izq, der = 0, len(alturas) - 1
    mejor = 0
    while izq < der:
        area = min(alturas[izq], alturas[der]) * (der - izq)
        mejor = max(mejor, area)
        if alturas[izq] < alturas[der]:
            izq += 1
        else:
            der -= 1
    return mejor


if __name__ == "__main__":
    assert contenedor_agua([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert contenedor_agua([1, 1]) == 1, "dos barras"
    assert contenedor_agua([]) == 0, "vacío"
    assert contenedor_agua([5]) == 0, "un elemento"
    assert contenedor_agua([0, 0, 0]) == 0, "alturas cero"
    assert contenedor_agua([4, 3, 2, 1, 4]) == 16, "extremos iguales"
    assert contenedor_agua([1, 2, 1]) == 2
    assert contenedor_agua([2, 3, 4, 5, 18, 17, 6]) == 17
    print("OK: todos los tests pasan")
