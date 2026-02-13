"""
Analizar ventas y obtener estadísticas por usuario.
Datos requeridos por usuario:
    -monto total de ventas
    -cantidad de ventas
    -promedio de monto por venta
"""

sales = [
    ("Ana", 100),
    ("Luis", 50),
    ("Ana", 200),
    ("Luis", 150),
    ("Ana", 50),
    ("Pedro", 300)
]

def sales_per_vendor(sales_data):
    """
    Ontiene el monto total de ventas,
    la cantidad total de ventas, y
    el monto promedio de ventas por vendedor
    """

    grouped = {}

    # 1. Acumulación y conteo
    for vendor, amount in sales_data:
        if vendor not in grouped:
            grouped[vendor] = {
                "total": 0,
                "sales_quantity": 0
            }

        grouped[vendor]["total"] += amount
        grouped[vendor]["sales_quantity"] += 1

        #Solucion pythonica:
        #grouped.setdefault(vendor, {"total": 0, "sales_quantity": 0})
        #grouped[vendor]["total"] += amount
        #grouped[vendor]["sales_quantity"] += 1

    # 2. Transformación (promedio)
    for vendor,value in grouped.items():
        total = value["total"]
        count = value["sales_quantity"]
        grouped[vendor]["average"] = round(total / count, 2)

        #Solucion mas pythonica:
        #for value in grouped.values():
            #value["average"] = round(
                #value["total"] / value["sales_quantity"],
                #2
            #)

    return grouped

print(sales_per_vendor(sales))
