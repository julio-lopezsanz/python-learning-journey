"""
Toma tu ejercicio del sistema de notas (Bloque 4). 
Reescríbelo usando funciones: 
    - Función para calcular_promedio(n1, n2, n3) 
    - Funcion para obtener_letra(promedio) 
    - Funcion para determinar_estado(promedio). 
El programa principal solo llama estas funciones
"""
def calculate_grade(g1,g2,g3):
    """
    Calcula el promedio a partir de tres calificaciones.
    """
    return (g1 + g2 + g3) // 3

def get_grade (average):
    """
    Retorna una letra, dependiendo del promedio obtenido
    """
    if average >=90 and average <=100:
        return "A"
    elif average >=80 and average <90:
        return "B"
    elif average >=70 and average <80:
        return "C"
    elif average >=60 and average <70:
        return "D"
    else:
        return "F"

def is_approved(grd):
    """
    Determina si el promedio es aprobatorio o no
    """
    if grd >= 60:
        return True

    return False

grade1 = int(input("Ingrese la calificacion de matematicas (0-100): "))
grade2 = int(input("Ingrese la calificacion de historia (0-100): "))
grade3 = int(input("Ingrese la calificacion de programacion (0-100): "))

avg = calculate_grade(grade1,grade2,grade3)
grade = get_grade(avg)
approved = is_approved(avg)

print("------RESULTADOS-----")
print(f"Promedio: {avg}")
print(f"Nota: {grade}")
if approved:
    print("¡Felicidades, has aprobado!")
else:
    print("Has reprobado. Estudia mas para la proxima")
