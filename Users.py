import re
import pickle as plk
import Exceptions as ex
from Inspiration import Inspiration
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
        try:
            if not re.match(r'^[A-Z][a-z_]{1,}$', self.name):
                raise ex.InvalidNameError()
            return True
        except ex.InvalidNameError as e:
            return False


    def check_nickname(self):
        try:
            if not re.match(r'^[a-zA-Z0-9]{3,15}$', self.nickname):
                raise ex.InvalidNicknameError()
            return True
        except ex.Nickname_Verified_Exception as e:
            return False


    def check_password(self):
        try:
            if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,20}$', self.password):
                raise ex.InvalidPasswordError()
            return True
        except ex.InvalidPasswordError as e:
            return False

    def check_email(self):
        try:
            if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', self.email):
                raise ex.InvalidEmailError()
            return True
        except ex.InvalidEmailError as e:
            return False

    def __add__(self, other):
        self.listaSiguiendo.append(other)
        other.listaSiguiendo.append(self)
        Data.diccUsers[self.nickname] = self
        Data.diccUsers[other.nickname] = other
        Data().guardar_usuarios()


    def __sub__(self, other):
        self.listaSiguiendo.remove(other)
        other.listaSiguiendo.remove(self)
        Data.diccUsers[self.nickname] = self
        Data.diccUsers[other.nickname] = other
        Data().guardar_usuarios()


    def follow(self, other):
        try:
            if other.nickname in self.listaSiguiendo:
                raise ex.AlreadyFollowingError()
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

    def create_inspiration(self, text):

        new_inspiration = Inspiration(self, text)
        if self.listaInspirations is not list:
            self.listaInspirations = []

        Data.diccUsers[self.nickname].listaInspirations.append(new_inspiration)
        Data().guardar_usuarios()

    def show_inspirations(self):
        user_inspirations = self.listaInspirations
        for followed_user in self.listaSiguiendo:
            user_inspirations.extend(followed_user.listaInspirations)

        unique_inspirations = []
        for inspiration in user_inspirations:
            if inspiration not in unique_inspirations:
                unique_inspirations.append(inspiration)

        sorted_inspirations = sorted(unique_inspirations, key=lambda x: x.fecha if x.fecha is not None else None)

        return sorted_inspirations

    def search_user(self, cadena):
        Data().lectura_usuarios()
        lista1= []

        for i in Data.diccUsers.items():
            if cadena.lower() in i[1].nickname.lower():
                lista1.append(i)

        return lista1# raise ex.UserNotFoundError()

    def me_gusta(self, inspiration):

        if self not in inspiration.likes:
            inspiration.likes.append(self)
            Data.diccUsers[self.nickname] = self
            Data().guardar_usuarios()

    def comprobar_mg(self, inspiration):

        if self in inspiration.likes:
            return True


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
    #Jordi = Data.diccUsers['jord']
    #Alejandro = Data.diccUsers['aos24']
    #print(Data.diccUsers['aos24'].password)
    #Jordi.__add__(Alejandro)
    nom = Data.diccUsers['jord']
    print(nom.nickname)











