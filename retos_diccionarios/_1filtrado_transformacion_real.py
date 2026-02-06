"""
numbers = [3, 10, 15, 20, 25, 30]

Devuelve una lista con:
- solo los mayores de 15
- de esos, solo pares
- multiplicados por 2

Restricción:
- no for explícito
- sin librerias
"""

numbers = [3, 10, 15, 20, 25, 30]

def number_filter(numbers_list):
    """
    Filtra una lista de numeros con los siguientes criterios:
        -Solo numeros mayor a 15
        -Solo numeros pares
    """

    #filtra y duplica en una sola linea
    return [num * 2 for num in numbers_list if num > 15 and num % 2 == 0]

result = number_filter(numbers)

if not result:
    print("la lista que uso como parametros esta vacia")
else:
    print(result)
