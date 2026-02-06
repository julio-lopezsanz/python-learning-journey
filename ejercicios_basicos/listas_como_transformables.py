"""
Dada una lista de números:
[1, 2, 3, 4, 5]
Crea una nueva lista con cada número multiplicado por 3.

Hazlo:
    -primero con for
    -luego con comprensión de listas
    -luego con map + lambda
"""

numbers = [1,2,3,4,5]

#Creando una lista con for
new_numbers = []

for num in numbers:
    new_numbers.append(num*3)

print(new_numbers)

#Creando una lista con comprension de lista
comprehension_numbers = [num*3 for num in numbers]

print(comprehension_numbers)

#creando una lista con map y lambda
lambmap_numbers = list(map(lambda num: num*3, numbers))
print(lambmap_numbers)
