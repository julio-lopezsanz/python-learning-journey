"""
Contexto real: sistema mínimo de inventario.

Tienes dos listas:
productos = ["manzana", "banana", "pera"]
cantidades = [10, 3, 0]

Objetivo:
    - Mostrar cada producto con su cantidad usando zip
    - Detectar qué productos están agotados
    - Crear una lista nueva solo con productos disponibles
"""

products = ["manzana", "banana", "pera"]
amounts = [10, 3, 0]

def inventory(products, amounts):
    """ 
    Muestra el producto con su respectiva cantidad, ademas de identificar los
    productos sin existencias, y crear una lista solo de los productos que estan 
    disponibles 
    """
    #Validacion en caso de que cualquiera de las listas este vacia
    #O que la cantidad de elementos difiere entre ambas listas
    if not products or not amounts or len(products) != len(amounts):
        return [], [], []

    registered = []
    available = []
    unavailable = []

    #Utiliza unicamente una de funcion zip y registra todos los productos
    #con sus respectivas cantidad ademas que guarda los productos disponibles,
    #y los no dispobibles. Todo en un solo recorrido
    for product, amount in zip(products, amounts):
        registered.append((product, amount))

        if amount > 0:
            available.append(product)
        else:
            unavailable.append(product)

    #Puede mejorarse con diccionarios
    return registered, available, unavailable

regis_products, avai_products, unavai_products = inventory(products,amounts)
print(f"Productos registrados: {regis_products}")
print(f"Productos disponibles: {avai_products}")
print(f"Productos no disponibles: {unavai_products}")
