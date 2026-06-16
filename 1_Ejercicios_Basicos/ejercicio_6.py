"""
Author: Julio Cesar Lopez Sanchez
Problema: Escribe un programa que calcule el factorial de un número dado 
          (¡por ejemplo, 5!) usando un bucle.
"""


def conseguir_factorial(num: int) -> int:
    """Toma un número entero y devuelve su factorial.

    Calcula el factorial de num multiplicando todos los enteros
    positivos desde 1 hasta num. Si num es 0, retorna 1.

    Args:
        num (int): Número entero no negativo.

    Returns:
        int: El factorial del número dado.

    Raises:
        ValueError: Si num es negativo.
    """
    if num < 0:
        raise ValueError(f"El número no puede ser negativo, se recibió {num}.")
    if num == 0:
        return 1

    factorial = 1
    for i in range(1, num + 1):
        factorial *= i

    return factorial


def main() -> None:
    """Punto de entrada del programa."""
    try:
        num = int(input("Ingresa el numero al que deseas sacar el factorial: "))
        print(f"El factorial de {num} es: {conseguir_factorial(num)}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
