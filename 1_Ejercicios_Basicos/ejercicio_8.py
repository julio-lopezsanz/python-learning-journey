"""
Author: Julio Cesar Lopez Sanchez
Problema: Escribe un programa que toma una cadena y la invierte 
          (por ejemplo, "Python" se convierte en "nohtyP").
"""


def invertir_palabra(word: str) -> str:
    """Toma un string y lo devuelve invertido

    Invierte el string utilizando la tecnica slicing

    Args:
        word (str): El string a invertir
    
    Returns:
        str: El string invertido con la tecnica slicing
    """

    return word[::-1]

def main() -> None:
    """Punto de entrada del programa"""
    word = input("Escribe una palabra: ")
    print(f"Resultado: {invertir_palabra(word)}")

if __name__ == "__main__":
    main()
