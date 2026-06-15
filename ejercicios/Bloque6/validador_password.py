"""
Crea una función validar_contrasena(contrasena) que retorne True solo si: 
    - Tiene al menos 8 caracteres 
    - Contiene al menos un número
    - Contiene al menos una mayúscula. 
Si es inválida, muestra qué condición falla.
"""
def has_min_char(word):
    """
    Valida que la contraseña tenga al menos 8 caracteres
    """
    if len(word) < 8:
        return False

    return True

def has_upper_letter(word):
    """
    Valida que la contraseña tenga al menos caracter en mayusculas
    """
    if any(c.isupper() for c in word):
        return True

    return False

def has_num(word):
    """
    Valida que la contraseña tenga al menos un numero
    """
    if any(c.isdigit() for c in word):
        return True

    return False

def validate_password(password):
    """Valida la contraseña para que cumpla todos los requisitos"""

    if not has_min_char(password):
        print("La contraseña debe tener minimo 8 caracteres")
        return False
    if not has_upper_letter(password):
        print("La contraseña debe contener al menos una letras mayuscula")
        return False
    if not has_num(password):
        print("La contraseña debe contener al menos un numero")
        return False

    return True

pword = input("Ingrese una contraseña: ")
VALIDATED = validate_password(pword)

if VALIDATED:
    print("La contraseña ha sido aceptada")
else:
    print("intentelo de nuevo")
