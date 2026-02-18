"""
Obtener los emails únicos
Contar cuántos emails duplicados hubo
Saber si "d@gmail.com" ya existe
"""

emails = [
    "a@gmail.com",
    "b@gmail.com",
    "a@gmail.com",
    "c@gmail.com",
    "b@gmail.com"
]

def analyze_emails(emails_logs):
    """
    Regresa los email unicos, cuenta los emails duplicados,
    y verifica si el email d@gmail.com esta en los logs
    """

    unique = set(emails_logs)

    total = len(emails_logs)
    duplicate = total - len(unique)

    return (
        unique,
        duplicate,
        "d@gmail.com" in emails_logs
    )

print(analyze_emails(emails))
