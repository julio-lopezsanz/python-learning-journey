"""
Dada esta lista de compras:
items = ["apple", "banana", "apple", "orange", "banana", "apple", "pear"]

Crea una función que:
    - reciba la lista
    - devuelva un diccionario con la cantidad de cada producto
    - no use count()
    - no modifique la lista original
"""

items = ["apple", "banana", "apple", "orange", "banana", "apple", "pear"]

def count_items(list_items):
    """
    Toma una lista, y la convierte en un diccionario, usandos sus elementos como claves,
    y cuantas veces se repite en dicha lista, como su valor
    """

    counts = {}

    for word in list_items:
        counts[word] = counts.get(word, 0) + 1

    #Nota: aqui devuelve incluso si esta vacio
    return counts

result = count_items(items)

if not result:
    print("La lista que se usa como parametro esta vacia")
else:
    print(result)
