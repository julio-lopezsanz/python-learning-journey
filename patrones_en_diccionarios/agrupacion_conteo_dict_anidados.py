"""
Escribe una función que reciba logs y devuelva:
{
  "Ana": {"login": 2, "logout": 1},
  "Luis": {"login": 1, "logout": 1}
}
"""

logs = [
    ("Ana", "login"),
    ("Luis", "logout"),
    ("Ana", "logout"),
    ("Ana", "login"),
    ("Luis", "login")
]

def user_login_logout(users_logs):
    """
    Cuenta los inicios y cierres de sesion de cada usuario
    """

    grouped = {}

    for user,status in users_logs:

        if user not in grouped:
            grouped[user] = {}

        if status in grouped[user]:
            grouped[user][status] += 1
        else:
            grouped[user][status] = 1

        #Solucion Pythonic:
        #grouped.setdefault(user, {})
        #grouped[user][status] = grouped[user].get(status, 0) + 1
    return grouped

print(user_login_logout(logs))
