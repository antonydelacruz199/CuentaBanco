from cuenta_banco import CuentaBanco


def main():
    cuenta_origen = CuentaBanco("Titular Principal", 1000.0)
    cuenta_destino = CuentaBanco("Cuenta Destino", 500.0)


if __name__ == "__main__":
    main()
