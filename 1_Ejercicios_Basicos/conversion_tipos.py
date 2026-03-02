"""
Pide al usuario su edad como texto con input(). 
Convierte ese texto a entero, luego a flotante. 
Imprime los tres valores y sus tipos. 
¿Qué pasa si el usuario escribe 'veinte' en vez de '20'?
R = Arroja un ValueError, ya que ingrese una cadena que no representa un numero
"""

age = input("Ingrese su edad: ")
age_int = int(age)
age_float = float(age)

print(f"Edad: {age} - tipo: {type(age)}")
print(f"Edad: {age_int} - tipo: {type(age_int)}")
print(f"Edad: {age_float} - tipo: {type(age_float)}")
