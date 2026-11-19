# git-lab — práctica de Python para entrevista

Ejercicios del [roadmap](https://ferreteriabasurto4-ops.github.io/html_viernes/roadmap.html) (bloques C: Python y F: Lógica + estructuras), en 4 niveles.

| Nivel | Qué cubre |
|---|---|
| `01_basico` | Python esencial + práctica obligatoria (FizzBuzz, Counter, CuentaBancaria…) |
| `02_intermedio` | Nivel picky: decoradores, generadores, closures, dataclasses, collections |
| `03_logica` | Problemas obligatorios: Two Sum, palíndromo, paréntesis, binary search, BST… |
| `04_avanzado` | Extra difícil: Kadane, merge intervals, LRU cache, 3Sum, DP, backtracking |

## Cómo practicar

**En el navegador:** abre `index.html` (GitHub Pages o local con `python -m http.server` → http://localhost:8000). Python corre en el navegador.

**En local:**
```bash
python python/01_basico/b01_fizzbuzz.py   # edita el archivo hasta que diga ✅
```
Las soluciones están en `python/soluciones/`. Regla del roadmap: 20 min sin mirar, luego estudia la solución y reescríbela de memoria.

## En entrevista (5 pasos)
1. Repite el problema y pregunta casos borde.
2. Solución ingenua + su Big-O.
3. Mejora + trade-off.
4. Codea hablando.
5. Prueba: caso normal, vacío, un elemento.
