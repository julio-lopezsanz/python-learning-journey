"""
Enunciado:

Tienes este texto:

texto = "Hola, hola! Mundo mundo PYTHON python."


Quieres contar la frecuencia de palabras, pero:
    - ignorando mayúsculas / minúsculas
    - ignorando signos de puntuación
"""
import string

text1 = "Hola, hola! Mundo mundo PYTHON python."

def normalize_text(text_to_normalize):
    """
    Normaliza el texto.
    """

    normal_text = text_to_normalize.translate(str.maketrans('', '', string.punctuation)).lower()

    return normal_text

def words_counter(text):
    """
    Normaliza el texto, para despues separarlo en una lista
    la cual se utilizara para realizar el conteo de palabras
    de dicha lista
    """
    normalized_text = normalize_text(text)

    word_list = normalized_text.split()

    word_counter = {}

    for word in word_list:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1

    return word_counter


print(words_counter(text1))
