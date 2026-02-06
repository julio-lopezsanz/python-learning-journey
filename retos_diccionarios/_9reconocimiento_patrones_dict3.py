"""
Devuelve: 
{ "error": ["DB down", "timeout"], "info": ["started", "running"] }
"""

logs = [
    ("error", "DB down"),
    ("info", "started"),
    ("error", "timeout"),
    ("info", "running"),
]

def group_log_status(logs_entries):
    """
    Agrupa los logs por estado y devuelve un diccionario de listas.
    """

    grouped = {}

    #Patron de agrupacion
    for status, action in logs_entries:
        grouped.setdefault(status, []).append(action)

    return grouped

print(group_log_status(logs))
