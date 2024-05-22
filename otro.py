EXCEPCIONES

# Excepción personalizada para nombres incorrectos
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


# En clase Users


    # Verificar que el nombre es correcto
    def check_name(self):
        try:
            if not re.match(r'^[A-Z][a-z_]{1,}$', self.name):
                raise ex.InvalidNameError()
            return True
        except ex.InvalidNameError as e:
            return False

    # Verificar que el nickname es correcto
    def check_nickname(self):
        try:
            if not re.match(r'^[a-zA-Z0-9]{3,15}$', self.nickname):
                raise ex.InvalidNicknameError()
            return True
        except ex.InvalidNicknameError as e:
            return False

    # Verificar que la contraseña es correcta
    def check_password(self):
        try:
            if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,20}$', self.password):
                raise ex.InvalidPasswordError()
            return True
        except ex.InvalidPasswordError as e:
            return False

    # Verificar que el email es correcto
    def check_email(self):
        def check_email(self):
            try:
                if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', self.email):
                    raise ex.InvalidEmailError()
                return True
            except ex.InvalidEmailError as e:
                return False




                    

    # Permite crear una nueva inspiracion
    def create_inspiration(self, text):
        new_inspiration = Inspiration(self, text)
        # Asegurar que la listaInspiration es una lista
        if self.listaInspirations is not list:
            self.listaInspirations = []
        # Añadir la nueva inspiración a la lista de inspiraciones
        Data.diccUsers[self.nickname].listaInspirations.append(new_inspiration)
        Data().guardar_usuarios()

    # Obtener las inspiraciones propias y las de los seguidos
    def show_inspirations(self):
        user_inspirations = self.listaInspirations
        for followed_user in self.listaSiguiendo:
            user_inspirations.extend(followed_user.listaInspirations)
        # Eliminar inspiraciones duplicadas
        unique_inspirations = []
        for inspiration in user_inspirations:
            if inspiration not in unique_inspirations:
                unique_inspirations.append(inspiration)

        # Ordenar inspiraciones por fecha de publicación
        sorted_inspirations = sorted(unique_inspirations, key=lambda x: x.date_published)

        return sorted_inspirations

    # Permite buscar usuarios a partir de una cadena
    def search_user(self, cadena):
        # Leer usuarios desde el archivo
        Data().lectura_usuarios()
        lista1 = []

        # Buscar coincidencias de la cadena en los nickname de los usuarios
        for i in Data.diccUsers.items():
            if cadena.lower() in i[1].nickname.lower():
                lista1.append(i)

        return lista1

        # Almacenar en un archivo csv el nickname del usuario, el texto de la inspiración y el número de likes

    def guardar_en_csv(self, filename):
        with open(filename, mode='w') as file:
            # Crear un escritor CSV
            writer = csv.writer(file)
            writer.writerow(["Usuario", "Inspiration", "Número de likes"])
            #  Iterar sobre cada inspiración en la lista de inspiraciones del usuario
            for inspiration in self.listaInspirations:
                writer.writerow([self.nickname, inspiration.text, len(inspiration.likes)])
