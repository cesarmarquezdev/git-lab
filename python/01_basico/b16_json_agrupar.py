r"""b16 - Leer JSON y agrupar (media)

Implementa:

1. `agrupar_por(ruta_json, clave)`: lee un archivo JSON con una lista de dicts y devuelve un dict `{valor_de_clave: [nombres...]}` agrupando el campo `'nombre'` de cada elemento segun `clave`. Mantiene el orden de aparicion.
   Para `[{'nombre': 'Ana', 'ciudad': 'Lima'}, {'nombre': 'Luis', 'ciudad': 'Lima'}, {'nombre': 'Eva', 'ciudad': 'Cusco'}]` y `clave='ciudad'` -> `{'Lima': ['Ana', 'Luis'], 'Cusco': ['Eva']}`
2. `a_json(d)`: devuelve el dict como string JSON con claves ordenadas y sin escapar acentos (`json.dumps`, `sort_keys=True`, `ensure_ascii=False`).
3. `de_json(texto)`: convierte el string JSON de vuelta a objeto Python (`json.loads`).

Casos borde: lista vacia -> `{}`.
"""

# Pista 1: `with open(ruta, encoding='utf-8') as f: datos = json.load(f)`.
# Pista 2: `grupos.setdefault(valor, []).append(nombre)` evita el if.
# Pista 3: `json.dumps(d, sort_keys=True, ensure_ascii=False)`.

import json


def agrupar_por(ruta_json, clave):
    pass


def a_json(d):
    pass


def de_json(texto):
    pass

if __name__ == "__main__":
    import json
    import os
    import tempfile

    with tempfile.TemporaryDirectory() as d:
        ruta = os.path.join(d, "gente.json")
        datos = [
            {"nombre": "Ana", "ciudad": "Lima"},
            {"nombre": "Luis", "ciudad": "Lima"},
            {"nombre": "Eva", "ciudad": "Cusco"},
        ]
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(datos, f)
        assert agrupar_por(ruta, "ciudad") == {"Lima": ["Ana", "Luis"], "Cusco": ["Eva"]}
        assert list(agrupar_por(ruta, "ciudad")) == ["Lima", "Cusco"], "orden de aparicion"
        vacio = os.path.join(d, "vacio.json")
        with open(vacio, "w", encoding="utf-8") as f:
            json.dump([], f)
        assert agrupar_por(vacio, "ciudad") == {}, "lista vacia"

    assert a_json({"b": 1, "a": "ñ"}) == '{"a": "ñ", "b": 1}'
    assert a_json({}) == '{}'
    assert de_json('{"a": [1, 2, null, true]}') == {"a": [1, 2, None, True]}
    assert de_json('[]') == []
    print("OK: todos los tests pasan")
