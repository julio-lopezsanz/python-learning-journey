"""
Author: Julio Cesar Lopez Sanchez
Problema: Escribe una función para devolver True si el primer y último número 
          de una lista dada son el mismo. Si los números son diferentes, devuelva False.
"""

def comprobar_primer_ultimo_numero(numbers: list) -> bool:
    """Comprueba si el primer y ultimo numero de una lista son iguales.

    Utilizando los indices, se comprueba si el primer valor de una lista 
    es igual al ultimo.

    Args:
        numbers (list): lista de numeros.

    Returns:
        bool: True si los valores son iguales, False en caso contrario

    Raises:
        ValueError: Si la lista esta vacia 
    """

    if not numbers:
        raise ValueError("La lista no puede estar vacia")

    return numbers[0] == numbers[-1]

def main() -> None:
    """Punto de entrada del programa"""
    numbers_x = [10, 20, 30, 40, 10]
    numbers_y = [75, 65, 35, 75, 30]
    is_equal_x = comprobar_primer_ultimo_numero(numbers_x)
    is_equal_y = comprobar_primer_ultimo_numero(numbers_y)
    print(f"Dada la lista {numbers_x} | El resultado es: {is_equal_x}")
    print(f"Dada la lista {numbers_y} | El resultado es: {is_equal_y}")

if __name__ == "__main__":
    main()
