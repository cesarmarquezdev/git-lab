"""a10 - Mejor momento para comprar y vender  [dificil]

`precios[i]` es el precio de una acción el día i. Puedes comprar un día y vender en un día POSTERIOR. Devuelve la ganancia máxima; si no hay forma de ganar, devuelve `0`.

Ejemplos:
`mejor_compra_venta([7,1,5,3,6,4])` -> `5` (compras a 1, vendes a 6)
`mejor_compra_venta([7,6,4,3,1])` -> `0`

En la entrevista te preguntarán: ¿Y si puedes hacer tantas transacciones como quieras? (suma de todas las subidas positivas). ¿Y como máximo k transacciones? (DP O(n*k)). ¿Y con enfriamiento de un día o comisión?
"""

# Pista 1: Para cada día de venta, ¿cuál sería la mejor compra posible? Solo importa el mínimo anterior.
# Pista 2: Recorre una vez guardando el precio mínimo visto hasta ahora.
# Pista 3: En cada día: ganancia = precio - minimo; actualiza la mejor y luego el mínimo.

def mejor_compra_venta(precios):
    # tu código aquí
    pass


if __name__ == "__main__":
    assert mejor_compra_venta([7, 1, 5, 3, 6, 4]) == 5
    assert mejor_compra_venta([7, 6, 4, 3, 1]) == 0, "siempre baja"
    assert mejor_compra_venta([]) == 0, "vacío"
    assert mejor_compra_venta([5]) == 0, "un elemento"
    assert mejor_compra_venta([2, 4, 1]) == 2, "el mínimo global llega tarde"
    assert mejor_compra_venta([3, 3, 3]) == 0, "precios iguales"
    assert mejor_compra_venta([1, 2]) == 1
    assert mejor_compra_venta([2, 1, 2, 0, 1]) == 1
    print("OK: todos los tests pasan")
