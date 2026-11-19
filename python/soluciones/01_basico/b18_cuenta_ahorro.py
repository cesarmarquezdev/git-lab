r"""b18 - Herencia: CuentaAhorro (media)

Ya tienes `CuentaBancaria` (en la plantilla). Crea la subclase `CuentaAhorro`:

- `__init__(self, titular, saldo=0, tasa=0.05)`: usa `super().__init__` y guarda `tasa` (interes por periodo).
- `aplicar_interes()`: suma `saldo * tasa` al saldo.
- Atributo de CLASE `MINIMO = 10`: `retirar` no puede dejar el saldo por debajo de `MINIMO`; si lo haria lanza `SaldoInsuficienteError` (sin cambiar el saldo). Reutiliza el `retirar` del padre con `super().retirar`.
- `__repr__` propio: `"CuentaAhorro('Ana', 100, tasa=0.05)"` (el `__str__` heredado sigue funcionando).

Ejemplo: `c = CuentaAhorro('Ana', 100, 0.1); c.aplicar_interes()` -> `c.saldo == 110.0`.
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
            raise SaldoInsuficienteError("saldo insuficiente")
        self.saldo -= monto

    def __str__(self):
        return f"Cuenta de {self.titular}: ${self.saldo:.2f}"

    def __repr__(self):
        return f"CuentaBancaria({self.titular!r}, {self.saldo!r})"


class CuentaAhorro(CuentaBancaria):
    MINIMO = 10

    def __init__(self, titular, saldo=0, tasa=0.05):
        super().__init__(titular, saldo)
        self.tasa = tasa

    def aplicar_interes(self):
        self.saldo += self.saldo * self.tasa

    def retirar(self, monto):
        if monto > 0 and self.saldo - monto < self.MINIMO:
            raise SaldoInsuficienteError(f"el saldo no puede bajar de {self.MINIMO}")
        super().retirar(monto)

    def __repr__(self):
        return f"CuentaAhorro({self.titular!r}, {self.saldo!r}, tasa={self.tasa!r})"

# Explicacion: super() delega en la clase padre sin repetir codigo. MINIMO vive en la clase (compartido por todas las instancias); tasa vive en cada instancia. Sobrescribir retirar (polimorfismo) añade la regla y reutiliza la validacion del padre. Operaciones O(1).
# Pregunta del entrevistador: Si asigno `c.MINIMO = 50` en una instancia, ¿cambia el de la clase? (No: crea un atributo de instancia que oculta al de clase.)

if __name__ == "__main__":
    c = CuentaAhorro('Ana', 100, 0.1)
    assert isinstance(c, CuentaBancaria)
    c.aplicar_interes()
    assert c.saldo == 110.0
    assert CuentaAhorro('Luis').tasa == 0.05, "tasa por defecto"
    assert CuentaAhorro.MINIMO == 10 and 'MINIMO' not in vars(c), "MINIMO es atributo de clase"
    c = CuentaAhorro('Ana', 100)
    c.retirar(90)
    assert c.saldo == 10, "dejar exactamente el minimo es valido"
    try:
        c.retirar(1)
    except SaldoInsuficienteError:
        pass
    else:
        assert False, "no puede quedar por debajo del minimo"
    assert c.saldo == 10, "saldo intacto tras fallo"
    c.depositar(5)
    assert c.saldo == 15, "metodos heredados"
    try:
        c.retirar(-1)
    except ValueError:
        pass
    else:
        assert False, "monto invalido lo valida el padre"
    c = CuentaAhorro('Ana', 100)
    assert repr(c) == "CuentaAhorro('Ana', 100, tasa=0.05)"
    assert str(c) == 'Cuenta de Ana: $100.00'
    print("OK: todos los tests pasan")
