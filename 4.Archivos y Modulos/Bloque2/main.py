"""
Archivo main.py  
importa la clase, 
crea 2 estudiantes, 
guarda sus datos en un archivo estudiantes.json y luego los lee e imprime
"""
import json
import os
from modelos import Student

current_dir = os.path.dirname(__file__)
route = os.path.join(current_dir, "estudiantes.json")

student1 = Student("Julio", 18)
student2 = Student("Mario", 17)

try:
    student1.add_grades(100)
    student1.add_grades(80)
    student1.add_grades(90)
    student2.add_grades(50)
    student2.add_grades(60)
    student2.add_grades(80)
except ValueError as e:
    print(f"Error: {e}")

student1.avg = student1.grades_avg()
student2.avg = student2.grades_avg() 

# Guarda ambos estudiantes en una lista
with open(route, "w", encoding="utf-8") as file:
    estudiantes = [student1.__dict__, student2.__dict__]
    json.dump(estudiantes, file, indent=4)

# Lee e imprime cada estudiante
with open(route, "r", encoding="utf-8") as file:
    students = json.load(file)
    for student in students:
        print(f"Nombre: {student['name']} | Edad: {student['age']} | Promedio: {student['avg']}")
