r"""b05 - Metodos de string y f-strings (facil)

Implementa tres funciones:

1. `normalizar_nombre(s)`: quita espacios de los extremos, colapsa espacios internos repetidos a uno solo y pone cada palabra con la primera letra en mayuscula.
   `'  ana   maria LOPEZ '` -> `'Ana Maria Lopez'`
2. `es_https(url)`: `True` si la URL (ignorando mayusculas y espacios extremos) empieza por `https://`.
3. `etiqueta_precio(producto, precio)`: usa un f-string: `etiqueta_precio('cafe', 3.5)` -> `'CAFE: $3.50'` (nombre en mayusculas, precio con 2 decimales).

Casos borde: string vacio o solo espacios en la 1 -> `''`.
"""

def normalizar_nombre(s):
    return " ".join(p.capitalize() for p in s.split())


def es_https(url):
    return url.strip().lower().startswith("https://")


def etiqueta_precio(producto, precio):
    return f"{producto.upper()}: ${precio:.2f}"

# Explicacion: split() sin argumentos divide por cualquier bloque de espacios y descarta vacios; join es el inverso. Los strings son inmutables, cada metodo devuelve uno nuevo. Todo O(n).
# Pregunta del entrevistador: ¿Diferencia entre `.capitalize()`, `.title()` y `.upper()`? (title pone mayuscula tras cualquier no-letra: "o'neil" -> "O'Neil".)

if __name__ == "__main__":
    assert normalizar_nombre('  ana   maria LOPEZ ') == 'Ana Maria Lopez'
    assert normalizar_nombre('') == '', "vacio"
    assert normalizar_nombre('   ') == '', "solo espacios"
    assert normalizar_nombre('pepe') == 'Pepe', "una palabra"
    assert es_https('https://x.com') is True
    assert es_https('  HTTPS://x.com ') is True, "mayusculas y espacios"
    assert es_https('http://x.com') is False
    assert es_https('') is False
    assert etiqueta_precio('cafe', 3.5) == 'CAFE: $3.50'
    assert etiqueta_precio('te', 2) == 'TE: $2.00'
    print("OK: todos los tests pasan")
