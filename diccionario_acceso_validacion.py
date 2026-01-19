"""
Dado este diccionario:

user = {
    "name": "Julio",
    "age": 28,
    "country": "México"
}
Crea una función que:
    -reciba el diccionario
    -reciba una clave
    -devuelva el valor solo si la clave existe
    -si no existe, devuelva un mensaje claro

No uses try/except todavía.
"""

user = {
    "name": "Julio",
    "age": 28,
    "country": "México"
}

def get_value(user,key):
    """
    obtiene el valor de cualquier clave del diccionario
    siempre y cuando exista
    """
    if key in user:
        return user[key]

    return f"La clave {key} no existe en el diccionario"

print(get_value(user, "name"))
print(get_value(user, "age"))
print(get_value(user, "country"))
print(get_value(user, "email"))
