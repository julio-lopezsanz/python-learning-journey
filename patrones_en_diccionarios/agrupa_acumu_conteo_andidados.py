"""
Tienes una lista de registros de ventas con este formato:

sales = [
    ("Ana", "manzana", 10),
    ("Luis", "pera", 5),
    ("Ana", "pera", 7),
    ("Ana", "manzana", 3),
    ("Luis", "manzana", 8),
    ("Pedro", "pera", 4),
    ("Pedro", "pera", 6)
]

Objetivo
    - Construir una función que devuelva un diccionario con esta estructura:

{
    "Ana": {
        "manzana": {"total": 13, "ventas": 2},
        "pera": {"total": 7, "ventas": 1}
    },
    "Luis": {
        "pera": {"total": 5, "ventas": 1},
        "manzana": {"total": 8, "ventas": 1}
    },
    "Pedro": {
        "pera": {"total": 10, "ventas": 2}
    }
}
"""

sales = [
    ("Ana", "manzana", 10),
    ("Luis", "pera", 5),
    ("Ana", "pera", 7),
    ("Ana", "manzana", 3),
    ("Luis", "manzana", 8),
    ("Pedro", "pera", 4),
    ("Pedro", "pera", 6)
]

def sales_per_vendor(sales_data):
    """
        Agrupa ventas por vendedor y producto,
        acumulando cantidad total y número de ventas.
    """

    grouped = {}

    for vendor, product, quantity in sales_data:

        if vendor not in grouped:
            grouped[vendor] = {}

        if product not in grouped[vendor]:
            grouped[vendor][product] = {
                "total" : 0,
                "sales" : 0
                }

        grouped[vendor][product]["total"] += quantity
        grouped[vendor][product]["sales"] += 1

        #Solucion pythonic:
        #grouped.setdefault(vendor, {})
        #grouped[vendor].setdefault(
        #    product,
        #    {"total": 0, "sales": 0}
        #)
        #grouped[vendor][product]["total"] += quantity
        #grouped[vendor][product]["sales"] += 1
    return grouped

print(sales_per_vendor(sales))
