"""
Dado:
keys = ["name", "age", "country"]
values = ["Julio", 28]

Crea una función que:
    - reciba ambas listas
    - si tienen longitudes distintas → devuelva {}
    - si son iguales → devuelva el diccionario correcto
"""

keys = ["name", "age", "country"]
values = ["Julio", 28]

def transform_list_to_dict(keys,values):
    """
    Crea diccionarios apartir de listas. Devuelve un diccionario vacio
    en caso de que no haya la misma cantidad de elementos en ambas listas
    """

    if len(keys) != len(values):
        return {}

    return dict(zip(keys,values))

result = transform_list_to_dict(keys, values)

if not result:
    print("Las listas no tienen la misma cantidad de elementos")
else:
    print(result)
