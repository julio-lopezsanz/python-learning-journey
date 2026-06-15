"""
La computadora elige un número del 1 al 100 (random). 
    - El usuario tiene que adivinarlo. 
Después de cada intento 
    - Di si el número secreto es mayor o menor. 
    - Cuenta los intentos y muestra cuántos tomó al final.
"""

import random

secret_number = random.randint(1,100)

print("\nEstoy pensando en un numero entre el 1 y el 100. ¿Puedes adivinarlo?")

num = int(input("\n¿En que numero estoy pensando?: "))
TRIES = 0

while num != secret_number:
    if num < secret_number:
        print(f"\nEl numero que estoy pensando es mayor a {num}")
        TRIES += 1
        num = int(input("\n¿En que numero estoy pensando?: "))
    elif num > secret_number:
        print(f"\nEl numero que estoy pensando es menor a {num} ")
        TRIES += 1
        num = int(input("\n¿En que numero estoy pensando?: "))

print(f"\n¡HAZ GANADO!. El numero secreto era: {secret_number}")
print(f"Logrado en {TRIES} intentos")
