"""a13 - LRU Cache  [extra]

Implementa la clase `LRUCache(capacidad)` con:
- `get(clave)`: devuelve el valor, o `-1` si no existe. Marca la clave como recién usada.
- `put(clave, valor)`: inserta o actualiza (también cuenta como uso). Si se excede la capacidad, elimina la clave menos recientemente usada.
Ambas operaciones deben ser O(1).

Ejemplo:
`c = LRUCache(2); c.put(1, 1); c.put(2, 2); c.get(1)` -> `1`; `c.put(3, 3)` expulsa la clave 2; `c.get(2)` -> `-1`.

En la entrevista te preguntarán: Impleméntalo sin OrderedDict (dict + lista doblemente enlazada con centinelas). ¿Y si es multihilo? (un lock, o lock striping; los move_to_end modifican estado incluso en get). ¿Y si quieres expiración por tiempo (TTL) o política LFU? ¿Y si la caché es distribuida?
"""

# EXPLICACIÓN
# 1) Ingenua: dict para los valores + lista con el orden de uso. Buscar y mover una clave en la lista es O(n) -> get/put O(n).
# 2) Con OrderedDict: internamente es un dict + lista doblemente enlazada, así move_to_end y popitem(last=False) son O(1). Es la respuesta corta en Python.
# 3) Versión 'a mano' que piden en la entrevista: un dict clave -> nodo, y una lista doblemente enlazada con nodos centinela cabeza/cola. Cada nodo guarda (clave, valor, prev, next). get: busca el nodo, lo desengancha y lo pone junto a la cola. put: si existe actualiza y mueve; si no, crea el nodo y, si se pasa de capacidad, quita el nodo junto a la cabeza y borra su clave del dict. Por eso el nodo guarda la clave: para borrarla del dict al expulsar. Se necesita la lista DOBLE porque desenganchar un nodo del medio en O(1) requiere conocer su prev.
# Final: get y put O(1), espacio O(capacidad).
#
# PREGUNTA DEL ENTREVISTADOR
# Impleméntalo sin OrderedDict (dict + lista doblemente enlazada con centinelas). ¿Y si es multihilo? (un lock, o lock striping; los move_to_end modifican estado incluso en get). ¿Y si quieres expiración por tiempo (TTL) o política LFU? ¿Y si la caché es distribuida?

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.datos = OrderedDict()

    def get(self, clave):
        if clave not in self.datos:
            return -1
        self.datos.move_to_end(clave)       # ahora es la más reciente
        return self.datos[clave]

    def put(self, clave, valor):
        self.datos[clave] = valor
        self.datos.move_to_end(clave)
        if len(self.datos) > self.capacidad:
            self.datos.popitem(last=False)  # expulsa la menos reciente


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
