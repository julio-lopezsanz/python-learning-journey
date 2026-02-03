"""
Devuelve:
{
  "Laptop": ["Ana", "Pedro", "Luis"],
  "Mouse": ["Luis", "Ana"]
}
"""

sales = [
    ("Ana", "Laptop"),
    ("Luis", "Mouse"),
    ("Ana", "Mouse"),
    ("Pedro", "Laptop"),
    ("Luis", "Laptop")
]

def group_data(sales_data):
    """
    Agrupa las ventas por producto y devuelve un diccionario con compradores por producto.
    """

    grouped = {}

    for person, product in sales_data:
        #Si el producto no existe, créalo con una lista vacía.
        #Luego mete la persona en esa lista.
        grouped.setdefault(product, []).append(person)

    return grouped

print(group_data(sales))
