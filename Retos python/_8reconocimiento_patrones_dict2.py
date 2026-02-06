"""
Devuelve total vendido por persona
"""

sales = [
    ("Ana", 100),
    ("Luis", 200),
    ("Ana", 50),
    ("Luis", 25),
    ("Pedro", 300),
]

def sales_per_person(sales_data):
    """
    Devuelve la cantidad total de compras, por cada cliente
    """

    amount = {}

    for person,total in sales_data:
        #patron: Acumulacion o suma por clave
        amount[person] = amount.get(person, 0) + total

    return amount

print(sales_per_person(sales))
