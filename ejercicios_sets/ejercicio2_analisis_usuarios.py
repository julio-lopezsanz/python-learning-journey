"""
Dada esta lista:

users = ["Ana", "Luis", "Ana", "Pedro", "Luis", "Pedro", "Sofia"]

Haz una función que devuelva:
    - El set de usuarios únicos
    - El set de usuarios duplicados
    - Prohibido usar count()
    - Usa dos sets
"""

users = ["Ana", "Luis", "Ana", "Pedro", "Luis", "Pedro", "Sofia"]

def analyze_users(users_list):
    """
    Devuelve dos sets: usuarios únicos y usuarios duplicados.
    """

    unique = set()
    duplicate = set()

    for user in users_list:
        if user in unique:
            duplicate.add(user)
        else:
            unique.add(user)

    return unique, duplicate

print(analyze_users(users))
