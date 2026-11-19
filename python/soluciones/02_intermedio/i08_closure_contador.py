"""i08 - Closure con nonlocal: crear_contador (SOLUCIÓN)
"""

def crear_contador(inicio=0, paso=1):
    total = inicio

    def contar():
        nonlocal total
        total += paso
        return total

    return contar

# Explicación:
# Regla LEGB: Local, Enclosing, Global, Built-in. Leer una variable de la función envolvente funciona sola (closure), pero **reasignarla** crea una local salvo que declares `nonlocal`. El closure mantiene viva `total` aunque `crear_contador` ya haya terminado. O(1) por llamada. Alternativas: clase con `__call__`, o un generador.
# Entrevistador: ¿Qué diferencia hay entre `nonlocal` y `global`? ¿Funcionaría sin `nonlocal` si `total` fuera una lista y usara `total[0] += 1`? ¿Por qué?


if __name__ == "__main__":
    c = crear_contador()
    assert c() == 1
    assert c() == 2
    assert c() == 3
    d = crear_contador(10, 5)
    assert d() == 15
    assert c() == 4, "contadores independientes"
    assert d() == 20
    e = crear_contador(paso=-1)
    assert e() == -1
    assert crear_contador(inicio=100)() == 101
    print("OK: todos los tests pasan")
