"""
Author: Julio Cesar Lopez Sanchez
Problema: Escribe un programa para contar el número total de vocales 
          (a, e, i, o, u) presentes en una oración dada.
"""

def contar_vocales(text: str) -> int:
    """Cuenta la cantidad de vocales que hay en un texto.

    Recorre el texto carácter por carácter y acumula la cantidad
    de vocales encontradas (mayúsculas y minúsculas).

    Args:
        text (str): Es el texto de donde se contarán las vocales.

    Returns:
        int: La cantidad total de vocales en el texto.
    """
    vocals = "aeiouAEIOU"
    vocals_amount = 0
    for char in text:
        if char in vocals:
            vocals_amount += 1

    return vocals_amount


def main() -> None:
    """Punto de entrada del programa."""
    text = input("Ingrese un texto: ")
    print(f"Cantidad total de vocales en el texto: {contar_vocales(text)}")


if __name__ == "__main__":
    main()
