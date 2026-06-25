"""
Author: Julio Cesar Lopez Sanchez
Problema: Escribe un programa en Python para crear una clase «Product» 
          con tres atributos de instancia: nombre, precio y cantidad. 
          Añade un método total_value() que devuelva el valor total de las existencias 
          multiplicando el precio por la cantidad.
"""

class Product:
    """Clase para representar un producto con su nombre, precio y cantidad en inventario."""
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Inicializa un producto, con su nombre, su precio y la cantidad de este

        Args: 
            name (str): El nombre del producto
            price (float): El precio del producto
            quantity (int): Cantidad de productos disponibles en el inventario

        Raises:
            ValueError: Si price es menor o igual a 0
        """
        if price <= 0:
            raise ValueError("El precio no puede ser negativo ni 0")
        if quantity < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self) -> float:
        """Calcula El valor total de los productos almacenados en el inventario
                
        Returns:
            float: Valor total del producto almacenado en inventario.
        """

        return self.price * self.quantity

def main() -> None:
    """Funcion principal"""
    product1 = Product("Audifonos", 5.99, 5)
    print(f"Valor total de {product1.name} en inventario es: {product1.total_value():.2f}")

    product2 = Product("Laptops", 99.99, 20)
    print(f"Valor total de {product2.name} en inventario es: {product2.total_value():.2f}")

if __name__ == "__main__":
    main()
