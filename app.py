from cuenta_banco import CuentaBanco


def mostra_menu():
    print("=== Menú de la Cuenta Bancaria ===")
    print("1. Depósito")
    print("2. Retiro")
    print("3. Transferencia")
    print("4. Consultar Saldo")
    print("5. Salir")


def pedir_monto(texto):
    """
    Pide un monto al usuario y lo convierte a float.
    """
    return float(input(texto))


def main():
    cuenta_origen = CuentaBanco("Titular Principal", 1000.0)
    cuenta_destino = CuentaBanco("Cuenta Destino", 500.0)

    while True:
        mostra_menu()
        opcion = input("Seleccione una opción (1-5): ").strip()

        try:
            if opcion == "1":
                monto = pedir_monto("Monto a depositar: ")
                cuenta_origen.deposito_cuenta(monto)
                print("Depósito realizado con éxito.")

            elif opcion == "2":
                monto = pedir_monto("Monto a retirar: ")
                cuenta_origen.retiro_cuenta(monto)
                print("Retiro realizado con éxito.")

            elif opcion == "3":
                monto = pedir_monto("Monto a transferir: ")
                cuenta_origen.transferencia_cuenta(monto, cuenta_destino)
                print("Transferencia realizada con éxito.")

            

        except ValueError as error:
            print(f"Error: {error}")
        except TypeError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
