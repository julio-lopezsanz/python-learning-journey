"""
Dadas dos listas:
keys = ["name", "age", "country"]
values = ["Julio", 28, "México"]

Crea un diccionario que las combine correctamente.
"""

keys = ["name", "age", "country"]
values = ["Julio", 28, "México"]

user = dict(zip(keys,values))

print(user)
