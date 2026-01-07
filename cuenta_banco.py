class CuentaBanco:
    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        """
        Constructor de la clase CuentaBanco.

        :param titular: Nombre del titular de la cuenta
        :param saldo_inicial: Saldo inicial de la cuenta (por defecto 0.0)
        """
        self.titular = titular
        self.saldo = saldo_inicial

    def deposito_cuenta(self, monto: float):
        pass

    def retiro_cuenta(self, monto: float):
        pass

    def transferencia_cuenta(self, monto: float, cuenta_destino):
        pass

    def saldo_cuenta(self) -> float:
        pass
