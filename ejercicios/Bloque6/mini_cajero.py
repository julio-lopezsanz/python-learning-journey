"""
Crea funciones: 
    -Depositar(saldo, monto) 
    -Retirar(saldo, monto) 
    -Mostrar_saldo(saldo). 
El retiro no puede dejar el saldo negativo. 
En el programa principal, simula 5 operaciones y muestra el saldo después de cada una.
"""
balance = 500


def deposit(bce, amt):
    """
    Agrega el monto a depositar al saldo actual
    """
    return bce + amt

def withdraw(bce, amt):
    """
    Retira un monto del saldo actual, siempre este no termine siendo negativo
    """
    if (bce - amt) < 0:
        print("No cuenta con el saldo suficiente para realizar esa operacion")
        return bce

    return bce - amt

def show_balance(bce):
    """
    Muestra el saldo actual
    """
    return bce

while True:
    print("-----Cajero automatico - Bienvenido-----")
    print("\n1. Depositar")
    print("\n2. Retirar")
    print("\n3. Mostrar Saldo")
    print("\n4. Salir")
    option = int(input("¿Que operacion desea realizar hoy?: "))

    if option == 1:
        amount = int(input("Ingrese el monto que desea depositar: "))
        balance = deposit(balance,amount)
    elif option == 2:
        amount = int(input("Ingrese el monto que desea retirar: "))
        balance = withdraw(balance,amount)
    elif option == 3:
        print(show_balance(balance))
    elif option == 4:
        print("Finalizando operacion...")
        break
    else:
        print("Opcion invalida")
