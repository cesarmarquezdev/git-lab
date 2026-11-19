"""i15 - Type hints con Optional (media)

Escribe con **type hints** completos:
1. `buscar_indice(lista: list[int], objetivo: int) -> Optional[int]`: índice de la primera aparición o `None` si no está.
2. `buscar_usuario(usuarios: list[dict[str, str]], nombre: str) -> Optional[dict[str, str]]`: el primer dict con `'nombre'` igual a `nombre`, o `None`.

Ejemplo:
```
buscar_indice([5, 6, 7], 7)  # 2
buscar_indice([5, 6], 9)  # None
buscar_indice([0], 0)  # 0 (¡no confundir con None!)
```

Pistas (no mires hasta intentarlo):
Pista 1: `from typing import Optional`; `Optional[int]` equivale a `int | None`.
Pista 2: Recorre con `enumerate` y `return` en cuanto encuentres; al final `return None` explícito.
Pista 3: Cuidado: el índice 0 es falsy; el llamador debe comparar con `is None`.

Entrevistador: ¿Por qué `if buscar_indice(...)` es un bug cuando el resultado puede ser 0? ¿Optional significa que el parámetro es opcional? ¿Los type hints se imponen en tiempo de ejecución?
"""

from typing import Optional


def buscar_indice(lista, objetivo):
    pass


def buscar_usuario(usuarios, nombre):
    pass


if __name__ == "__main__":
    from typing import Optional

    assert buscar_indice([5, 6, 7], 7) == 2
    assert buscar_indice([5, 6, 5], 5) == 0, "primera aparición"
    assert buscar_indice([0], 0) == 0, "índice 0 es válido"
    assert buscar_indice([], 1) is None, "lista vacía"
    assert buscar_indice([1, 2], 9) is None, "no encontrado"
    usuarios = [{"nombre": "ana", "rol": "admin"}, {"nombre": "luis", "rol": "dev"}]
    assert buscar_usuario(usuarios, "luis") == {"nombre": "luis", "rol": "dev"}
    assert buscar_usuario(usuarios, "zoe") is None
    assert buscar_usuario([], "ana") is None
    assert buscar_indice.__annotations__["return"] == Optional[int], "falta el hint de retorno Optional[int]"
    assert buscar_indice.__annotations__["lista"] == list[int], "falta el hint list[int]"
    assert buscar_usuario.__annotations__["return"] == Optional[dict[str, str]]
    assert buscar_usuario.__annotations__["usuarios"] == list[dict[str, str]]
    print("OK: todos los tests pasan")
