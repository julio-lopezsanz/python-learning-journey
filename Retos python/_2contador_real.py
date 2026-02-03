"""
words = ["python", "java", "python", "c++", "java", "python"]

Devuelve:
{
  "python": 3,
  "java": 2,
  "c++": 1
}

Reglas:
- no count()
- no librerías
"""

words = ["python", "java", "python", "c++", "java", "python"]

def word_counter(words_list):
    """
    Cuenta cuantas veces se repite un elementos, dentro de una lista
    y devuelve un diccionario con el resultado
    """
    #Crea el diccionario vacio donde se almacenara el resultado
    counts = {}

    for word in words_list:
        #Si la palabra ya existe en el diccionario, súmale 1.
        #Si no existe, créala empezando en 1.
        counts[word] = counts.get(word, 0) + 1

    return counts

print(word_counter(words))
