"""
Tienes esta lista de palabras:

palabras = ["sol", "luna", "mar", "cielo", "mesa", "sal"]


Quieres un diccionario que agrupe las palabras por su longitud.
"""

words = ["sol", "luna", "mar", "cielo", "mesa", "sal"]

def group_words(words_list):
    """
    Agrupa las palabras de la lista, dependiendo de la longitud de cada una de las palabras
    """

    grouped = {}

    for word in words_list:
        length = len(word)
        if length not in grouped:
            grouped[length] = []

        grouped[length].append(word)

        #Solucion Pythonic: grouped.setdefault(length, []).append(word)

    return grouped

print(group_words(words))
