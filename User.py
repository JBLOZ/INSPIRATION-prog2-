import re
import pickle as plk

archivo = 'usuarios.pickle'




class User():


    diccUsers = {}

    def __init__(self, name, nickname, email, password):
        self.name = name
        self.nickname = nickname
        self.email = email
        self.password = password
        self.listaSeguidores = []
        self.listaSiguiendo = []
        self.listaInspirations = []
        self.listaMisInspirations = []
        lectura_usuarios()
        try:
            if self.nickname in User.diccUsers.keys():
                raise ValueError('Usuario ya existente')

            if self.check_name() and self.check_nickname() and self.check_password():
                User.diccUsers[self.nickname] = self
                guardar_usuarios()

            else:
                raise ValueError('Datos incorrectos')
        except ValueError as e:
            print(e)


    def show_tweets(self):
        pass

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
            if re.match(r'^[a-z0-9]{3,15}$', self.nickname):
                return True
            else:
                raise ValueError('Nickname incorrecto')
        except ValueError as e:
            print(e)
            return False


    def check_password(self):
        try:
            if re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,20}$', self.password):
                return True
            else:
                raise ValueError('Contraseña incorrecta')
        except ValueError as e:
            print(e)
            return True


    def __add__(self, other):
        self.listaInspirations.append(other)

    def __sub__(self, other):
        self.listaInspirations.remove(other)




    def log_in(self, nickname, password):

        try:
            if User.diccUsers[nickname].password == password:
                return User.diccUsers[nickname]

            else:
                raise ValueError('Contraseña incorrecta')
        except ValueError as e:
            print(e)
            return None

def lectura_usuarios():
    try:
        with open(archivo, "rb") as rfile:
            User.diccUsers = plk.load(rfile)
    except EOFError:
        print('Archivo vacío')
    except Exception as e:
        print(e)


def guardar_usuarios():
    try:
        with open(archivo, "wb") as wfile:
            plk.dump(User.diccUsers, wfile)
    except Exception as e:
        print(e)




print(User.diccUsers)










