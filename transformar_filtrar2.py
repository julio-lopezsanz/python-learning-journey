"""
De esta lista:
["sol", "luna", "estrella", "cielo", "mar"]

Crea una nueva lista con las palabras que:
    -tengan más de 4 letras
    -estén en mayúsculas
"""
words = ["sol", "luna", "estrella", "cielo", "mar"]

#Solucion con comprension de lista
new_words = [word for word in words if len(word) > 4 and word.isupper()]
print(new_words)

#Solucion con filter y lambda

#filtramos palabras con mas de 4 digitos y mayusculas
filtred_words = list(filter(lambda word: len(word) > 4 and word.isupper(), words))
print(filtred_words)

#NOTA IMPORTANTE: Nunca cambies la lógica para forzar un resultado.
#Cambia los datos o acepta el resultado. Si la lista es vacia, ese
#es el resultado
