"""
Tienes este diccionario:

grades = {
    "Ana": "A",
    "Luis": "B",
    "Sofía": "A",
    "Pedro": "C",S
    "Marta": "B"
}


Quieres obtener un diccionario donde:
    - la clave sea la calificación
    - el valor sea una lista de personas con esa calificación
"""

grades = {
    "Ana": "A",
    "Luis": "B",
    "Sofía": "A",
    "Pedro": "C",
    "Marta": "B"
}

def inverse_group(dictionary):
    """
    Invierte el diccionario, usando el valor como clave, y la clave como valor
    """

    grouped = {}

    for key,value in dictionary.items():
        if value not in grouped:
            grouped[value] = []

        grouped[value].append(key)

        #Solucion Pythonic: grouped.setdefault(value, []).append(key)
    return grouped

print(inverse_group(grades))
