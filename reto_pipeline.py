"""
Dada esta lista:
numbers = [3, 7, 12, 18, 5, 20, 1, 15]

Debes generar una nueva lista que cumpla todo esto:
    -Solo números mayores que 10
    -De esos, toma solo los pares
A esos números:
    -elévalos al cuadrado
A cada resultado:
    -réstale 5

Restricciones
    -No uses for explícito.
Solo puedes usar:
    -comprensión de listas
    -map / filter
    -una mezcla de ambos
No se vale hacerlo en varios pasos con variables intermedias si puedes evitarlo.
"""

numbers = [3, 7, 12, 18, 5, 20, 1, 15]

def apply(numbers, func):
    """
    Genera una lista con numeros pares mayores a 10
    luego los eleva al cuadrado y le resta el valor de 5
    """
    return [func(num) - 5 for num in numbers if num > 10 and num % 2 == 0]

def square(num):
    """
    eleva al cuadrado un numero
    """
    return num ** 2

print(apply(numbers,square))
