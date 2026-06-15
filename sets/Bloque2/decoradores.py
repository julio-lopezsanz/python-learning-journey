"""
Crea un decorador validar_acceso que imprima "Acceso permitido" 
antes de ejecutar cualquier función. 
Úsalo en una función ver_dashboard() que imprima "Mostrando dashboard..."
"""

def validate_access(func):
    """Imprime acceso permitido, antes de cualquier funcion"""
    def wrapper():
        print("Acceso permitido")
        func()
    return wrapper

@validate_access
def show_dashboard():
    """Imprime el dashboard"""
    print("Mostrando dashboard...")

show_dashboard()
