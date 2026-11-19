"""i08 - Closure con nonlocal: crear_contador (media)

Escribe `crear_contador(inicio=0, paso=1)` que devuelva una función. Cada llamada a esa función incrementa en `paso` un contador privado y devuelve el nuevo valor. Dos contadores creados por separado son independientes. No uses variables globales ni clases.

Ejemplo:
```
c = crear_contador()
c(), c(), c()  # 1, 2, 3
d = crear_contador(10, 5); d()  # 15
```

Pistas (no mires hasta intentarlo):
Pista 1: La función interna necesita modificar una variable de la función externa.
Pista 2: Sin declararla, `total += 1` dentro de la interna lanza UnboundLocalError.
Pista 3: Declara `nonlocal total` en la función interna.

Entrevistador: ¿Qué diferencia hay entre `nonlocal` y `global`? ¿Funcionaría sin `nonlocal` si `total` fuera una lista y usara `total[0] += 1`? ¿Por qué?
"""

def crear_contador(inicio=0, paso=1):
    # tu código aquí
    pass


if __name__ == "__main__":
    c = crear_contador()
    assert c() == 1
    assert c() == 2
    assert c() == 3
    d = crear_contador(10, 5)
    assert d() == 15
    assert c() == 4, "contadores independientes"
    assert d() == 20
    e = crear_contador(paso=-1)
    assert e() == -1
    assert crear_contador(inicio=100)() == 101
    print("OK: todos los tests pasan")
