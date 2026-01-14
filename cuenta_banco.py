class CuentaBanco:
    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        """
        Constructor de la clase CuentaBanco.

        :param titular: Nombre del titular de la cuenta
        :param saldo_inicial: Saldo inicial de la cuenta (por defecto 0.0)
        """
        self.titular = titular
        self.saldo = float(saldo_inicial)

    def _validar_monto(self, monto: float) -> float:
        """
        Valida que el monto sea numérico y mayor que cero.
        """
        if not isinstance(monto, (int, float)):
            raise TypeError("El monto debe ser un número.")
        if monto <= 0:
            raise ValueError("El monto debe ser mayor que cero.")
        return float(monto)

    def deposito_cuenta(self, monto: float):
        """
        Deposita un monto positivo a la cuenta.
        """
        monto = self._validar_monto(monto)
        self.saldo += monto
        return self.saldo
    
    def retiro_cuenta(self, monto: float):
        pass

    def transferencia_cuenta(self, monto: float, cuenta_destino):
        pass

    def saldo_cuenta(self) -> float:
        pass
