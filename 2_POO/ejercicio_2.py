"""
Author: Julio Cesar Lopez Sanchez
Problema: Crea una clase Vehiculo con atributos de marca y velocidad_actual
        un metodo acelerar que aumenta la velocidad_actual
        y un metodo frenar que disminuye la velocidad_actual
        Crea una clase Motocicleta que herede de Vehiculo y agrega un atributo de cilindrada
"""

class Vehicle:
    """
    Clase para representar un vehículo con operaciones de aceleración y frenado.
    """
    def __init__(self, brand: str) -> None:
        self.brand = brand
        self.current_speed = 0

    def speed_up(self, speed: int) -> None:
        """
        Aumenta la velocidad actual del vehículo.

        Args:
            speed (int): Cantidad a aumentar la velocidad actual

        """
        self.current_speed += speed

    def slow_down(self, speed: int) -> None:
        """
        Disminuye la velocidad actual del vehículo.

        Args:
            speed (int): Cantidad a disminuir la velocidad actual

        Raises:
            ValueError: Si la desminucion da un resultado negativo.
        """
        if self.current_speed - speed < 0:
            raise ValueError("La velocidad no puede ser negativa")
        self.current_speed -= speed

class Motorcycle(Vehicle):
    """Clase para representar una motocicleta."""

    def __init__(self, brand: str, displacement: int) -> None:
        super().__init__(brand)
        self.displacement = displacement

def main() -> None:
    """Funcion principal"""
    car_honda = Vehicle("Honda")
    print(f"Marca de carro: {car_honda.brand}")

    car_honda.speed_up(100)
    print(f"El carro acelero a: {car_honda.current_speed}")

    car_honda.slow_down(25)
    print(f"El carro desacelero a: {car_honda.current_speed}")

    bike_honda = Motorcycle("Honda", 250)
    print(f"Marca de motocicleta: {bike_honda.brand}")

    bike_honda.speed_up(150)
    print(f"La motocicleta acelero: {bike_honda.current_speed}")

    bike_honda.slow_down(100)
    print(f"La motocicleta desacelero: {bike_honda.current_speed}")

if __name__ == "__main__":
    main()
