"""
Dado:

grades = {
    "math": 90,
    "english": 85,
    "science": 92
}

Crea una función que:
    -reciba el diccionario
    -imprima cada materia y su calificación
    -use .items()

Ejemplo de salida:

math: 90
english: 85
science: 92

"""

grades = {
    "math": 90,
    "english": 85,
    "science": 92
}

def print_data(grades):
    """
    imprime la clave y el valor de un diccionario
    """
    for subject,grade in grades.items():
        print(f"{subject}: {grade}")

print_data(grades)
