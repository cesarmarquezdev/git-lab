r"""b17 - Clase CuentaBancaria (media)

Crea:

1. La excepcion `SaldoInsuficienteError` (hereda de `Exception`).
2. La clase `CuentaBancaria` con:
   - `__init__(self, titular, saldo=0)`
   - `depositar(monto)`: suma al saldo. Si `monto <= 0` lanza `ValueError`.
   - `retirar(monto)`: resta del saldo. Si `monto <= 0` lanza `ValueError`; si `monto > saldo` lanza `SaldoInsuficienteError` y el saldo NO cambia.
   - `saldo` accesible como atributo.
   - `__str__` legible: `'Cuenta de Ana: $100.00'`
   - `__repr__` para depurar: `"CuentaBancaria('Ana', 100)"`

Retirar exactamente todo el saldo es valido.
"""

class SaldoInsuficienteError(Exception):
    pass


class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("el monto debe ser positivo")
        self.saldo += monto

    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("el monto debe ser positivo")
        if monto > self.saldo:
            raise SaldoInsuficienteError(f"saldo {self.saldo}, intento de retirar {monto}")
        self.saldo -= monto

    def __str__(self):
        return f"Cuenta de {self.titular}: ${self.saldo:.2f}"

    def __repr__(self):
        return f"CuentaBancaria({self.titular!r}, {self.saldo!r})"

# Explicacion: Validar antes de mutar mantiene el objeto consistente. Excepcion propia = mejor semantica que ValueError generico, el llamador puede capturarla de forma especifica. __str__ es para usuarios (print), __repr__ para desarrolladores (consola, listas, depuracion). Operaciones O(1).
# Pregunta del entrevistador: En dinero real, ¿usarias float para el saldo? (No: errores de redondeo; usa decimal.Decimal o enteros en centimos.)

if __name__ == "__main__":
    c = CuentaBancaria('Ana', 100)
    assert c.saldo == 100
    assert CuentaBancaria('Luis').saldo == 0, "saldo por defecto"
    c.depositar(50)
    assert c.saldo == 150
    c.retirar(150)
    assert c.saldo == 0, "retirar todo es valido"
    c = CuentaBancaria('Ana', 100)
    try:
        c.retirar(101)
    except SaldoInsuficienteError:
        pass
    else:
        assert False, "debia lanzar SaldoInsuficienteError"
    assert c.saldo == 100, "el saldo no cambia si falla"
    assert issubclass(SaldoInsuficienteError, Exception)
    for malo in (0, -5):
        try:
            c.depositar(malo)
        except ValueError:
            pass
        else:
            assert False, "depositar monto invalido"
        try:
            c.retirar(malo)
        except ValueError:
            pass
        else:
            assert False, "retirar monto invalido"
    assert str(c) == 'Cuenta de Ana: $100.00'
    assert repr(c) == "CuentaBancaria('Ana', 100)"
    print("OK: todos los tests pasan")
