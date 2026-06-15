"""
Crea 4 funciones: 
    - calcular_area_circulo(radio)
    - calcular_area_rectangulo(base, altura)
    - calcular_hipotenusa(a, b)
    - es_primo(numero) Saber si el numero es primo
Prueba cada una con al menos 3 valores distintos.
"""
PI = 3.1416
def calculate_area_circle(radius):
    """
    Calcula el area de un circulo
    """
    return round(PI * (radius ** 2),2)

def calculate_area_rectangle(length, width):
    """
    Calcula el area de un rectangulo
    """
    return  round(length * width,2)

def calculate_hypotenuse(a,b):
    """
    Calcula la hipotenusa de un triangulo a partir de sus catetos
    """
    return round(((a**2) + (b**2)) ** 0.5,2)

def is_prime(number):
    """
    Comprueba si un numero es primo
    """
    if number < 2:
        return False

    for i in range(2,number):
        if number % i == 0:
            return False

    return True

print("\nResultado")
print(f"\n Area de un circulo: {calculate_area_circle(2)}")
print(f"\n Area de un circulo: {calculate_area_circle(5)}")
print(f"\n Area de un circulo: {calculate_area_circle(7)}")
print(f"\n Area de un rectangulo: {calculate_area_rectangle(1.4,2.5)}")
print(f"\n Area de un rectangulo: {calculate_area_rectangle(3.5,4.7)}")
print(f"\n Area de un rectangulo: {calculate_area_rectangle(5.4,6.6)}")
print(f"\n Hipotenusa de un triangulo: {calculate_hypotenuse(6,7)}")
print(f"\n Hipotenusa de un triangulo: {calculate_hypotenuse(8,9)}")
print(f"\n Hipotenusa de un triangulo: {calculate_hypotenuse(10,11)}")
print(f"\n ¿Es un numero primo?: {is_prime(7)}")
print(f"\n ¿Es un numero primo?: {is_prime(11)}")
print(f"\n ¿Es un numero primo?: {is_prime(37)}")
print(f"\n ¿Es un numero primo?: {is_prime(1)}")
print(f"\n ¿Es un numero primo?: {is_prime(6)}")
print(f"\n ¿Es un numero primo?: {is_prime(8)}")
