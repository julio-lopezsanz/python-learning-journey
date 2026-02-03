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
        grouped.setdefault(product, []).append(person)

    return grouped

print(group_data(sales))
