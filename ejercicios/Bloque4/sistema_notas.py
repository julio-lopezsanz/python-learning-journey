"""
Pide 3 calificaciones (0-100). 
Calcula el promedio. 
Muestra la letra correspondiente: 
    - A (90-100) 
    - B (80-89) 
    - C (70-79) 
    - D (60-69) 
    - F (<60) 
También indica si el alumno pasa o reprueba (>=60).
"""

grade1 = int(input("Ingrese la calificacion de matematicas (0-100): "))
grade2 = int(input("Ingrese la calificacion de historia (0-100): "))
grade3 = int(input("Ingrese la calificacion de programacion (0-100): "))

avg = (grade1 + grade2 + grade3)//3

if avg >=90 and avg <=100:
    print("A")
elif avg >=80 and avg <90:
    print("B")
elif avg >=70 and avg <80:
    print("C")
elif avg >=60 and avg <70:
    print("D")
elif avg < 60:
    print("F")

if avg >= 60:
    print("¡Felicidades, has aprobado!")
else:
    print("Has reprobado. Estudia mas para la proxima")
