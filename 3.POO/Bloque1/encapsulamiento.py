"""
Crea una clase Usuario con atributos públicos nombre y email, 
y un atributo privado __password. 
Agrega un método cambiar_password(actual, nueva) 
que solo cambie la contraseña si la actual es correcta.
"""

class User:
    """Registra un usuario, con un email y su contraseña"""
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def change_password(self, current_password, new_password):
        """Cambia la contraseña de un usuario, siempre y cuando escriba su actual contraseña"""
        if current_password == self.__password:
            self.__password = new_password
            print("La contraseña ha cambiado exitosamente")
        else:
            print("Contraseña actual incorrecta")

usuario = User("Julio","julio@email.com","holaamigo")
usuario.change_password("soyjulio","nosequeponer")
usuario.change_password("holaamigo","holajulio")
