import re
import pickle as plk
import Exceptions as ex
from Inspiration import Inspiration
import csv
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
            print(e)
            return False

    # Verificar que el nickname es correcto
    def check_nickname(self):
        try:
            if not re.match(r'^[a-zA-Z0-9]{3,15}$', self.nickname):
                raise ex.InvalidNicknameError()
            return True
        except ex.InvalidNicknameError as e:
            print(e)
            return False

    # Verificar que la contraseña es correcta
    def check_password(self):
        try:
            if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,20}$', self.password):
                raise ex.InvalidPasswordError()
            return True
        except ex.InvalidPasswordError as e:
            print(e)
            return False

    # Verificar que el email es correcto
    def check_email(self):
        try:
            if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', self.email):
                raise ex.InvalidEmailError()
            return True
        except ex.InvalidEmailError as e:
            print(e)
            return False

    def __add__(self, other):
        try:
            if other in self.listaSiguiendo:
                raise ex.AlreadyFollowingError()
            else:
                self.listaSiguiendo.append(other)
                Data.diccUsers[self.nickname] = self
                Data().guardar_usuarios()
        except ex.AlreadyFollowingError as e:
            print(e)


    def __sub__(self, other):
        try:
            if other not in self.listaSiguiendo:
                raise ex.NotFollowingError()
            else:
                self.listaSiguiendo.remove(other)
                Data.diccUsers[self.nickname] = self
                Data().guardar_usuarios()
        except ex.NotFollowingError as e:
            print(e)


    def follow(self, other):
        self.__add__(other)

    def unfollow(self, other):
        self.__sub__(other)

    def create_inspiration(self, text):

        new_inspiration = Inspiration(self, text)
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
        if  len(unique_inspirations) == 0:
            return "No hay inspiraciones para mostrar."

        sorted_inspirations = sorted(unique_inspirations, key=lambda x: x.fecha)
        return sorted_inspirations

    def search_user(self, cadena):
        Data().lectura_usuarios()
        lista= []

        for i in Data.diccUsers.items():
            if cadena.lower() in i[1].nickname.lower():
                lista.append(i)
        try:
            if len(lista) == 0:
                raise ex.UserNotFoundError()

        except ex.UserNotFoundError as e:
            print(e)

        return lista


    def me_gusta(self, inspiration):

        if self in inspiration.likes:
            inspiration.likes.remove(self)
        else:
            inspiration.likes.append(self)
        Data.diccUsers[inspiration.user.nickname] = inspiration.user

        Data().guardar_usuarios()

    def guardar_en_csv(self):
        filename = f"{self.nickname}.csv"
        with open(filename, mode='w') as file:
            # Crear un escritor CSV
            writer = csv.writer(file)
            writer.writerow(["Usuario", "Inspiration", "Número de likes"])
            #  Iterar sobre cada inspiración en la lista de inspiraciones del usuario
            for inspiration in self.listaInspirations:
                writer.writerow([self.nickname, inspiration.text, len(inspiration.likes)])


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













