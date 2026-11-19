"""a10 - Mejor momento para comprar y vender  [dificil]

`precios[i]` es el precio de una acción el día i. Puedes comprar un día y vender en un día POSTERIOR. Devuelve la ganancia máxima; si no hay forma de ganar, devuelve `0`.

Ejemplos:
`mejor_compra_venta([7,1,5,3,6,4])` -> `5` (compras a 1, vendes a 6)
`mejor_compra_venta([7,6,4,3,1])` -> `0`

En la entrevista te preguntarán: ¿Y si puedes hacer tantas transacciones como quieras? (suma de todas las subidas positivas). ¿Y como máximo k transacciones? (DP O(n*k)). ¿Y con enfriamiento de un día o comisión?
"""

# EXPLICACIÓN
# 1) Ingenua: probar todos los pares (compra, venta) con compra < venta -> O(n^2).
# 2) Óptima: para vender el día i, la mejor compra es el mínimo de los días anteriores. Una pasada manteniendo ese mínimo. Trade-off: ninguno; solo hay que ver que la decisión 'voraz' es suficiente.
# 3) Final: O(n) tiempo, O(1) espacio. Es Kadane disfrazado (máximo subarray sobre las diferencias diarias).
#
# PREGUNTA DEL ENTREVISTADOR
# ¿Y si puedes hacer tantas transacciones como quieras? (suma de todas las subidas positivas). ¿Y como máximo k transacciones? (DP O(n*k)). ¿Y con enfriamiento de un día o comisión?

def mejor_compra_venta(precios):
    if not precios:
        return 0
    minimo = precios[0]
    mejor = 0
    for p in precios[1:]:
        mejor = max(mejor, p - minimo)
        minimo = min(minimo, p)
    return mejor


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
