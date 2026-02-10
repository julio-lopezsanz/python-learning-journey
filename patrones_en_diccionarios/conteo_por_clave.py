"""
Tienes esta lista de palabras:

palabras = ["gato", "perro", "gato", "ave", "perro", "gato"]

Se quiere obtener un diccionario que indique cuántas veces aparece cada palabra.
"""

words = ["gato", "perro", "gato", "ave", "perro", "gato"]

def words_counter(list_words):
    """
    Recorre la lista, almacena las repeticiones de palabras en un diccionario
    y lo devuelve.
    """
    counter = {}

    for word in list_words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1

    #Solucion mas pythonic: counter[word] = counter.get(word, 0) + 1

    return counter

print(words_counter(words))
