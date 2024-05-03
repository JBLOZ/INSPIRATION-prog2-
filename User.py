import re
import pickle as plk

archivo = 'usuarios.pickle'
class User():
    listaUsers = []
    def __init__(self, name, nickname, email, password):
        self.name = name
        self.nickname = nickname
        self.email = email
        self.password = password
        self.listaSeguidores = []
        self.listaSiguiendo = []
        self.listaInspirations = []
        self.listaMisInspirations = []

    def show_tweets(self):
        pass

    def check_name(self):
        try:
            if re.match(r'^[A-Z][a-z_]{1,}$', self.name):
                return True
            else:

               return False
        except:
            return False

    def check_nickname(self):
        if re.match(r'^[a-z0-9]{3,15}$', self.nickname):
            return True
        else:
            return False

    def check_password(self):
        if re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,20}$', self.password):
            return True
        else:
            return False


    def __add__(self, other):
        self.listaInspirations.append(other)

    def __sub__(self, other):
        if other in User.listaUsers:
            User.listaUsers.remove(other)






    def save_user(self):
        lector_usuarios()
        with open(archivo, "wb") as wfile:

            User.listaUsers.append({self.nickname: self})
            plk.dump(User.listaUsers, wfile)

    def log_in(self, nickname, password):
        User.lector_usuarios()
        try:
            if nickname in User.listaUsers:
                if User.listaUsers[nickname].password == password:
                    return User.listaUsers[nickname]
                else:
                    raise ValueError('Contraseña incorrecta')
            else:
                raise ValueError('Usuario no encontrado')
        except ValueError as e:
            print(e)
            return None


def lector_usuarios():
    try:
        with open(archivo, "rb") as rfile:
            User.listaUsers = plk.load(rfile)
    except:
        User.listaUsers = []


lector_usuarios()
print(User.listaUsers)










