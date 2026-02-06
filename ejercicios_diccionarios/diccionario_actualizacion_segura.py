"""
Dado:

user = {
    "name": "Julio",
    "age": 28
}

Crea una función que:
reciba el diccionario
reciba clave y valor
solo actualice si la clave existe
devuelva siempre el diccionario, exista o no la clave

Prohibido
- Nada de strings de error.
"""

user = {
    "name": "Julio",
    "age": 28
}

def update_dictionary(dictionary,key,value):
    """
    Actualiza el valor de cualquier clave del diccionario, siempre
    y cuando esta exista
    """

    if key in dictionary:
        dictionary[key] = value

    return dictionary

result = update_dictionary(user, "email", "julio")

print(result)
