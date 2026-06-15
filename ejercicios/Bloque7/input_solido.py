"""
Crea una función pedir_entero(mensaje) que use un bucle para pedir 
un número al usuario hasta que escriba uno válido. 
Cada vez que falle, muestra un mensaje de error claro. 
Retorna el entero válido.
"""
MESSAGE = "Error: Solo se pueden ingresar numeros enteros"

def request_int(msg):
    """
    Pide un valor valido (numero entero) y lo retorna.
    """
    while True:
        try:
            return int(input("Ingresa un numero entero: "))
        except ValueError:
            print(msg)


num = request_int(MESSAGE)
print(num)
