"""
Author: Julio Cesar Lopez Sanchez
Problema: Crea un clase libro y agrega los metodos de prestar y devolver
"""

class Book:
    """
    Clase para representar un libro con operaciones de préstamo y devolución.
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def lend(self):
        """
        Metodo para prestar un libro. Cambia el estado de disponibilidad a False.
        """
        if not self.available:
            raise ValueError(f"El libro '{self.title}' no esta disponible para prestar")
        self.available = False

    def return_book(self):
        """
        Metodo para devolver un libro. Cambia el estado de disponibilidad a True.
        """
        if self.available:
            raise ValueError(f"El libro '{self.title}' ya esta disponible y no puede ser devuelto")
        self.available = True

def main():
    """Funcion principal para probar la clase Book."""
    book = Book("1984", "George Orwell")
    print(f"Libro: {book.title} - Disponible: {book.available}")

    book.lend()
    print(f"Libro: {book.title} - Disponible: {book.available}")

    book.return_book()
    print(f"Libro: {book.title} - Disponible: {book.available}")

if __name__ == "__main__":
    main()
