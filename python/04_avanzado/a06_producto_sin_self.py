"""a06 - Producto de array excepto uno mismo  [extra]

Dada una lista `nums`, devuelve una lista `res` donde `res[i]` es el producto de todos los elementos de `nums` excepto `nums[i]`. NO uses división. Debe correr en O(n).

Ejemplos:
`producto_sin_self([1, 2, 3, 4])` -> `[24, 12, 8, 6]`
`producto_sin_self([-1, 1, 0, -3, 3])` -> `[0, 0, 9, 0, 0]`

En la entrevista te preguntarán: ¿Cómo manejarías los ceros si SÍ pudieras dividir? (contar ceros: 0 ceros -> total//x; 1 cero -> solo esa posición vale el producto del resto; 2+ -> todo ceros). ¿Y si el producto desborda? (en Python no, pero en otros lenguajes: módulo o logaritmos).
"""

# Pista 1: Para cada i necesitas (producto de todo lo que está a la izquierda) * (producto de todo lo que está a la derecha).
# Pista 2: Haz una pasada de izquierda a derecha guardando en res[i] el producto de los previos.
# Pista 3: Haz una segunda pasada de derecha a izquierda con una variable `derecha` acumulada y multiplica res[i] por ella.

def producto_sin_self(nums):
    # tu código aquí
    pass


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
