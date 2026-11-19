"""i10 - Top-k palabras con Counter (media)

Escribe `top_k_palabras(texto, k)` que devuelva una lista de tuplas `(palabra, veces)` con las `k` palabras más frecuentes. Ignora mayúsculas y la puntuación `.,;:!?¿¡`. Los empates se ordenan alfabéticamente (para que el resultado sea determinista). Si hay menos de `k` palabras distintas, devuelve todas.

Ejemplo:
```
top_k_palabras('a b a c b a', 2)  # [('a', 3), ('b', 2)]
top_k_palabras('Hola, hola!', 1)  # [('hola', 2)]
```

Pistas (no mires hasta intentarlo):
Pista 1: `collections.Counter` cuenta elementos de un iterable en una sola línea.
Pista 2: Limpia el texto con `.lower()` y `.strip('.,;:!?¿¡')` por cada palabra tras `.split()`.
Pista 3: Ordena con `sorted(c.items(), key=lambda p: (-p[1], p[0]))` y corta con `[:k]`.

Entrevistador: Si el texto tiene 10 millones de palabras y k=10, ¿qué mejorarías (heapq.nlargest)? ¿Cuándo te sirve Counter y cuándo un dict normal con get?
"""

from collections import Counter


def top_k_palabras(texto, k):
    # tu código aquí
    pass


if __name__ == "__main__":
    assert top_k_palabras("a b a c b a", 2) == [("a", 3), ("b", 2)]
    assert top_k_palabras("Hola, hola! HOLA?", 1) == [("hola", 3)]
    assert top_k_palabras("", 3) == [], "texto vacío"
    assert top_k_palabras("solo", 5) == [("solo", 1)], "menos de k distintas"
    assert top_k_palabras("b a c", 2) == [("a", 1), ("b", 1)], "empate: orden alfabético"
    assert top_k_palabras("x y x", 0) == [], "k = 0"
    print("OK: todos los tests pasan")
