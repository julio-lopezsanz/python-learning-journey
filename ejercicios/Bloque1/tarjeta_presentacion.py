"""
Crea variables para:
 - Nombre
 - Edad
 - Ciudad
 - Altura
 - Si eres estudiante o no
Despues imprime cada una ademas con su tipo de variable
"""

NAME = "Julio"
AGE = 28
CITY = "Zihuatanejo"
HEIGHT = 1.81
IS_STUDENT = False

print(f"\nNombre: {NAME} - {type(NAME)}")
print(f"\nEdad: {AGE} - {type(AGE)} ")
print(f"\nCiudad: {CITY} - {type(CITY)}")
print(f"\nAltura: {HEIGHT}m - {type(HEIGHT)}")
print(f"\n¿Eres estudiante?: {IS_STUDENT} - {type(IS_STUDENT)}")
