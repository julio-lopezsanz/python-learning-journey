"""
Devuelve:
{
    "apple": 10,
    "banana": 6,
    "orange": 13.5
}
"""

products = {
    "apple": [10, 12, 8],
    "banana": [5, 6, 7],
    "orange": [12, 15]
}

def avg_per_producto(product_dict):
    """
    Retorna el promedio de ventas por producto
    """

    return {
        product: round(sum(values) / len(values),2)
        for product, values in product_dict.items()
        if values is not None and values
    }

print(avg_per_producto(products))
