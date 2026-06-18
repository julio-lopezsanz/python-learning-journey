"""
Author: Julio Cesar Lopez Sanchez
Problema: Escribe un script que tome una lista que contenga elementos duplicados 
          y devuelva una nueva lista con solo elementos únicos.
"""

def eliminar_duplicado_lista(data_list: list) -> list:
    """Elimina los duplicados de una lista y retorna una lista solo con los elementos unicos

    Convierte la lista en un set, debido que los sets no pueden tener datos duplicados, auto-
    maticamente se eliminan los datos duplicados. despues volver a convertir ese set en una lista

    Args:
        data_list (list): Lista con elementos duplicados

    Returns:
        list: Lista con los elementos unicos 

    Raises:
        ValueError: Si la lista esta vacia
    """

    if not data_list:
        raise ValueError("La lista no puede estar vacia")

    no_duplicates = set(data_list)
    return list(no_duplicates)

def main() -> None:
    """Punto de entrada del programa"""
    data = [1, 2, 2, 3, 4, 4, 4, 5]
    new_data = eliminar_duplicado_lista(data)
    print(f"Lista de datos en bruto: {data}")
    print(f"Lista de datos sin elementos duplicados: {new_data}")

if __name__ == "__main__":
    main()
