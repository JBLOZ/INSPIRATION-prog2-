import re
import pickle as plk
import Exceptions as ex

class User:
    def __init__(self, name=None, nickname=None, email=None, password=None):
        self.name = name
        self.nickname = nickname
        self.email = email
        self.password = password
        self.listaSeguidores = []
        self.listaSiguiendo = []
        self.listaInspirations = []

    def check_name(self):
        if re.match(r'^[A-Z][a-z_]{1,}$', self.name):
            return True
        else:
            raise InvalidNameError()

    def check_nickname(self):
        if re.match(r'^[a-zA-Z0-9]{3,15}$', self.nickname):
            return True
        else:
            raise ex.InvalidNicknameError()

    def check_password(self):
        if re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,20}$', self.password):
            return True
        else:
            raise ex.InvalidPasswordError()

    def check_email(self):
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", self.email):
            return True
        else:
            raise ex.InvalidEmailError()

    def __add__(self, other):
        self.listaInspirations.append(other)
        Data.diccUsers[self.nickname] = self
        Data().guardar_usuarios()


    def __sub__(self, other):
        self.listaInspirations.remove(other)
        Data.diccUsers[self.nickname] = self
        Data().guardar_usuarios()

    def log_in(self, nickname, password):
        try:
            if nickname not in Data.diccUsers:
                raise ex.UserNotFoundError()
            elif Data.diccUsers[nickname].password == password:
                return Data.diccUsers[nickname]
            else:
                raise InvalidPasswordError()
        except (ex.UserNotFoundError, ex.InvalidPasswordError) as e:
            return None

    def follow(self, other):
        try:
            if other.nickname in self.listaSiguiendo:
                raise AlreadyFollowingError()
            self.listaSiguiendo.append(other.nickname)
            other.listaSeguidores.append(self.nickname)
            Data.diccUsers[self.nickname] = self
            Data().guardar_usuarios()
        except ex.AlreadyFollowingError as e:
            pass

    def unfollow(self, other):
        try:
            if other.nickname not in self.listaSiguiendo:
                raise ex.NotFollowingError()
            self.listaSiguiendo.remove(other.nickname)
            other.listaSeguidores.remove(self.nickname)
            Data.diccUsers[self.nickname] = self
            Data().guardar_usuarios()
        except ex.NotFollowingError as e:
            pass

    def create_inspiration(current_user, text):
        new_inspiration = Inspiration(current_user, text)
        current_user.listaInspirations.append(new_inspiration)

    def show_inspirations(current_user):
        user_inspirations = current_user.listaInspirations
        for followed_user in current_user.listaSiguiendo:
            user_inspirations.extend(followed_user.listaInspirations)

        unique_inspirations = []
        for inspiration in user_inspirations:
            if inspiration not in unique_inspirations:
                unique_inspirations.append(inspiration)

        sorted_inspirations = sorted(unique_inspirations, key=lambda x: x.date_published)

        return sorted_inspirations



class Data:

    archivo = 'usuarios.pickle'
    diccUsers = {}
    def __init__(self):
        pass


    def lectura_usuarios(self):
        try:
            with open(Data.archivo, "rb") as rfile:
                Data.diccUsers = plk.load(rfile)
        except (EOFError, FileNotFoundError):
            print('Archivo vacío o no encontrado. Inicializando diccionario vacío...')
            Data.diccUsers = {}
        except Exception as e:
            print(e)

    def guardar_usuarios(self):
        try:
            with open(Data.archivo, "wb") as wfile:
                plk.dump(Data.diccUsers, wfile)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    Data().lectura_usuarios()

    print(Data.diccUsers['jord'].name, Data.diccUsers['jord'].nickname, Data.diccUsers['jord'].email, Data.diccUsers['jord'].password)













