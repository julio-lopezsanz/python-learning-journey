"""
Crea un archivo modelos.py 
con una clase Estudiante que tenga: 
nombre, edad y calificaciones (lista). 
Agrega un método promedio() que calcule el promedio de sus calificaciones
"""

class Student:
    """Clase para registrar estudiantes: Datos personales y calificaciones"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def grades_avg(self):
        """Saca el promedio de las calificaciones de los estudiantes"""
        if not self.grades:
            return 0

        return sum(self.grades)/len(self.grades)

    def add_grades(self,grade):
        """Agrega calificaciones a la lista de calificaciones"""
        if 0 <= grade <= 100:
            self.grades.append(grade)
