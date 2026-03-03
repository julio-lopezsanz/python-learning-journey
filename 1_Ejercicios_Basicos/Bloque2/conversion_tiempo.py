"""
Pide al usuario un número de segundos (ejemplo: 9000). 
Convierte y muestra: 
    - Horas 
    - Minutos
    - Segundos 
Ejemplo: 
9000 segundos = 2 horas, 30 minutos, 0 segundos.
"""

time_in_seconds = int(input("Ingresa una cantidad entera de segundos: "))

hours = time_in_seconds // 3600 # 1 hora = 3600
minutes = (time_in_seconds % 3600)/60 #Quita las horas y deja los minutos
seconds = time_in_seconds % 60 #Deja los segundos restantes

print(f"{time_in_seconds} Segundos = {hours} horas, {minutes} minutos y {seconds} segundos.")
