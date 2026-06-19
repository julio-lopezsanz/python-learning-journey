"""
Author: Julio Cesar Lopez Sanchez
Problema: Itera por una lista dada de números e 
          imprime solo aquellos que sean divisibles por 5.
"""

def filtrar_divisores(numbers: list) -> list:
    """Toma una lista y retorna una nueva lista solo con numeros divisibles entre 5

    Recorre los valores de la lista y selecciona los unicos numeros que son divisibles entre 5
    para agregarlos a la lista nueva.

    Args:
        numbers (list): Es la lista de numeros dada
    
    Returns:
        list: Regresa la lista con numeros divisibles por 5

    Raises:
        ValueError: Si la lista esta vacia.
    """

    if not numbers:
        raise ValueError("La lista no puede estar vacia")

    return [x for x in numbers if x % 5 == 0]

def main() -> None:
    """Punto de entrada del programa"""
    num_list = [10, 20, 33, 46, 55]
    print(f"lista de numeros: {num_list}")
    print(f"lista de numeros divisible por 5: {filtrar_divisores(num_list)}")

if __name__ == "__main__":
    main()
