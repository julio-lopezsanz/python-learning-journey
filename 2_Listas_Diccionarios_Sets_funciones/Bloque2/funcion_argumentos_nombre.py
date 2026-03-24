"""
Crea una función registrar_producto() 
    - Que reciba datos del producto con **kwargs
    - imprima cada dato. 
Llámala con: nombre, precio, categoría y stock.
"""
#def funcion(**kwargs) - Genérico — cuando la función acepta cualquier dato
def add_product(**product_data):
    """Registra un producto"""
    for key, value in product_data.items():
        print(f"{key}: {value}")

add_product(name = "Audifonos",price = 10.99,category = "Tecnologia", stock = 10 )
