"""
Pide al usuario: 
    - nombre completo 
    - edad 
    - ciudad 
    - ocupación 
Muestra: 
un resumen formateado con todos los datos, 
usando f-strings. Que se vea presentable.
"""

name = input("\nIngresa tu nombre completo: ")
age = input("\nIngresa tu edad: ")
city = input("\nIngresa tu ciudad de residencia: ")
occupation = input("\nIngresa a que te dedicas: ")

print(f"Tu nombre es {name} y ", end="")
print(f"tienes {age} años de edad.")
print(f"Vives en {city}, bonita ciudad por cierto, ", end="")
print(f"y tu trabajo es {occupation}")
