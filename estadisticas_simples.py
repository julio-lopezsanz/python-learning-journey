"""
Devuelve un diccionario con el promedio de cada alumno.
"""

grades = {
    "Ana": [90, 85, 92],
    "Luis": [70, 88, 80],
    "Pedro": [100, 95, 98]
}

def average_grade(dict_grades):
    """
    Devuelve el promedio de cada alumno
    """

    if not dict_grades:
        return {}

    return {
        student: round(sum(grades) / len(grades),2)
        for student, grades in dict_grades.items()
        #evita que se divida entre 0 en caso de que este vacio
        if grades
    }

result = average_grade(grades)

if not result:
    print("El diccionario que utiliza de parametro esta vacio")
else:
    print(result)
