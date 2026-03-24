"""
Crea una función promedio() q
    - Que reciba cualquier cantidad de números
    - Retorne su promedio.
"""

def avarage(*grades):
    """Obtiene el promedio de una cantidad indefinida de calificaciones"""
    if not grades:
        return 0

    avg = 0
    for grade in grades:
        avg += grade
    return avg/len(grades)
    #Otra forma mas pythonic
    #return sum(grades) / len(grades)

print(avarage(5,10,5,10,5,10))
