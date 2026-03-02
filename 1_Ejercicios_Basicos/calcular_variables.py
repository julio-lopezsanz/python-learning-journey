"""
Crea variables: 
    - precio_producto 
    - cantidad 
    - descuento_porcentaje 
Calcula: 
    - subtotal 
    - monto del descuento 
    - total final. 
Imprime todo con formato claro usando f-strings.
"""

PRODUCT_PRICE = 500
PRODUCT_AMOUNT = 5
DISCOUNT_PERCENT = 20

SUBTOTAL = PRODUCT_PRICE * PRODUCT_AMOUNT
DISCOUNT = (SUBTOTAL * DISCOUNT_PERCENT)/100
TOTAL = SUBTOTAL - DISCOUNT 

print(f"Subtotal: {SUBTOTAL}")
print(f"Descuento: {DISCOUNT}")
print(f"Total: {TOTAL}")
