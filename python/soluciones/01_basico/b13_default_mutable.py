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

def agregar_tarea(tarea, lista=None):
    if lista is None:
        lista = []
    lista.append(tarea)
    return lista

# Explicacion: El default se evalua al definir la funcion y el mismo objeto se reutiliza. Con None creamos una lista nueva en cada llamada. Ojo: usar `if not lista` seria un bug, porque una lista vacia pasada por el usuario seria reemplazada; hay que comparar con `is None`.
# Pregunta del entrevistador: ¿Por que `if not lista: lista = []` es un bug sutil? ¿Cuando el default mutable es util a proposito? (Cache/memoizacion rapida.)

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
