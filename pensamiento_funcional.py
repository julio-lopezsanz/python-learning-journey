"""
Dada:
[1, 2, 3, 4, 5]

Genera:
[1, 4, 9, 16, 25]
pero no uses for explícito.
"""

numbers = [1, 2, 3, 4, 5]

#solucion con comprension
new_numbers = [num**2 for num in numbers]

#solucion con map y lambda
new_numbers2 = list(map(lambda num: num**2, numbers))

print(new_numbers)
print(new_numbers2)
