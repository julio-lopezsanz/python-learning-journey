"""
prices = {
    "apple": 10,
    "banana": 5,
    "orange": 12,
    "pear": 7
}

Devuelve solo los productos que cuesten más de 8.
"""

prices = {
    "apple": 10,
    "banana": 5,
    "orange": 12,
    "pear": 7
}

def filter_products_by_price(prices):
    """
    Devuelve un nuevo diccionario con productos cuyo precio es mayor a 8
    """
    return {product: price for product, price in prices.items() if price > 8}

print(filter_products_by_price(prices))
