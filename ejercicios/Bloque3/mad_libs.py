"""
Pide al usuario 5 palabras: 
    - nombre 
    - verbo 
    - adjetivo 
    - lugar
    - número 
Construye una historia coherente usando esas palabras con f-strings. 
La historia debe tener al menos 3 oraciones.
"""

name = input("Ingresa un nombre: ")
verb = input("Ingresa un verbo: ")
adjective = input("Ingresa un adjetivo cualificativo: ")
place = input("Ingresa un lugar: ")
number = int(input("ingresa un numero: "))

STORY = f"""
En un lugar lejano, conocido como {place}, vivía un temido caballero llamado {name}.
Se decía que solía {verb} por todo el campo de batalla sin mostrar miedo alguno.
Con su espada {adjective}, hacía retroceder a cualquiera que osara
interponerse en su camino, y con apenas {number} cortes
era capaz de derrotar a sus enemigos.
"""

print(STORY)
