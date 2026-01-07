"""
Contexto real: tienes que analizar comentarios de usuarios.

Objetivo:
Escribe una función que reciba una cadena de texto y devuelva:
 -Cantidad total de caracteres
 -Cantidad de palabras
 -Cuántas veces aparece la letra "a" (sin importar mayúsculas)
 -Una lista con las palabras que tengan más de 5 letras

Restricciones:
- Usa métodos de cadenas
- Usa for
- No uses librerías externas
"""
def text_cleaner(text):
    """
    Limpia el texto para su analisis
    """
    #Nota: Puede mejorarse usando la libreria re que esta restringida
    return text.replace(",", "").replace(".", "")

def text_analyzer(text):
    """
    Analiza el texto
    """
    text_len = len(text)

    #limpia el texto, crea una lista con todas las palabras y almacena la cantidad de palabras
    clean_text = text_cleaner(text)
    words = clean_text.split()
    word_counter = len(words)

    #Cuenta las letras "a" del texto independientemente se son mayusculas o minusculas
    letter_counter = 0
    for letter in clean_text:
        if letter.lower() == "a":
            letter_counter += 1

    #Se crea una lista donde se almacenan palabras con mas de 5 caracteres
    words_list = [word for word in words if len(word) > 5]

    return text_len, word_counter, letter_counter,words_list

text_to_analyze = input("Ingrese el texto que va a analizar\n:")
total_char, total_words, total_a, lista = text_analyzer(text_to_analyze)
print(f"Total de caracteres en el texto: {total_char}")
print(f"Total de palabras en el texto: {total_words}")
print(f"Total de letras 'a' en el texto: {total_a}")
print(f"lista de palabras con mas de 5 letras: {lista}")
