"""
Devuelve:
{
    "Ana": 150,
    "Luis": 200,
    "Pedro": 300
}
"""

orders = [
    {"user": "Ana", "total": 100},
    {"user": "Luis", "total": 200},
    {"user": "Ana", "total": 50},
    {"user": "Pedro", "total": 300},
]

def purchases_per_user(orders_dict):
    """
    Agrupa y suma compras por cliente
    """
    #Diccionario donde agruparemos el resultado
    totals = {}

    for order in orders_dict:
        #saca el nombre del usuario
        user = order["user"]
        #saca el total de compra del usuario
        total = order["total"]

        #Si el usuario ya existe, se sumara su compra.
        #Si no existe, se crea empezando en 0.
        totals[user] = totals.get(user, 0) + total

    return totals


print(purchases_per_user(orders))
