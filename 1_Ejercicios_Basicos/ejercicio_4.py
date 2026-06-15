"""
Author: Julio Cesar Lopez Sanchez
Problema: Escribe una función para eliminar caracteres de una cadena que va 
          desde el índice 0 hasta n y devuelve una nueva cadena.
"""

def convertir_cadena_en_subcadena(word: str, cut: int) -> str:
    """Toma una cadena de caracteres y crea una subcadena de ella.

    Toma un string y elimina un cantidad especifica de caracteres, retornando un nuevo string

    args:
          word: Cadena de texto original
          cut: Cantidad de caracteres que se eliminan

    returns: 
          new_string = word[cut:]
    """

    return word[cut:]

def main() -> None:
    """Funcion principal"""
    try:
        word = input("Ingresa una palabra: ")
        num = int(input("Ingresa la cantidad de caracteres que deseas quitar de la palabra: "))
        if num < 0 or num > len(word):
            print("Error: El número debe estar entre 0 y la longitud de la palabra.")
        else:
            print(convertir_cadena_en_subcadena(word, num))
    except ValueError:
        print("Error: Por favor ingresa solo datos validos (Cadena y enteros)")

if __name__ == "__main__":
    main()
