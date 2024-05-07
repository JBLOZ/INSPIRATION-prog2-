import re
import pickle as plk

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
            if re.match(r'^[A-Z][a-z_]{1,}$', self.name):
                return True
            else:
                raise ValueError('Nombre incorrecto')
        except ValueError as e:
            print(e)
            return False

    def check_nickname(self):
        try:
            if re.match(r'^[a-zA-Z0-9_-]{3,15}$', self.nickname):
                return True
            else:
                raise ValueError('Nickname incorrecto')
        except ValueError as e:
            print(e)
            return False

    def check_password(self):
        try:
            if re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_.])[A-Za-z\d@$!%*?&_.]{8,20}$', self.password):
                return True
            else:
                raise ValueError('Contraseña incorrecta')
        except ValueError as e:
            print(e)
            return False

    def check_email(self):
        try:
            if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", self.email):
                return True
            else:
                raise ValueError('Email incorrecto')
        except ValueError as e:
            print(e)
            return False

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
            if nickname not in Data().diccUsers:
                raise ValueError('El usuario no existe')
            elif Data().diccUsers[nickname].password == password:
                return Data().diccUsers[nickname]
            else:
                raise ValueError('Contraseña incorrecta')
        except ValueError as e:
            print(e)
            return None

    def follow(self, other):
        try:
            if other.nickname in self.listaSiguiendo:
                raise ValueError('Ya sigues a este usuario')
            self.listaSiguiendo.append(other.nickname)
            other.listaSeguidores.append(self.nickname)
            Data.diccUsers[self.nickname] = self
            Data().guardar_usuarios()
        except ValueError as e:
            print(e)

    def unfollow(self, other):
        try:
            if other.nickname not in self.listaSiguiendo:
                raise ValueError('No sigues a este usuario')
            self.listaSiguiendo.remove(other.nickname)
            other.listaSeguidores.remove(self.nickname)
            Data.diccUsers[self.nickname] = self
            Data().guardar_usuarios()
        except ValueError as e:
            print(e)



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

    print(Data.diccUsers)













