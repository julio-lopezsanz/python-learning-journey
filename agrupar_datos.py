"""
students = [
    ("Ana", "math"),
    ("Luis", "english"),
    ("Ana", "english"),
    ("Pedro", "math"),
    ("Luis", "math")
]

Devuelve:

{
  "math": ["Ana", "Pedro", "Luis"],
  "english": ["Luis", "Ana"]
}
"""

students = [
    ("Ana", "math"),
    ("Luis", "english"),
    ("Ana", "english"),
    ("Pedro", "math"),
    ("Luis", "math")
]

def group_data(data):
    """
    Agrupa datos sin el uso de librerias
    """
    grouped = {}

    for key, value in data:
        grouped.setdefault(value, []).append(key)

    return grouped

print(group_data(students))
