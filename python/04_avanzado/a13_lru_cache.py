"""a13 - LRU Cache  [extra]

Implementa la clase `LRUCache(capacidad)` con:
- `get(clave)`: devuelve el valor, o `-1` si no existe. Marca la clave como recién usada.
- `put(clave, valor)`: inserta o actualiza (también cuenta como uso). Si se excede la capacidad, elimina la clave menos recientemente usada.
Ambas operaciones deben ser O(1).

Ejemplo:
`c = LRUCache(2); c.put(1, 1); c.put(2, 2); c.get(1)` -> `1`; `c.put(3, 3)` expulsa la clave 2; `c.get(2)` -> `-1`.

En la entrevista te preguntarán: Impleméntalo sin OrderedDict (dict + lista doblemente enlazada con centinelas). ¿Y si es multihilo? (un lock, o lock striping; los move_to_end modifican estado incluso en get). ¿Y si quieres expiración por tiempo (TTL) o política LFU? ¿Y si la caché es distribuida?
"""

# Pista 1: Necesitas buscar por clave en O(1) y también saber cuál es la más antigua en O(1).
# Pista 2: En Python, collections.OrderedDict mantiene el orden de inserción y tiene move_to_end(k) y popitem(last=False).
# Pista 3: get: si existe, move_to_end y devuelve. put: asigna, move_to_end; si len > capacidad, popitem(last=False).

class LRUCache:
    def __init__(self, capacidad):
        # tu código aquí
        pass

    def get(self, clave):
        pass

    def put(self, clave, valor):
        pass


if __name__ == "__main__":
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)                      # expulsa la 2
    assert c.get(2) == -1, "la 2 debía ser expulsada"
    c.put(4, 4)                      # expulsa la 1
    assert c.get(1) == -1
    assert c.get(3) == 3
    assert c.get(4) == 4
    c = LRUCache(1)
    assert c.get(9) == -1, "cache vacía"
    c.put(1, "a")
    c.put(2, "b")
    assert c.get(1) == -1 and c.get(2) == "b", "capacidad 1"
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    c.put(1, 10)                     # actualizar cuenta como uso
    c.put(3, 3)                      # debe expulsar la 2, no la 1
    assert c.get(1) == 10 and c.get(2) == -1 and c.get(3) == 3, "actualizar refresca la clave"
    c = LRUCache(2)
    c.put(1, 0)
    assert c.get(1) == 0, "un valor 0 no es 'no existe'"
    print("OK: todos los tests pasan")
