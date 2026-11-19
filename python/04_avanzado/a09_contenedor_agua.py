"""a09 - Contenedor con más agua  [dificil]

Tienes una lista `alturas` donde cada elemento es una barra vertical en la posición i. Elige dos barras que, junto con el eje x, formen un contenedor; devuelve el máximo volumen (área) de agua que puede guardar: `min(alturas[i], alturas[j]) * (j - i)`.

Ejemplo:
`contenedor_agua([1,8,6,2,5,4,8,3,7])` -> `49`

En la entrevista te preguntarán: Demuéstrame por qué es correcto mover el puntero de la barra baja (argumento de descarte). ¿Y si quisieras el volumen de agua atrapada tras la lluvia (trapping rain water)? (two pointers con max_izq/max_der, también O(n)).
"""

# Pista 1: Fuerza bruta: probar todos los pares, O(n^2). ¿Puedes descartar pares sin probarlos?
# Pista 2: Empieza con los punteros en los extremos (máxima anchura). El área la limita la barra más baja.
# Pista 3: Mueve el puntero de la barra MÁS BAJA hacia dentro: mover la más alta nunca puede mejorar (la anchura baja y el mínimo no sube).

def contenedor_agua(alturas):
    # tu código aquí
    pass


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
