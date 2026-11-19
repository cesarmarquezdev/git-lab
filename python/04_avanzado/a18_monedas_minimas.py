"""a18 - Cambio de monedas (Coin Change)  [extra]

Dada una lista de denominaciones `monedas` (enteros positivos, cantidad ilimitada de cada una) y un `monto`, devuelve el MENOR número de monedas que suman exactamente `monto`. Si es imposible, devuelve `-1`. Para `monto == 0` devuelve `0`.

Ejemplos:
`monedas_minimas([1, 2, 5], 11)` -> `3` (5+5+1)
`monedas_minimas([2], 3)` -> `-1`

En la entrevista te preguntarán: ¿Por qué no sirve el algoritmo voraz? (contraejemplo [1,3,4], 6). ¿Cuántas FORMAS distintas hay de formar el monto (Coin Change II)? (otro DP, cuidado con el orden de los bucles: combinaciones vs permutaciones). ¿Puedes bajar el espacio en climbing stairs a O(1)?
"""

# Pista 1: Estrategia voraz (usar siempre la moneda más grande) falla: con [1,3,4] y monto 6 da 4+1+1 (3 monedas) pero lo óptimo es 3+3 (2).
# Pista 2: Define f(m) = mínimo de monedas para el monto m. f(m) = 1 + min(f(m - c)) para cada moneda c <= m. f(0) = 0.
# Pista 3: Hazlo con tabla: dp[0] = 0, dp[m] = infinito al inicio; llena m de 1 a monto. Al final, si dp[monto] sigue infinito -> -1.

def monedas_minimas(monedas, monto):
    # tu código aquí
    pass


if __name__ == "__main__":
    assert monedas_minimas([1, 2, 5], 11) == 3
    assert monedas_minimas([2], 3) == -1, "imposible"
    assert monedas_minimas([1], 0) == 0, "monto cero"
    assert monedas_minimas([], 0) == 0, "sin monedas y monto 0"
    assert monedas_minimas([], 5) == -1, "sin monedas"
    assert monedas_minimas([1], 2) == 2
    assert monedas_minimas([1, 3, 4], 6) == 2, "el voraz falla aquí"
    assert monedas_minimas([2, 5, 10, 1], 27) == 4
    assert monedas_minimas([186, 419, 83, 408], 6249) == 20, "monto grande: la recursión ingenua no termina"
    print("OK: todos los tests pasan")
