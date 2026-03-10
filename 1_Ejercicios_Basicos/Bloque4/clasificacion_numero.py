"""
Pide un número al usuario. 
Indica si es: 
    - positivo negativo o cero
    - par o impar. 
Muestra ambos resultados.
"""

number = int(input("Ingresa un numero: "))

if number > 0:
    print(f"El  numero  {number} es positivo")
elif number < 0:
    print(f"El numero {number} es negativo")
else:
    print(f"El numero es {number}")

IS_EVEN_OR_ODD = "Es par" if number % 2 == 0 else "Es impar"
print(IS_EVEN_OR_ODD)
