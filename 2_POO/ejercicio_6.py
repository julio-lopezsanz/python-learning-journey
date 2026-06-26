"""
Author: Julio Cesar Lopez Sanchez
Problema: Crea una clase Battery que tenga un atributo de nivel de carga y un metodo para 
          consumir carga.
          Crea una clase Vehicle que tenga un atributo de marca y un objeto de tipo Battery.
"""

class Battery:
    """Representa la batería de un vehículo con nivel de carga."""

    def __init__(self, capacity: int) -> None:
        """Inicializa la batería con una capacidad dada.

        Args:
            capacity: Capacidad máxima de carga de la batería.

        Raises:
            ValueError: Si la capacidad es negativa.
        """
        if capacity < 0:
            raise ValueError("La capacidad de la batería no puede ser negativa")
        self.capacity = capacity        
        self.charge_level = capacity  # inicia con carga completa

    def consume(self, amount: int) -> None:
        """Consume carga de la batería.

        Args:
            amount: Cantidad de carga a consumir.

        Raises:
            ValueError: Si el consumo deja la carga por debajo de 0.
        """
        if self.charge_level - amount < 0:
            raise ValueError("No hay suficiente carga en la batería")
        self.charge_level -= amount

    def is_dead(self) -> bool:
        """Indica si la batería está completamente descargada."""
        return self.charge_level == 0


class Vehicle:
    """Clase para representar un vehículo con operaciones de aceleración y frenado.

    Además, tiene una batería que se consume al arrancar.

    Args:
        brand: Marca del vehículo.
        battery_capacity: Capacidad de la batería del vehículo.
    """
    def __init__(self, brand: str, battery_capacity: int) -> None:
        self.brand = brand
        self.current_speed = 0
        self.battery = Battery(battery_capacity)  # Vehicle TIENE una Battery

    def start(self) -> None:
        """Arranca el vehículo, consumiendo carga de la batería."""
        if self.battery.is_dead():
            raise ValueError(f"No se puede arrancar '{self.brand}': batería agotada")
        self.battery.consume(10)
        print(f"{self.brand} arrancado correctamente")

class Motorcycle(Vehicle):
    """Clase para representar una motocicleta.
    Hereda de Vehicle y agrega un atributo de cilindrada.
    Args:
        brand: Marca de la motocicleta.
        battery_capacity: Capacidad de la batería.
        displacement: Cilindrada de la motocicleta.
    """
    def __init__(self, brand: str, battery_capacity: int, displacement: int) -> None:
        super().__init__(brand, battery_capacity)  # <- AQUÍ se crea self.battery
        self.displacement = displacement

def main() -> None:
    """Función principal para probar las clases Vehicle y Motorcycle."""
    car_honda = Vehicle("Honda", 100)
    print(f"Marca de carro: {car_honda.brand}")

    car_honda.start()
    print(f"Nivel de batería después de arrancar: {car_honda.battery.charge_level}")

    bike_honda = Motorcycle("Honda", 50, 250)
    print(f"Marca de motocicleta: {bike_honda.brand}, Cilindrada: {bike_honda.displacement}")

    bike_honda.start()
    print(f"Nivel de batería después de arrancar la moto: {bike_honda.battery.charge_level}")

if __name__ == "__main__":
    main()
