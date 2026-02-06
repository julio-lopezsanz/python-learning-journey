"""
De esta lista:
[4, 7, 10, 15, 23, 50]

Crea una nueva lista solo con los números mayores a 10.

Hazlo:
    -con for
    -con comprensión
    -con filter
"""
numbers = [4,7,10,15,23,50]

#Creando una lista con for
new_numbers = []

for num in numbers:
    if num > 10:
        new_numbers.append(num)

print(new_numbers)

#Creando una lista con comprension
comprehension_numbers = [num for num in numbers if num > 10]

print(comprehension_numbers)

#Creando una lista filtrada con filter
filt_numbers = list(filter(lambda num: num > 10, numbers))
print(filt_numbers)
