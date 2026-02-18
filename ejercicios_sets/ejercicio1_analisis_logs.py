"""
Tienes esta lista:

logs = ["login", "logout", "login", "login", "logout"]


Haz lo siguiente:
    - Obtén las acciones únicas
    - Cuenta cuántas acciones distintas hay
    - Verifica si "signup" apareció
    - Usa set sí o sí
"""

logs = ["login", "logout", "login", "login", "logout"]

def analyze_logs(list_logs):
    """
    Devuelve las acciones únicas, cuántas hay
    y si 'signup' está presente.
    """

    unique_actions = set(list_logs)

    return (
        unique_actions,
        len(unique_actions),
        "signup" in unique_actions
    )

print(analyze_logs(logs))
