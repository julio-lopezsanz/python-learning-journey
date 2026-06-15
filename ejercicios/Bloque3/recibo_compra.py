"""
Pide: 
    - nombre del producto 
    - precio unitario
    - cantidad 
Calcula y muestra un recibo con: 
    - nombre del producto 
    - precio unitario formateado con 2 decimales 
    - cantidad 
    - subtotal 
    - IVA (16%) 
    - total 
Alinea los números a la derecha.
"""

product_name = input("\nIngrese el nombre del producto: ")
product_price = float(input("\nIngrese el precio unitario del producto: "))
product_quantity = int(input("\nIngrese la cantidad de productos comprados: "))
subtotal = product_price * product_quantity
iva = subtotal * 0.16
total = subtotal + iva

print("\n---------------Recibo de compra---------------\n")
print(f"\nProducto: {product_name:>16}")
print(f"\nPrecio: {product_price:>19.2f}")
print(f"\nCantidad: {product_quantity:>12}")
print(f"\nSubtotal: {subtotal:>17.2f}")
print(f"\nIva (16%): {iva:>15.2f}")
print(f"\nTotal: {total:>20.2f}")
