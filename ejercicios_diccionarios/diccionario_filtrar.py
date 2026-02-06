"""
Crea una función que:
    -reciba un diccionario de materias → calificaciones
    -devuelva solo las materias aprobadas
    -considera aprobado ≥ 90

Resultado esperado:
{"math": 90, "science": 92}
"""
grades = {
    "math": 90,
    "english": 85,
    "science": 92
}

def get_approved_grades(grades):
    """
    Devuelve solamente la materia y calificacion aprobada
    """
    #Nota mental: Es importante que pese que con otros metodos visualmente el resultado
    #sea el mismo o parecido, es importante comprender que la estructura puede que no sea
    #la indicada, este resultado se puede devolver como una lista, un set o un diccionario
    #pero la manera en la que trabaja cada uno de ellos, es importante destacar esto. ya
    #que grandes bugs se forman de esa manera.
    return {subject: grade for subject,grade in grades.items() if grade >= 90}

print(get_approved_grades(grades))
