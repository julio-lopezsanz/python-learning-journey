"""
Pide la elección del usuario (piedra/papel/tijera). 
    - Genera una elección aleatoria de la computadora  (import random, random.choice([...])). 
    - Determina quién gana con condicionales. 
Muestra el resultado.
"""
import random

option = input("¿Que eliges?. ¿piedra, papel o tijera?: ").lower()
bot_option = random.choice(["piedra","papel","tijera"])

if option == bot_option:
    print(f"Haz elegido {option} y tu contricante {bot_option}")
    print("¡ES UN EMPATE!")
elif option == "tijera" and bot_option == "piedra":
    print(f"Haz elegido {option} y tu contricante {bot_option}")
    print("¡HAS PERDIDO!")
elif option == "tijera" and bot_option == "papel":
    print(f"Haz elegido {option} y tu contricante {bot_option}")
    print("¡HAS GANADO!")
elif option == "papel" and bot_option == "tijera":
    print(f"Haz elegido {option} y tu contricante {bot_option}")
    print("¡HAS PERDIDO!")
elif option == "papel" and bot_option == "piedra":
    print(f"Haz elegido {option} y tu contricante {bot_option}")
    print("¡HAS GANADO!")
elif option == "piedra" and bot_option == "papel":
    print(f"Haz elegido {option} y tu contricante {bot_option}")
    print("¡HAS PERDIDO!")
elif option == "piedra" and bot_option == "tijera":
    print(f"Haz elegido {option} y tu contricante {bot_option}")
    print("¡HAS GANADO!")
