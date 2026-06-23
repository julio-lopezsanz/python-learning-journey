"""
Author: Julio Cesar Lopez Sanchez
Problema: Escribe un programa en Python que defina una clase llamada estudiante
          que almacene el nombre del estudiante y una lista de calificaciones.
          Agrega un metodo de promedio que calcule y devuelva el promedio de las calificaciones.
"""


class Student:
    """Clase para representar un estudiante con nombre y calificaciones, y calcular su promedio."""

    def __init__(self, name: str, marks: list) -> None:
        """Inicializa un estudiante con un nombre y una lista de calificaciones.

        Args:
            name (str): El nombre del estudiante.
            marks (list): Lista de calificaciones del estudiante.

        Raises:
            ValueError: Si la lista de calificaciones está vacía.
        """
        if not marks:
            raise ValueError("La lista de calificaciones no puede estar vacia")
        self.name = name
        self.marks = marks

    def average(self) -> float:
        """Calcula y devuelve el promedio de las calificaciones.

        Returns:
            float: El promedio de las calificaciones.
        """
        return sum(self.marks) / len(self.marks)


def main() -> None:
    """Funcion principal."""
    student1 = Student("Maria", [85, 90, 78, 92, 88])
    print(f"El promedio de {student1.name} es: {student1.average()}")

    student2 = Student("Julio", [90, 90, 100, 100, 100])
    print(f"El promedio de {student2.name} es: {student2.average()}")

    student3 = Student("Adolfo", [70, 80, 50, 100, 80])
    print(f"El promedio de {student3.name} es: {student3.average()}")


if __name__ == "__main__":
    main()
