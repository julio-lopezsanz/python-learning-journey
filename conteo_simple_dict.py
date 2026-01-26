"""
Dada una lista:
words = ["sol", "luna", "sol", "cielo", "luna", "sol"]

Crea una función que:
    - devuelva un diccionario
    - cada palabra sea clave
    - su valor sea cuántas veces aparece

Prohibido:

    -No uses collections.
"""
words = ["sol", "luna", "sol", "cielo", "luna", "sol"]

def simple_count(lista):
    """
    Crea un diccionario a partir de una lista. con las palabras almacenadas en esta,
    como claves, y las veces que aparece en dicha lista como valores
    """
    if not lista:
        return {}

    #Crea un diccionario vacio
    counts = {}
    #recorre la lista
    for word in lista:
        #Si existe, se suma 1. si no vuelve a aparecer se queda en 1
        counts[word] = counts.get(word, 0) + 1
    return counts

result = simple_count(words)

if not result:
    print("La lista que se uso esta vacia")
else:
    print(result)
