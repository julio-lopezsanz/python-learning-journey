"""
Contexto real: programa que no se cierra hasta que el usuario lo decida.

Crea un programa que:
    - Muestre un menú con opciones:
        -Agregar número a una lista
        -Mostrar la lista
        -Salir
    -Use while
    -Valide entradas incorrectas
"""
numbers = []

def add_number(numbers):
    """
    Agrega un numero a una lista
    """
    while True:
        try:
            number = int(input("\nIngrese el numero que desea agregar a las lista: "))
            numbers.append(number)
            print("\n¡el numero se ha agregado!")
            break
        except ValueError:
            print("\n¡ERROR: valor invalido. Solo se permiten numeros enteros!")

def show_list(numbers):
    """
    imprime la lista de numeros
    """
    if not numbers:
        print("\nLa lista está vacía")

    print("\nLista de numeros")
    print(numbers)

while True:
    print("\n-------------MENU-------------")
    print("1. Agregar un numero a la lista")
    print("2. Mostrar la lista de numeros")
    print("3. Salir del menu")
    try:
        option = int(input("\nSeleccione la accion que desea realizar: "))
        if option == 1:
            add_number(numbers)
        elif option == 2:
            show_list(numbers)
        elif option == 3:
            print("Saliendo del programa...")
            break
        else:
            print("\n¡ERROR: Opcion invalida. seleccione unicamente las opciones disponibles!")
    except ValueError:
        print("\n¡ERROR: valor invalido. Solo se permiten numeros enteros!")
