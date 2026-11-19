r"""b12 - Argumentos: defaults, *args, **kwargs, lambda (facil)

Implementa:

1. `sumar_todo(*numeros)`: suma cualquier cantidad de argumentos posicionales (sin argumentos -> 0).
2. `formatear_kwargs(**kwargs)`: devuelve un string `'a=1, b=2'` con los argumentos con nombre ordenados alfabeticamente por clave. Sin argumentos -> `''`.
3. `potencia(base, exp=2)`: base elevada a `exp`; por defecto al cuadrado.
4. `ordenar_por_precio(productos)`: recibe una lista de dicts `{'nombre':..., 'precio':...}` y devuelve una lista nueva ordenada por precio ascendente usando `lambda`.

Ejemplos: `sumar_todo(1, 2, 3)` -> `6`; `formatear_kwargs(b=2, a=1)` -> `'a=1, b=2'`; `potencia(3)` -> `9`; `potencia(2, exp=3)` -> `8`.
"""

# Pista 1: `*numeros` llega como tupla; `**kwargs` llega como dict.
# Pista 2: `', '.join(f'{k}={v}' for k, v in sorted(kwargs.items()))`
# Pista 3: `sorted(productos, key=lambda p: p['precio'])`

def sumar_todo(*numeros):
    pass


def formatear_kwargs(**kwargs):
    pass


def potencia(base, exp=2):
    pass


def ordenar_por_precio(productos):
    pass

if __name__ == "__main__":
    assert sumar_todo(1, 2, 3) == 6
    assert sumar_todo() == 0, "sin argumentos"
    assert sumar_todo(5) == 5
    assert formatear_kwargs(b=2, a=1) == 'a=1, b=2'
    assert formatear_kwargs() == '', "sin kwargs"
    assert potencia(3) == 9
    assert potencia(2, exp=3) == 8
    assert potencia(2, 3) == 8, "posicional"
    assert potencia(base=5, exp=0) == 1
    ps = [{'nombre': 'b', 'precio': 5}, {'nombre': 'a', 'precio': 2}]
    assert [p['nombre'] for p in ordenar_por_precio(ps)] == ['a', 'b']
    assert ps[0]['nombre'] == 'b', "no muta"
    assert ordenar_por_precio([]) == []
    print("OK: todos los tests pasan")
