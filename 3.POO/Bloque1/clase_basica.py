"""
Crea una clase Auto con atributos:
    -Marca 
    -Modelo 
    -Año  
    -Velocidad. 
Agrega métodos acelerar(cantidad) y frenar(cantidad) que aumenten o reduzcan la velocidad.
Asegúrate que la velocidad no baje de 0.
"""

class Car:
    """Clase carro"""
    def __init__(self, make, model, year, speed):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def acceleration(self, amount):
        """Aumenta la velocidad del coche"""
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
            print("El carro no puede reducir mas su velocidad")

    def show_car_info(self):
        """Muestra la informacion del carro"""
        print(f"Marca: {self.make}\nModelo: {self.model}\nyear: {self.year}")

car1 = Car("Honda", "Civic", 2007, 180)
car2 = Car("Toyota", "Corolla", 2010, 150)

car1.show_car_info()
car2.show_car_info()

car1.acceleration(40)
car2.acceleration(50)

car1.slow_down(170)
car2.slow_down(200)
car1.slow_down(50)
car2.slow_down(10)
car2.acceleration(10)
