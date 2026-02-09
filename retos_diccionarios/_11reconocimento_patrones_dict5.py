"""
Tienes una lista de ventas.
Cada venta es un diccionario con:

{"vendedor": "Ana", "monto": 120}


Quieren obtener un diccionario donde cada vendedor tenga el total vendido.
"""

sales = [
    {"vendor": "Ana", "amount": 120},
    {"vendor": "Luis", "amount": 50},
    {"vendor": "Ana", "amount": 80}
]

def sales_per_vendor(sales_data):
    """
    Se utiliza el patron de suma por clave.
    Sumara el monto total de ventas por vendedor
    """
    total_sales = {}

    for order in sales_data:

        vendor = order["vendor"]
        amount = order["amount"]

        total_sales[vendor] = total_sales.get(vendor, 0) + amount

    return total_sales

print(sales_per_vendor(sales))
