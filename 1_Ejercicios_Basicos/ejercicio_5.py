"""
Author: Julio Cesar Lopez Sanchez
Problema: Escribe un programa para intercambiar los valores de dos variables, 
          y , sin usar una tercera variable temporal.
"""

def main() -> None:
    """Funcion principal"""
    a = 5
    b = 10
    print(f"Antes del cambio: a = {a} y b = {b}")
    a, b = b, a
    print(f"Despues del cambio: a = {a} y b = {b}")


if __name__ == "__main__":
    main()
