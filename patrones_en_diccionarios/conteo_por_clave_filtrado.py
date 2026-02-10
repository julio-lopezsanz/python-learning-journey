"""
Tienes esta lista de números:

nums = [1, 3, 2, 3, 4, 1, 2, 3, 5]

Quieres contar solo los números mayores que 2
El resultado debe ser un diccionario con el conteo
"""

nums = [1, 3, 2, 3, 4, 1, 2, 3, 5]

def numbers_counter(list_numbers):
    """
    Filtra los numeros que son mayores a 2
    Crea un diccionario con los numeros mayores a 2 y cuantas veces se repiten en la lista
    todo en una sola pasada
    """
    counter = {}

    for number in list_numbers:
        if number > 2:
            if number in counter:
                counter[number] += 1
            else:
                counter[number] = 1
            #Solucion Pythonic: counter[number] = counter.get(number, 0) + 1

    return counter

print(numbers_counter(nums))
