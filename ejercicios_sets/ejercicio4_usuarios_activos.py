"""
¿Quiénes no están activos?
¿Todos los activos están en la lista total?
¿Hay alguien activo que no debería existir?
"""

active_users = {"Ana", "Luis", "Pedro","julio"}
all_users = {"Ana", "Luis", "Pedro", "Maria", "Juan"}

def users_status(active_users, all_users):
    """
    Devuelve los que no estan activos, determina si los usuarios activos
    estan en el registros de todos los usuarios y descubre si hay usuarios 
    activos que no pertenezcan a los registros de todos los usuarios
    """

    not_active = all_users - active_users

    active_in_logs = active_users.issubset(all_users)

    active_not_in_logs = active_users - all_users

    return not_active, active_in_logs, active_not_in_logs

print(users_status(active_users, all_users))
