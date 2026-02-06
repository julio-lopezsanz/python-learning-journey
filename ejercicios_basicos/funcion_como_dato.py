"""
Crea una función llamada:
    -apply(numbers, func)
que aplique func a cada número y devuelva la lista resultante.
Luego crea:
    -una función que duplique
    -una que eleve al cuadrado
    -una que reste 1
Pásalas a apply.
"""
numbers = [1,2,3,4,5,6]

def apply(numbers, func):
    """
    Crea una nueva lista, utilizando cualquiera de las 
    funciones predeterminadas como duplicar, elevar, o restas
    """
    #Solucion con comprension: return [func(n) for n in numbers]

    #Solucion con map
    new_numbers = list(map(func, numbers))
    return new_numbers

def duplicate(number):
    """
    Duplica un numero
    """
    return number * 2

def square(number):
    """
    Eleva al cuadrado un numero
    """
    return number ** 2

def subtract(number):
    """
    Resta uno a un numero
    """
    return number - 1

print(apply(numbers,duplicate))
print(apply(numbers,square))
print(apply(numbers,subtract))
