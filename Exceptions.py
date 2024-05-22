class InvalidNameError(Exception):
    def __init__(self, message="Nombre incorrecto"):
        self.message = message
        super().__init__(self.message)

# Excepción personalizada para nicknames incorrectos
class InvalidNicknameError(Exception):
    def __init__(self, message="Nickname incorrecto"):
        self.message = message
        super().__init__(self.message)

# Excepción personalizada para contraseñas incorrectas
class InvalidPasswordError(Exception):
    def __init__(self, message="Contraseña incorrecta"):
        self.message = message
        super().__init__(self.message)
# Excepción personalizada para emails incorrectos
class InvalidEmailError(Exception):
    def __init__(self, message="Email incorrecto"):
        self.message = message
        super().__init__(self.message)
# Excepción personalizada para usuario no encontrado
class UserNotFoundError(Exception):
    def __init__(self, message="El usuario no existe"):
        self.message = message
        super().__init__(self.message)

# Excepción personalizada para el caso de ya seguir a un usuario
class AlreadyFollowingError(Exception):
    def __init__(self, message="Ya sigues a este usuario"):
        self.message = message
        super().__init__(self.message)

# Excepción personalizada para el caso de no seguir a un usuario
class NotFollowingError(Exception):
    def __init__(self, message="No sigues a este usuario"):
        self.message = message
        super().__init__(self.message)