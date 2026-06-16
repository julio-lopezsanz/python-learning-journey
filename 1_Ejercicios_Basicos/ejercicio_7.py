"""
Author: Julio Cesar Lopez Sanchez
Problema: Haz una lista de 5 frutas. 
          Añade una nueva fruta al final de la lista 
          y luego elimina la segunda fruta (en el índice 1).
"""

def main() -> None:
    """Funcion principal"""
    lista = ["manzana", "pera", "platano", "uva", "naranja"]
    lista.append("kiwi")
    print(lista)
    lista.pop(1)
    print(lista)

if __name__ == "__main__":
    main()
