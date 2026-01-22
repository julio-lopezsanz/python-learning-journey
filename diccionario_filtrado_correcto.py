"""
Dado:

grades = {
    "math": 90,
    "english": 85,
    "science": 92,
    "history": 70
}

Crea una función que:
    -reciba el diccionario
    -devuelva un nuevo diccionario
    -solo con materias aprobadas (≥ 90)

Restricciones:
    -no modifiques el original
    -el retorno debe ser un diccionario
"""
grades = {
    "math": 90,
    "english": 85,
    "science": 92,
    "history": 70
}

def get_approved_grades(grades):
    """
    Devuelve un nuevo diccionario con las materias aprobadas (>= 90)
    """
    return {subject: grade for subject,grade in grades.items() if grade >= 90}

result = get_approved_grades(grades)
print(result)
