"""
De esta lista:
[2, 5, 8, 11, 14, 17]

Crea una nueva lista que contenga el cuadrado de los números pares.

(Esto obliga a: filtrar + transformar)
"""
numbers = [2,5,8,11,14,17]

#Solucion con comprension
new_numbers = [num**2 for num in numbers if num % 2 == 0]
print(new_numbers)


#Solucion con map y filter

#filtrando los numeros pares
filtred_numbers = list(filter(lambda num: num % 2 == 0, numbers))

#transformando la lista filtrada, elevando sus numeros al cuadrado
squaring_numbers = list(map(lambda num: num**2, filtred_numbers))

print(squaring_numbers)
