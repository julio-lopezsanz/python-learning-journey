"""
Retoma el ejercicio del mini banco. 
    - Crea excepciones propias: SaldoInsuficienteError y MontoInvalidoError (hereda de Exception). 
    - Úsalas en las funciones del banco. 
    - En el programa principal, maneja cada excepción de forma distinta.
    - Cambia el if/elif por match/case
Debido a que en esta practica se usaran conceptos nuevos como ex
"""

BALANCE = 500

class SaldoInsuficienteError(Exception):
    """Clase propia que hereda cosas de la clase Exception"""

class MontoInvalidoError(Exception):
    """Clase propia que hereda cosas de la clase Exception"""

def deposit(balance):
    """
    Pide una cantidad a depositar, y lo agrega al saldo
    """
    while True:
        try:
            amount = int(input("\nIngrese el monto que desea depositar: "))

            if amount > 10000:
                raise MontoInvalidoError("Solo puedes ingresar hasta $10,000 por operación")
            if amount <= 0:
                raise MontoInvalidoError("El monto debe ser mayor a 0")

            return balance + amount

        except ValueError:
            print("Error: Solo se permiten números enteros.")
        except MontoInvalidoError as e:
            print(f"Error: {e}")

def withdraw(balance):
    """
    Retira un monto del saldo actual, siempre este no termine siendo negativo
    """
    while True:
        try:
            amount = int(input("\nIngrese el monto que desea retirar: "))

            if amount > balance:
                raise SaldoInsuficienteError("Saldo insuficiente para realizar la operacion")
            if amount <= 0:
                raise MontoInvalidoError("El monto debe ser mayor a 0")

            return balance - amount

        except ValueError:
            print("\nError: Solo se permiten números enteros.")
        except MontoInvalidoError as e:
            print(f"\nError: {e}")
        except SaldoInsuficienteError as ex:
            print(f"\nError: {ex}")

def show_balance(balance):
    """
    Muestra el saldo actual
    """
    print(f"\nSaldo actual: ${balance}\n")

while True:
    print("-----Cajero automatico - Bienvenido-----")
    print("\n1. Depositar")
    print("\n2. Retirar")
    print("\n3. Mostrar Saldo")
    print("\n4. Salir")
    try:
        option = int(input("\n¿Que operacion desea realizar hoy?: "))
        match option:
            case 1:
                BALANCE = deposit(BALANCE)
            case 2:
                BALANCE = withdraw(BALANCE)
            case 3:
                show_balance(BALANCE)
            case 4:
                print("\nFinalizando operacion...")
                break
            case _:
                print("\nError: opcion invalida")
    except ValueError:
        print("\nSolo se permiten numeros.")
