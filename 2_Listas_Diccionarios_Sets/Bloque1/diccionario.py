"""
Crea un diccionario que represente un producto de tienda con: 
    - nombre
    - precio
    - stock 
    - categoría
Luego imprime cada dato con su clave.
"""

product = {
    "name": "Audifonos",
    "price": 5.99,
    "stock": 20,
    "category": "Tecnologia"
}

print(product["name"])
print(product["price"])
print(product["stock"])
print(product["category"])

#Forma mas limpia de imprimir un diccionario
for key, value in product.items():
    print(f"{key}: {value}")
