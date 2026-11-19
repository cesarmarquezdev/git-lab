"""i10 - Top-k palabras con Counter (SOLUCIÓN)
"""

from collections import Counter


def top_k_palabras(texto, k):
    palabras = (p.strip(".,;:!?¿¡").lower() for p in texto.split())
    conteo = Counter(p for p in palabras if p)
    return sorted(conteo.items(), key=lambda par: (-par[1], par[0]))[:k]

# Explicación:
# `Counter` es un dict especializado: contar es O(n). Ordenar los m distintos cuesta O(m log m). `Counter.most_common(k)` usa un heap (O(m log k)) pero no garantiza el desempate alfabético, por eso ordenamos con una clave compuesta `(-conteo, palabra)`. Espacio O(m). Un `if p` evita contar cadenas vacías (p. ej. un '!' suelto).
# Entrevistador: Si el texto tiene 10 millones de palabras y k=10, ¿qué mejorarías (heapq.nlargest)? ¿Cuándo te sirve Counter y cuándo un dict normal con get?


if __name__ == "__main__":
    assert top_k_palabras("a b a c b a", 2) == [("a", 3), ("b", 2)]
    assert top_k_palabras("Hola, hola! HOLA?", 1) == [("hola", 3)]
    assert top_k_palabras("", 3) == [], "texto vacío"
    assert top_k_palabras("solo", 5) == [("solo", 1)], "menos de k distintas"
    assert top_k_palabras("b a c", 2) == [("a", 1), ("b", 1)], "empate: orden alfabético"
    assert top_k_palabras("x y x", 0) == [], "k = 0"
    print("OK: todos los tests pasan")
