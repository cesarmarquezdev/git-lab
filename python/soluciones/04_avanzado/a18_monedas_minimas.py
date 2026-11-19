"""a18 - Cambio de monedas (Coin Change)  [extra]

Dada una lista de denominaciones `monedas` (enteros positivos, cantidad ilimitada de cada una) y un `monto`, devuelve el MENOR número de monedas que suman exactamente `monto`. Si es imposible, devuelve `-1`. Para `monto == 0` devuelve `0`.

Ejemplos:
`monedas_minimas([1, 2, 5], 11)` -> `3` (5+5+1)
`monedas_minimas([2], 3)` -> `-1`

En la entrevista te preguntarán: ¿Por qué no sirve el algoritmo voraz? (contraejemplo [1,3,4], 6). ¿Cuántas FORMAS distintas hay de formar el monto (Coin Change II)? (otro DP, cuidado con el orden de los bucles: combinaciones vs permutaciones). ¿Puedes bajar el espacio en climbing stairs a O(1)?
"""

# EXPLICACIÓN
# Camino recursión -> memo -> tabla:
# 1) Recursión pura: f(m) = 1 + min(f(m - c)). Correcta pero los subproblemas se repiten: O(S^n) con S = monto, n = monedas (exponencial). Con monto 6249 no termina.
# 2) Memoización: el mismo f(m) se calcula una sola vez si lo guardas en un dict (o @lru_cache). Hay `monto` estados y cada uno prueba n monedas -> O(monto * n) tiempo, O(monto) espacio, más la pila de recursión de profundidad `monto` (que en Python puede desbordar).
# 3) Tabla bottom-up: mismo coste O(monto * n) pero sin recursión: dp[m] se calcula desde menores a mayores. Trade-off: perdemos la 'pereza' de la memo (calcula todos los montos aunque no hagan falta) a cambio de evitar la recursión.
# Final: O(monto * n) tiempo, O(monto) espacio. Mismo patrón que climbing stairs (f(n) = f(n-1) + f(n-2)), que se reduce a 2 variables porque solo mira 2 estados atrás.
#
# PREGUNTA DEL ENTREVISTADOR
# ¿Por qué no sirve el algoritmo voraz? (contraejemplo [1,3,4], 6). ¿Cuántas FORMAS distintas hay de formar el monto (Coin Change II)? (otro DP, cuidado con el orden de los bucles: combinaciones vs permutaciones). ¿Puedes bajar el espacio en climbing stairs a O(1)?

def monedas_minimas(monedas, monto):
    INF = float("inf")
    dp = [0] + [INF] * monto          # dp[m] = mínimo de monedas para m
    for m in range(1, monto + 1):
        for c in monedas:
            if c <= m and dp[m - c] + 1 < dp[m]:
                dp[m] = dp[m - c] + 1
    return -1 if dp[monto] == INF else dp[monto]


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
