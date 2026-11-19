r"""b15 - Leer CSV, agrupar y escribir JSON (media)

Implementa `totales_por_categoria(ruta_csv, ruta_salida)`:

- Lee un CSV con cabecera `categoria,producto,monto` (usa `csv.DictReader` y `with open(..., newline='')`).
- Agrupa con un dict y suma el `monto` (float) por categoria.
- Escribe el resultado como JSON en `ruta_salida` (`json.dump`) y ademas lo devuelve.

Ejemplo, con filas `fruta,manzana,2.5`, `fruta,pera,1.5`, `lacteo,leche,3`:
-> `{'fruta': 4.0, 'lacteo': 3.0}`

Casos borde: CSV solo con cabecera -> `{}` (y se escribe `{}`).
"""

import csv
import json


def totales_por_categoria(ruta_csv, ruta_salida):
    totales = {}
    with open(ruta_csv, newline="", encoding="utf-8") as f:
        for fila in csv.DictReader(f):
            cat = fila["categoria"]
            totales[cat] = totales.get(cat, 0) + float(fila["monto"])
    with open(ruta_salida, "w", encoding="utf-8") as f:
        json.dump(totales, f)
    return totales

# Explicacion: `with` garantiza que el archivo se cierra aunque haya excepcion. DictReader da cada fila como dict, evitando indices magicos. Todo es O(n) en filas, memoria O(categorias) porque leemos en streaming. CSV entrega strings: hay que convertir a float.
# Pregunta del entrevistador: ¿Que pasa con un archivo de 10 GB? (Funciona: DictReader es un iterador, no carga todo en memoria.) ¿Y si falta una columna? (KeyError: decidir si validar o fallar.)

if __name__ == "__main__":
    import csv
    import json
    import os
    import tempfile

    with tempfile.TemporaryDirectory() as d:
        entrada = os.path.join(d, "ventas.csv")
        salida = os.path.join(d, "totales.json")
        with open(entrada, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["categoria", "producto", "monto"])
            w.writerow(["fruta", "manzana", "2.5"])
            w.writerow(["fruta", "pera", "1.5"])
            w.writerow(["lacteo", "leche", "3"])
        res = totales_por_categoria(entrada, salida)
        assert res == {"fruta": 4.0, "lacteo": 3.0}, "resultado devuelto"
        with open(salida, encoding="utf-8") as f:
            assert json.load(f) == {"fruta": 4.0, "lacteo": 3.0}, "archivo escrito"

        vacio = os.path.join(d, "vacio.csv")
        with open(vacio, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(["categoria", "producto", "monto"])
        salida2 = os.path.join(d, "vacio.json")
        assert totales_por_categoria(vacio, salida2) == {}, "solo cabecera"
        with open(salida2, encoding="utf-8") as f:
            assert json.load(f) == {}
    print("OK: todos los tests pasan")
