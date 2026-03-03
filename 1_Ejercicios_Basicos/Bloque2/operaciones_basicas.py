"""
Dado un número entero del usuario, 
calcula e imprime: 
    - cuadrado 
    - Cubo 
    - Raíz cuadrada (usa ** 0.5) 
    - si es par o impar 
    - residuo al dividir entre 7.
    Nota: Ocurre un ValueError si: ingresas caracteres que no sean numeros o 
          ingresas numeros flotantes
"""

number = int(input("Ingresa un numero: "))

print(f"Cuadrado de {number}: {number ** 2}")
print(f"Cubo de {number}: {number ** 3}")
print(f"Raiz cuadrada de {number}: {number ** 0.5}")
print(f"{number} es par" if number % 2 == 0 else f"{number} es impar")
print(f"residuo al dividir {number} entre 7: {number % 7}")
