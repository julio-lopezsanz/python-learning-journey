"""
Lee e imprime el archivo json "productos"
"""

import json
import os

current_dir = os.path.dirname(__file__)
route = os.path.join(current_dir, "productos.json")

products = [
    {"product": "Audifonos", "price": 5.99},
    {"product": "Microfono", "price": 10.99},
    {"product": "Teclado", "price": 3.99}
]

with open(route, "w", encoding="utf-8") as file:
    json.dump(products, file, indent=4)

with open(route, "r", encoding="utf-8") as file:
    productos = json.load(file)
    for producto in productos:
        print(f"Producto: {producto['product']} | Precio: ${producto['price']}")
