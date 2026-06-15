"""
Author: Julio Cesar Lopez Sanchez
Problema: Mostrar solo aquellos caracteres que estén presentes en un índice 
          par en la cadena dada.
"""

def mostrar_indices_pares(word: str) -> None:
    """Muestra los caracteres de una cadena con indice par

    toma una cadena de caracteres, la recorre con el uso del ciclo for, e imprime
    unicamente los caracteres que esten en un indice par.

    args:
        word: Cadena de texto a procesar.

    returns:
            None   
    """

    for i, char in enumerate(word):
        if i % 2 == 0:
            print(f"{char}")

def main() -> None:
    """Funcion principal"""
    word = input("Ingresa una palabra a desglosar: ")
    mostrar_indices_pares(word)

if __name__ == "__main__":
    main()
