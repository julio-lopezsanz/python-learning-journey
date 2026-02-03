"""
Devuelve un nuevo diccionario SIN los valores None.
"""

users = {
    "Ana": 20,
    "Luis": None,
    "Pedro": 30,
    "Maria": None
}

def data_cleaner(dict_users):
    """
    Devuelve un diccionario con el nombre del usuario y su valor, siempre
    y cuando este no tenga como valor "none"
    """
    return {user: value for user,value in dict_users.items() if value is not None}

print(data_cleaner(users))
