"""
Author: Julio Cesar Lopez Sanchez
Problema: Escribe una función en Python que acepte dos números enteros. 
          Si el producto de los dos números es menor o igual a 1000, 
          devuelven su producto; de lo contrario, devuelven su suma. 
"""


def multi_dos_numeros(num1: int, num2: int) -> int:
    """Multiplica o suma dos enteros segun el valor de su producto.

    Si el producto de num1 y num2 es menor o igual a 1000, retorna
    dicho producto. En caso contrario, retorna la suma de ambos.

    Args:
        num1 (int): Primer numero entero.
        num2 (int): Segundo numero entero.

    Returns:
        int: El producto (num1 * num2) si es <= 1000,
             o la suma (num1 + num2) si el producto supera 1000.
    """
    producto = num1 * num2
    return producto if producto <= 1000 else num1 + num2


def main():
    """Funcion principal"""
    try:
        numero1 = int(input("Ingresa el primer numero: "))
        numero2 = int(input("Ingresa el segundo numero: "))
        print(multi_dos_numeros(numero1, numero2))
    except ValueError:
        print("Error: Por favor ingresa solo numeros enteros.")


if __name__ == "__main__":
    main()
