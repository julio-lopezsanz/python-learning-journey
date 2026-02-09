"""
Tienes una lista de registros de accesos al sistema.
Cada registro tiene:

{"user": "Ana", "success": True}


Quieren obtener un diccionario con la cantidad de accesos exitosos por usuario.
"""

access_logs = [
    {"user": "Ana", "success": True},
    {"user": "Luis", "success": False},
    {"user": "Ana", "success": True},
    {"user": "Luis", "success": True},
    {"user": "Ana", "success": False},
]

def successful_accesses_per_user(logs):
    """
    Se utilizaran los patrones: filtro por condicion y conteo por clave.
    """
    result = {}

    #Estás recorriendo la lista.
    #En cada vuelta, log es un diccionario,
    for log in logs:
        #Solo los accesos exitosos siguen al siguiente paso.
        #Los fallidos se ignoran por completo.
        if log["success"]:
            #Extraes la clave que te interesa.
            user = log["user"]
            #Busca si user ya existe como clave en result
            #Si existe → devuelve su valor actual
            #Si NO existe → devuelve 0
            result[user] = result.get(user, 0) + 1

    return result

print(successful_accesses_per_user(access_logs))
