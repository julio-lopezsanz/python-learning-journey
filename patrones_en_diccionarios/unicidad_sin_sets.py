"""
Tienes una lista de registros de accesos a una plataforma:

access_logs = [
    ("Ana", "login"),
    ("Luis", "login"),
    ("Ana", "login"),
    ("Ana", "logout"),
    ("Luis", "login"),
    ("Pedro", "login"),
    ("Pedro", "logout"),
    ("Pedro", "login")
]

Objetivo

Construir una función que devuelva un diccionario con esta estructura:

{
    "Ana": {
        "acciones": ["login", "logout"],
        "total_eventos": 3
    },
    "Luis": {
        "acciones": ["login"],
        "total_eventos": 2
    },
    "Pedro": {
        "acciones": ["login", "logout"],
        "total_eventos": 3
    }
}

Reglas importantes
    -acciones no debe contener duplicados
    -El orden no importa
    -No uses sets todavía
    -Usa solo lo que ya sabes
"""

access_logs = [
    ("Ana", "login"),
    ("Luis", "login"),
    ("Ana", "login"),
    ("Ana", "logout"),
    ("Luis", "login"),
    ("Pedro", "login"),
    ("Pedro", "logout"),
    ("Pedro", "login")
]

def action_per_user(logs_data):
    """
    Lleva un control de acciones realizadas por el usuario, y cuantas veces los usuarios
    realizaron acciones.
    """

    grouped = {}

    for user,action in logs_data:

        if user not in grouped:
            grouped[user] = {
                "actions": [],
                "events_count": 0
            }

        if action not in grouped[user]["actions"]:
            grouped[user]["actions"].append(action)

        grouped[user]["events_count"] += 1

        #Solucion con sets
        #for user, action in logs_data:
        #   if user not in grouped:
        #        grouped[user] = {
        #           "actions": set(),
        #            "events_count": 0
        #        }
        #grouped[user]["actions"].add(action)
        #grouped[user]["events_count"] += 1

        #solucion mas pythonica sin sets:
        # for user, action in logs_data:
        #grouped.setdefault(user, {
        #    "actions": [],
        #    "events_count": 0
        #})
        #if action not in grouped[user]["actions"]:
        #    grouped[user]["actions"].append(action)
        #grouped[user]["events_count"] += 1

        #Solucion pythonic con sets:
        #for user, action in logs_data:
        #grouped.setdefault(user, {
        #    "actions": set(),
        #    "events_count": 0
        #})
        #grouped[user]["actions"].add(action)
        #grouped[user]["events_count"] += 1
    return grouped

print(action_per_user(access_logs))
