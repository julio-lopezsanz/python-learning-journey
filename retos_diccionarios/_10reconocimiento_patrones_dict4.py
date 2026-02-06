"""
Devuelve los precios con IVA 16% agregado.
"""

prices = {
    "apple": 10,
    "banana": 5,
    "orange": 8
}

def add_taxes(products_prices):
    """
    Agrega el impuesto del 16% al precio de los productos registrados
    """

    #patron de transformacion de datos
    return {
        product: round(price * 1.16,2)
        for product, price in products_prices.items()
    }

print(add_taxes(prices))
