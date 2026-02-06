"""
Dado un diccionario:

user = {
    "name": "Julio",
    "age": 28,
    "country": "México"
}

Crea una función que:
    -reciba el diccionario
    -reciba una clave
    -devuelva siempre el mismo tipo
    -si la clave existe → devuelve el valor
    -si no existe → devuelve None

Prohibido:
    -strings de error
    -print dentro de la función
"""

user = {
    "name": "Julio",
    "age": 28,
    "country": "México"
}

def get_value(data,key):
    """
    Toma el diccionario y una clave y devuelve el valor de la clave, siempre
    y cuando esta exista, del caso contrario, devuelve none
    """
    if key in data:
        return data.get(key)

result = get_value(user,"email")

if result is None:
    print("La clave no existe.")
else:
    print(result)
