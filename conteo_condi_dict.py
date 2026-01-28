"""
numbers = [1,2,2,3,3,3,4,4,4,4]

Devuelve un diccionario solo con los números que aparezcan MÁS de una vez.
"""

numbers = [1,2,2,3,3,3,4,4,4,4]

def count_items(list_items):
    """
    Hace el conteo de elementos de una lista, y devuelve un diccionario con 
    los valores que aparezcan mas de una vez
    """
    #Devuelve un diccionario vacio en caso de que la lista este vacia
    if not list_items:
        return {}

    #crea un diccionario, en donde las claves son los elementos de la lista
    #y los valores son las veces que este se repite en dicha lista
    counts = {}
    for number in list_items:
        counts[number] = counts.get(number, 0) + 1

    #retorna un diccionario a partir del diccionario creado anteriormente
    #con una condicion en especifico
    return {num: value for num, value in counts.items() if value > 1}

print(count_items(numbers))
