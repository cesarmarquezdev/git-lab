r"""b05 - Metodos de string y f-strings (facil)

Implementa tres funciones:

1. `normalizar_nombre(s)`: quita espacios de los extremos, colapsa espacios internos repetidos a uno solo y pone cada palabra con la primera letra en mayuscula.
   `'  ana   maria LOPEZ '` -> `'Ana Maria Lopez'`
2. `es_https(url)`: `True` si la URL (ignorando mayusculas y espacios extremos) empieza por `https://`.
3. `etiqueta_precio(producto, precio)`: usa un f-string: `etiqueta_precio('cafe', 3.5)` -> `'CAFE: $3.50'` (nombre en mayusculas, precio con 2 decimales).

Casos borde: string vacio o solo espacios en la 1 -> `''`.
"""

# Pista 1: `s.split()` sin argumentos ya colapsa espacios y quita los de los extremos.
# Pista 2: `' '.join(p.capitalize() for p in palabras)`. Para 3: `f'{x:.2f}'`.
# Pista 3: `url.strip().lower().startswith('https://')`

def normalizar_nombre(s):
    pass


def es_https(url):
    pass


def etiqueta_precio(producto, precio):
    pass

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
