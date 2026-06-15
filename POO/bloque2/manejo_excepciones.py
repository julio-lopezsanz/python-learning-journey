"""
Modifica la clase Car para que maneje errores correctamente:

Si se intenta acelerar con un valor negativo, lanza un ValueError
Si se intenta frenar más de la velocidad actual, lanza un error personalizado VelocidadInvalidaError
Usa try/except al llamar los métodos
"""
class InvalidSpeedError(Exception):
    """Error personalizado en caso de velocidad invalida"""
    def __init__(self, amount, speed):
        self.amount = amount
        self.speed = speed
        super().__init__("Velocidad invalida. no puedes desacelerar mas que la velocidad actual")

class Car:
    """
    Representa un automóvil con sus datos y comportamiento básico.

    Atributos:
        make (str): Marca del carro
        model (str): Modelo del carro
        year (int): Año de fabricación
        speed (float): Velocidad actual en KM/H
    """
    def __init__(self, make, model, year, speed):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def acceleration(self, amount):
        """Aumenta la velocidad del coche"""
        if amount < 0:
            raise ValueError("No se permiten valores negativos")

        self.speed += amount
        print(f"El carro acelera a {self.speed}KM/H")

    def slow_down(self, amount):
        """Reduce la velocidad del coche"""
        if self.speed - amount > 0:
            self.speed -= amount
            print(f"El carro desacelera a {self.speed}KM/H")
        elif self.speed - amount == 0:
            self.speed -= amount
            print("El carro se ha detenido")
        else:
            raise InvalidSpeedError(amount, self.speed)

    def show_car_info(self):
        """Muestra la informacion del carro"""
        print(f"Marca: {self.make}\nModelo: {self.model}\nyear: {self.year}")

car1 = Car("Honda", "Civic", 2007, 180)
car2 = Car("Toyota", "Corolla", 2010, 150)

car1.show_car_info()
car2.show_car_info()

try:
    car1.acceleration(-20)
    car1.slow_down(210)
except InvalidSpeedError as e:
    print(f"Error: {e}")
except ValueError as ex:
    print(f"Error: {ex}")
