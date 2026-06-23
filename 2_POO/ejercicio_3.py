"""
Author: Julio Cesar Lopez Sanchez
Problema: Escribe un programa en Python para crear una clase Rectangulo con largo 
          y ancho como atributos de instancia,  
          y dos métodos: que devuelva el área y que devuelva el perímetro.
"""


class Rectangle:
    """Clase para representar un rectángulo con operaciones de área y perímetro."""

    def __init__(self, width: float, length: float) -> None:
        """Inicializa un rectángulo con ancho y largo dados.

        Args:
            width (float): El ancho del rectángulo.
            length (float): El largo del rectángulo.

        Raises:
            ValueError: Si width o length son 0 o negativos.
        """
        if width <= 0 or length <= 0:
            raise ValueError("La altura y la anchura de un rectangulo no pueden ser 0 o negativas.")
        self.width = width
        self.length = length

    def area(self) -> float:
        """Calcula el área del rectángulo.

        Returns:
            float: El área del rectángulo.
        """
        return self.width * self.length

    def perimeter(self) -> float:
        """Calcula el perímetro del rectángulo.

        Returns:
            float: El perímetro del rectángulo.
        """
        return 2 * (self.width + self.length)


def main() -> None:
    """Punto de entrada del programa."""
    rectangle1 = Rectangle(5, 6)
    print(f"Area del Rectangulo: {rectangle1.area()}")
    print(f"Perimetro del Rectangulo: {rectangle1.perimeter()}")

    rectangle2 = Rectangle(7.5, 9.0)
    print(f"Area del Rectangulo: {rectangle2.area()}")
    print(f"Perimetro del Rectangulo: {rectangle2.perimeter()}")

    rectangle3 = Rectangle(5.75, 7.86)
    print(f"Area del Rectangulo: {rectangle3.area()}")
    print(f"Perimetro del Rectangulo: {rectangle3.perimeter()}")


if __name__ == "__main__":
    main()
