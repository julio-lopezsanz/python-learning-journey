"""
Author: Julio Cesar Lopez Sanchez
Problema: Iterar por los primeros 10 números (0 a 9). 
          En cada iteración, imprime el número actual, el anterior y su suma.
"""

def mostrar_iteraciones() -> None:
    """Imprime el numero actual, el anterior y su suma para los primeros 10 numeros.

    Itera del 0 al 9. En la primera iteracion (i=0), el numero
    anterior se trata como 0.

    Returns:
        None
    """

    for i in range(10):
        anterior = i-1 if i > 0 else 0

        print(f"numero de Iteracion actual: {i}")
        print(f"numero de Iteracion anterior: {anterior}")
        print(f"Suma de los numeros de iteracion: {i + anterior}")


def main() -> None:
    """Funcion Principal"""
    mostrar_iteraciones()

if __name__ == "__main__":
    main()
