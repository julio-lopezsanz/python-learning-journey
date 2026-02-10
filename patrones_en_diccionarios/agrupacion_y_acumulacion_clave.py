"""
Tienes esta lista de compras:

compras = [
    ("Ana", "manzana", 2),
    ("Luis", "pera", 1),
    ("Ana", "pera", 3),
    ("Luis", "manzana", 2),
    ("Ana", "manzana", 1)
]

Quieres obtener un diccionario donde:
    - la clave sea la persona
    - el valor sea otro diccionario
    - ese diccionario interno tenga:
    - producto → cantidad total comprada
"""

purchases = [
    ("Ana", "manzana", 2),
    ("Luis", "pera", 1),
    ("Ana", "pera", 3),
    ("Luis", "manzana", 2),
    ("Ana", "manzana", 1)
]

def purchases_per_user(purchases_dict):
    """
    Devuelve un diccionario con las compras de cada usuario, en relacion a los
    productos que compro y sus cantidades totales
    """

    grouped = {}

    for name, product, amount in purchases_dict:
        if name not in grouped:
            grouped[name] = {}
        if product in grouped[name]:
            grouped[name][product] += amount
        else:
            grouped[name][product] = amount
        #Solucion Pythonic:
        #grouped.setdefault(name, {})
        #grouped[name][product] = grouped[name].get(product, 0) + amount

    return grouped

print(purchases_per_user(purchases))
