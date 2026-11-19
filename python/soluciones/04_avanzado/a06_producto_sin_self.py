"""a06 - Producto de array excepto uno mismo  [extra]

Dada una lista `nums`, devuelve una lista `res` donde `res[i]` es el producto de todos los elementos de `nums` excepto `nums[i]`. NO uses división. Debe correr en O(n).

Ejemplos:
`producto_sin_self([1, 2, 3, 4])` -> `[24, 12, 8, 6]`
`producto_sin_self([-1, 1, 0, -3, 3])` -> `[0, 0, 9, 0, 0]`

En la entrevista te preguntarán: ¿Cómo manejarías los ceros si SÍ pudieras dividir? (contar ceros: 0 ceros -> total//x; 1 cero -> solo esa posición vale el producto del resto; 2+ -> todo ceros). ¿Y si el producto desborda? (en Python no, pero en otros lenguajes: módulo o logaritmos).
"""

# EXPLICACIÓN
# 1) Ingenua: para cada i multiplicar todos los demás -> O(n^2). Con división: producto total // nums[i] -> O(n), pero falla con ceros (y está prohibido).
# 2) Óptima: prefijos y sufijos. res[i] = prefijo[i-1] * sufijo[i+1]. En vez de dos arrays auxiliares, reutilizamos `res` para los prefijos y acumulamos el sufijo en una variable. Trade-off: código menos obvio a cambio de espacio extra O(1).
# 3) Final: O(n) tiempo, O(1) espacio extra (sin contar la salida).
#
# PREGUNTA DEL ENTREVISTADOR
# ¿Cómo manejarías los ceros si SÍ pudieras dividir? (contar ceros: 0 ceros -> total//x; 1 cero -> solo esa posición vale el producto del resto; 2+ -> todo ceros). ¿Y si el producto desborda? (en Python no, pero en otros lenguajes: módulo o logaritmos).

def producto_sin_self(nums):
    n = len(nums)
    res = [1] * n
    izquierda = 1
    for i in range(n):
        res[i] = izquierda          # producto de todo lo anterior a i
        izquierda *= nums[i]
    derecha = 1
    for i in range(n - 1, -1, -1):
        res[i] *= derecha           # producto de todo lo posterior a i
        derecha *= nums[i]
    return res


if __name__ == "__main__":
    assert producto_sin_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert producto_sin_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0], "un cero"
    assert producto_sin_self([0, 0, 2]) == [0, 0, 0], "dos ceros"
    assert producto_sin_self([2, 3]) == [3, 2], "dos elementos"
    assert producto_sin_self([5]) == [1], "un elemento: producto vacío es 1"
    assert producto_sin_self([]) == [], "vacío"
    assert producto_sin_self([-2, -3, 4]) == [-12, -8, 6], "negativos"
    assert producto_sin_self([1, 1, 1]) == [1, 1, 1]
    print("OK: todos los tests pasan")
