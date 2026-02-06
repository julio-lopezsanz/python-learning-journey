"""
Métodos iterables (aterrizados)

Objetivo:
    -Dada una lista de números:
    -Usa enumerate para mostrar índice y valor
    -Crea una nueva lista con el cuadrado de cada número
    -Hazlo primero con for
    -Luego intenta con una expresión lambda
"""

numbers = [2,4,6,8,10,12,14]

for index,num in enumerate(numbers,start=1):
    print(f"{index}. {num}")

#Lista comprimida que crea una nueva lista con numeros al cuadrado
#Nota: En python real, es preferible este metodo al escrito con lambda
exp_numbers = [num*num for num in numbers]
print(f"\n{exp_numbers}")

#lista creada usando funciones anonimas lambda
#Este metodo es mas recomendable usarlo, cuando la funcion ya existe y no cuando se crea
#por ejemplo: list(map(abs, numbers))
exp_numbers2 = list(map(lambda num: num ** 2, numbers))
print(f"\n{exp_numbers2}")
