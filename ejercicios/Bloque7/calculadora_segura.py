"""
Crea una calculadora. 
Agrégale manejo de excepciones: 
    - Valida que los inputs sean números 
    - Que no haya división entre cero 
Usa raise para errores de lógica de negocio.
"""
MESSAGE = "Error: Solo se puede ingresar numeros"

def sum_of_num(msg):
    """
    Realiza la suma de dos numeros dados por el usuario y retorna el resultado
    """
    while True:
        try:
            num1 = int(input("\nIngresa el primer numero: "))
            num2 = int(input("Ingresa el segundo numero: "))
            return num1 + num2
        except ValueError:
            print(msg)

def substract(msg):
    """
    Realiza la resta de dos numeros dados por el usuario y retorna el resultado
    """
    while True:
        try:
            num1 = int(input("\nIngresa el primer numero: "))
            num2 = int(input("Ingresa el segundo numero: "))
            return num1 - num2
        except ValueError:
            print(msg)

def multi(msg):
    """
    Realiza la multiplicacion de dos numeros dados por el usuario y retorna el resultado
    """
    while True:
        try:
            num1 = int(input("\nIngresa el primer numero: "))
            num2 = int(input("Ingresa el segundo numero: "))
            return num1 * num2
        except ValueError:
            print(msg)

def div(msg):
    """
    Realiza la division de dos numeros dados por el usuario y retorna el resultado
    """
    while True:
        try:
            num1 = int(input("\nIngresa el primer numero: "))
            num2 = int(input("Ingresa el segundo numero: "))
            if num2 == 0:
                raise ZeroDivisionError("No puedes dividir entre 0")
            return num1 / num2
        except ValueError:
            print(msg)
        except ZeroDivisionError as e:
            print(f"Error: {e}")

while True:
    try:
        print("\n---------Menu---------")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")
        option = int(input("\n¿Que operacion desea realizar?: "))

        if option == 1:
            print("\nRealizando suma...")
            print(f"\nResultado: {sum_of_num(MESSAGE)}")
        elif option == 2:
            print("\nRealizando resta...")
            print(f"\nResultado: {substract(MESSAGE)}")
        elif option == 3:
            print("\nRealizando multiplicacion...")
            print(f"\nResultado: {multi(MESSAGE)}")
        elif option == 4:
            print("\nRealizando division...")
            print(f"\nResultado: {div(MESSAGE)}")
        elif option == 5:
            print("\nSaliendo del programa...")
            break
        else:
            print("Error: Opcion invalida")
    except ValueError:
        print(MESSAGE)
