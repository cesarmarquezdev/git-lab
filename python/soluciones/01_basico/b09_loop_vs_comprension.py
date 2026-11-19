r"""b09 - Misma funcion con loop y con comprension (facil)

Implementa DOS versiones de la misma funcion:
- `cuadrados_pares_loop(nums)`: con un bucle `for` y `append`.
- `cuadrados_pares_comp(nums)`: con una list comprehension.

Ambas devuelven una lista con el cuadrado de cada numero PAR de `nums`, en el mismo orden.

Ejemplo: `[1, 2, 3, 4]` -> `[4, 16]`
Casos borde: lista vacia -> `[]`; sin pares -> `[]`; negativos: `-2` es par y su cuadrado es `4`.
"""

def cuadrados_pares_loop(nums):
    resultado = []
    for n in nums:
        if n % 2 == 0:
            resultado.append(n * n)
    return resultado


def cuadrados_pares_comp(nums):
    return [n * n for n in nums if n % 2 == 0]

# Explicacion: Ambas O(n) tiempo y O(k) espacio para k pares. La comprension es mas corta y algo mas rapida (menos overhead de llamar a append). Evita comprensiones anidadas ilegibles: si necesitas mas de un if/for, usa el loop.
# Pregunta del entrevistador: Si la lista tiene 10 millones de elementos y solo vas a iterar el resultado una vez, ¿que usarias en lugar de la lista? (Una expresion generadora con parentesis.)

if __name__ == "__main__":
    for f in (cuadrados_pares_loop, cuadrados_pares_comp):
        assert f([1, 2, 3, 4]) == [4, 16], f.__name__
        assert f([]) == [], f.__name__ + " vacia"
        assert f([1, 3]) == [], f.__name__ + " sin pares"
        assert f([-2, 0]) == [4, 0], f.__name__ + " negativos y cero"
        assert f([6]) == [36], f.__name__ + " un elemento"
    print("OK: todos los tests pasan")
