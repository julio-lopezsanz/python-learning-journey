"""
Tienes esta lista de usuarios, ordénalos por edad de mayor a menor:
usuarios = [
    {"nombre": "Ana", "edad": 30},
    {"nombre": "Luis", "edad": 22},
    {"nombre": "Maria", "edad": 27}
]
"""

users = [
    {"nombre": "Ana", "edad": 30},
    {"nombre": "Luis", "edad": 22},
    {"nombre": "Maria", "edad": 27}
]

sorted_by_age = sorted(users,key = lambda u: u["edad"], reverse=True)
print(sorted_by_age)
