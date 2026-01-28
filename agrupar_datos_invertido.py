"""
records = [
    ("Carlos", "ventas"),
    ("Ana", "marketing"),
    ("Luis", "ventas"),
    ("Ana", "ventas"),
    ("Pedro", "marketing"),
    ("Luis", "soporte")
]
Debes devolver:
{
    "ventas": ["Carlos", "Luis", "Ana"],
    "marketing": ["Ana", "Pedro"],
    "soporte": ["Luis"]
}
Reglas
    - Usa diccionarios
    - Usa bucle (como hiciste)
    - No librerías
    - No pasos raros innecesarios
"""
records = [
    ("Carlos", "ventas"),
    ("Ana", "marketing"),
    ("Luis", "ventas"),
    ("Ana", "ventas"),
    ("Pedro", "marketing"),
    ("Luis", "soporte")
]

def group_data(data):
    """
    Devuelve un diccionario con datos agrupados pero invertidos
    """

    grouped = {}

    for key, value in data:
        grouped.setdefault(value, []).append(key)

    return grouped

print(group_data(records))
