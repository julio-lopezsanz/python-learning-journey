"""
Crea una función que:
    -Reciba una lista de números
    -Reciba una función (como parámetro)
    -Aplique esa función a cada número
    -Devuelva la lista transformada
Como idea puede ser una funcion que duplique el valor de cada numero
"""

def apply_function(numbers, func):
    """
    Aplica una función a cada número y devuelve la lista transformada.
    """
    transformed = []
    for num in numbers:
        transformed.append(func(num))
    return transformed


def duplicate(number):
    """
    Duplica un numero
    """
    return number * 2


numbers = [2, 4, 6, 8, 10, 12, 14]
print(apply_function(numbers, duplicate))
