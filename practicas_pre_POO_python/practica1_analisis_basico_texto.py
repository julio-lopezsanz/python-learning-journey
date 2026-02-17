"""
Dado un texto:
    - contar palabras
    - contar letras
    - manejar texto vacío con excepciones
"""
import re
import string

text = "¡Hoy es un maravilloso dia!, ¡Vamos a esforzarnos por aprender!"

def text_cleaner(text_to_clean):
    """
    Vuelve el texto en minusculas y
    limpia el texto de espacios y signos de puntuacion.
    """
    #Volvemos el texto a minusculas
    clean_text = text_to_clean.lower()

    #eliminamos las puntuaciones
    clean_text = clean_text.translate(str.maketrans('', '', string.punctuation))

    #eliminamos caracteres especiales
    clean_text = re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]', '', clean_text)

    return clean_text

def word_letter_counter(text_to_count):
    """
    Cuenta las palabras y letras de un texto
    """
    #manejamos en caso de que el texto este vacio
    if not text_to_count:
        return {}

    clean_text = text_cleaner(text_to_count)
    total_word = len(clean_text.split())
    total_letters = len(clean_text.replace(" ", ""))

    return {
        "words" : total_word,
        "letters" : total_letters
    }
    
print(word_letter_counter(text))
