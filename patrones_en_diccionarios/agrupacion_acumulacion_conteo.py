"""
Tienes una lista de tuplas (usuario, monto) y quieres:

un diccionario donde cada usuario tenga:
    - el total gastado
    - el número de compras
"""

sales = [
    ("Ana",40),
    ("Luis",50),
    ("Ana",40),
    ("Ana",40)
]

def purchases_per_person(sales_data):
    """
    Devuelve un diccionario con:
        - monto total de compras y cantidad total de compras por persona
    """

    grouped = {}

    for user, amount in sales_data:
        if user not in grouped:
            grouped[user] = {"total": 0, "purchases": 0}

        grouped[user]["total"] += amount
        grouped[user]["purchases"] += 1

    #solucion pythonica:
    #data = grouped.get(user, {"total": 0, "purchases": 0})
        #data["total"] += amount
        #data["purchases"] += 1
        #grouped[user] = data

    return grouped

print(purchases_per_person(sales))
