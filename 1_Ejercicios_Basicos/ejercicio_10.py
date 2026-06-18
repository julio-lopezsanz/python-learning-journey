"""
Author: Julio Cesar Lopez Sanchez
Problema: Dada una lista de enteros, 
          encuentra e imprime tanto el número mayor como el más pequeño.
"""

def encontrar_min_max(numbers: list) -> int:
    """Encuentra el numero mayor y menor en una lista

    utiliza las funciones min(), max() para encontrar el numero mayor y menor
    dentro de una lista de numeros

    Args:
        numbers (list): Es la lista de numeros

    Returns:
        tuple[int, int]: Una tupla con (el número menor, el número mayor).
    
    Raises:
        ValueError: Si la lista esta vacia
    """
    if not numbers:
        raise ValueError("La lista no puede estar vacia")

    return min(numbers), max(numbers)

def main() -> None:
    """Punto de entrada del programa"""
    nums = []
    num_min, num_max = encontrar_min_max(nums)
    print(f"Lista de numeros dada: {nums}")
    print(f"Numero mayor: {num_max}\nNumero menor: {num_min}")

if __name__ == "__main__":
    main()
