"""
Pide un número al usuario. 
Imprime su tabla de multiplicar del 1 al 12. 
"""

number = int(input("Ingresa un numero para mostrar su tabla de multiplicar: "))

for cycle in range(1,13):
    print(f"{number} X {cycle} = {number * cycle}")
