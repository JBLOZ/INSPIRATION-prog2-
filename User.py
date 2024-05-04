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
        lectura_usuarios() #Lee los usuarios del archivo
        try:
            if self.nickname in User.diccUsers.keys(): #Comprueba si el usuario ya existe
                raise ValueError('Usuario ya existente')

            if self.check_name() and self.check_nickname() and self.check_password(): #Comprueba que los datos sean correctos
                User.diccUsers[self.nickname] = self #Añade el usuario al diccionario
                guardar_usuarios() #Guarda los usuarios en el archivo

            else:
                raise ValueError('Datos incorrectos') #Si los datos son incorrectos, lanza una excepción
        except ValueError as e: #Captura la excepción
            print(e) #Imprime el mensaje de la excepción


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

    def follow(self, other):
        try:
            if other.nickname in self.listaSiguiendo:
                raise ValueError('Ya sigues a este usuario')
            self.listaSiguiendo.append(other.nickname)
            other.listaSeguidores.append(self.nickname)
            User.diccUsers[self.nickname] = self
            guardar_usuarios()

        except ValueError as e:
            print(e)


    def unfollow(self, other):
        try:
            if other.nickname not in self.listaSiguiendo:
                raise ValueError('No sigues a este usuario')
            self.listaSiguiendo.remove(other.nickname)
            other.listaSeguidores.remove(self.nickname)
            User.diccUsers[self.nickname] = self
            guardar_usuarios()
        except ValueError as e:
            print(e)


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













