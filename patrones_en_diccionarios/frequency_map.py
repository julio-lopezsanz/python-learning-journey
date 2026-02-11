"""
Enunciado:

Tienes este texto:

texto = "hola hola mundo hola python mundo"


👉 Quieres un diccionario que muestre la frecuencia de cada palabra.
"""

text1 = "hola hola mundo hola python mundo"

def frequency_words(text):
    """
    Toma un texto, divide cada palabra en una lista, y despues almacena en un
    diccionario, la cantidad de veces que se repite cada palabra en el texto
    """

    words_list = text.split()

    word_counter = {}

    for word in words_list:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1

    return word_counter

print(frequency_words(text1))
