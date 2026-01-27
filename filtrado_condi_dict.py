"""
Dado:

students = {
    "Ana": 85,
    "Luis": 92,
    "Pedro": 78,
    "Marta": 95,
    "Sofia": 90
}


Crea una función que:
    - devuelva SOLO los aprobados (≥ 90)
    - pero con este formato nuevo:

{
    "Luis": "aprobado",
    "Marta": "aprobado",
    "Sofia": "aprobado"
}
"""

students = {
    "Ana": 85,
    "Luis": 92,
    "Pedro": 78,
    "Marta": 95,
    "Sofia": 90
}

def get_approved_students(dictionary):
    """
    Obtiene los alumnos aprobados de un diccionario
    """
    return {student: "Aprobado" for student, grade in dictionary.items() if grade >=90}

result = get_approved_students(students)

if not result:
    print("El diccionario que uso como argumento esta vacio")
else:
    print(result)
