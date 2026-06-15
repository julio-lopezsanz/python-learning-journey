"""
Crea una clase base Figura con un método area(). 
Luego crea dos clases que hereden de ella: 
Rectangulo y Circulo, cada una calculando su propia área.
"""

import math

class Figure:
    """Clase generica para figuras geometricas"""

    def area(self):
        """Metodo generico para las areas de cada figura"""

class Rectangle(Figure):
    """Calcula el area de un rectangulo"""
    def __init__(self ,width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

class Circle(Figure):
    """Calcula el area de un circulo"""
    def __init__(self ,radius):
        self.radius = radius

    def area(self):
        return (self.radius**2) * math.pi

figures = [Rectangle(7, 8), Circle(8)]

for fig in figures:
    print(f"{fig.__class__.__name__}: {fig.area():.2f}")
