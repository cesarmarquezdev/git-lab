"""i15 - Type hints con Optional (SOLUCIÓN)
"""

from typing import Optional


def buscar_indice(lista: list[int], objetivo: int) -> Optional[int]:
    for i, valor in enumerate(lista):
        if valor == objetivo:
            return i
    return None


def buscar_usuario(usuarios: list[dict[str, str]], nombre: str) -> Optional[dict[str, str]]:
    for usuario in usuarios:
        if usuario.get("nombre") == nombre:
            return usuario
    return None

# Explicación:
# Los hints no se verifican en ejecución: son documentación y la usan herramientas como mypy o el IDE. Desde 3.9 se escribe `list[int]`, `dict[str, str]` (sin `typing.List`) y desde 3.10 `int | None`. `Optional[X]` significa 'X o None', NO 'argumento opcional'. Devolver None obliga al llamador a manejar el caso; alternativa: lanzar excepción o devolver un valor por defecto. Búsqueda lineal O(n), espacio O(1).
# Entrevistador: ¿Por qué `if buscar_indice(...)` es un bug cuando el resultado puede ser 0? ¿Optional significa que el parámetro es opcional? ¿Los type hints se imponen en tiempo de ejecución?


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
