"""
Dado:

data = {
    "a": 1,
    "b": 2,
    "c": 3
}


Crea una función que:
    - intercambie claves y valores
    - devuelva el nuevo diccionario

Resultado:
{1: "a", 2: "b", 3: "c"}
"""

data = {
    "a": 1,
    "b": 2,
    "c": 3
}

def dictionary_inverter(dictionary):
    """
    invierte las clave y valores en un diccionario
    """

    return {value: key for key, value in dictionary.items()}

print (dictionary_inverter(data))
