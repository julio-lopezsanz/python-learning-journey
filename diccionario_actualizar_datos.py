"""
Crea una función que:

    -reciba un diccionario de usuario
    -reciba una clave
    -reciba un nuevo valor
    -actualice el diccionario solo si la clave existe
    -si no existe, no lo modifique

Devuelve el diccionario final.
"""

data = {
    "name": "Julio",
    "age": 28,
    "country": "México"
}

def update_data(data, key, value):
    """
    Actualiza el valor de cualquier clave de un diccionario
    siempre y cuando exista
    
    """
    #Una función debería devolver siempre el mismo tipo de dato,
    #sin importar si todo salió bien o mal.
    if key in data:
        data[key] = value
        return data

    #un metodo comun para evitar devolver un string en caso de error
    if key not in data:
        print("La clave no existe")

print(update_data(data, "name", "Cesar"))
print(update_data(data, "age", 27))
print(update_data(data, "country", "chile"))
print(update_data(data, "email", "julio@jul.com"))
