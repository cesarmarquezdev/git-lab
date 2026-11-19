r"""b13 - La trampa del default mutable (media)

Esta funcion tiene el bug clasico: la lista por defecto se comparte entre llamadas.

```
def agregar_tarea(tarea, lista=[]):
    lista.append(tarea)
    return lista
```

Arreglala para que:
- `agregar_tarea('a')` -> `['a']` y despues `agregar_tarea('b')` -> `['b']` (cada llamada sin lista crea una nueva).
- Si se pasa una lista, se añade a esa lista y se devuelve esa misma lista (mismo objeto).

Pista de entrevista: usa `None` como default.
"""

# Pista 1: Los valores por defecto se evaluan UNA sola vez, al definir la funcion.
# Pista 2: Cambia el default a `None` y crea la lista dentro de la funcion.
# Pista 3: `if lista is None: lista = []`

def agregar_tarea(tarea, lista=[]):
    lista.append(tarea)
    return lista

if __name__ == "__main__":
    assert agregar_tarea('a') == ['a']
    assert agregar_tarea('b') == ['b'], "no debe acumular entre llamadas"
    mia = ['x']
    r = agregar_tarea('y', mia)
    assert r == ['x', 'y']
    assert r is mia, "debe devolver la misma lista recibida"
    assert agregar_tarea('c') == ['c'], "sigue limpia tras usar una lista propia"
    vacia = []
    agregar_tarea('z', vacia)
    assert vacia == ['z'], "una lista vacia pasada tambien cuenta"
    print("OK: todos los tests pasan")
