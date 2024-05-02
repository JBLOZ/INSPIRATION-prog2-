from Inspiration import Inspiration
import pickle as pk

archivo = ''
class User():
    def __init__(self, nombre, nickname, email, password):
        self.nombre = nombre
        self.nickname = nickname
        self.email = email
        self.password = password
        self.listaSeguidores = []
        self.listaSiguiendo = []
        self.listaInspirations = []

    def log_in(self, nickname, password):
        if nickname == self.nickname and password == self.password:
            print("Inicio de sesión exitoso")
            return True
        else:
            print("Nombre de usuario o contraseña incorrectos")
            return False

    def check_name(self, nombre_a_verificar):
       if re.match(r'^[A-Z][a-z_]{3,}$', )




    def __add__(self, other):
        self.listaInspirations.append(other)

    def lector_usuarios(self):
        try:
            with open(archivo, "rb") as rfile:
                diccionario_usuarios = pk.load(rfile)
        except EOFError:
            diccionario_usuarios = {}

        return diccionario_usuarios

    def save_user(self):
        with open(archivo, 'wb') as sfile:

"""
def log_in(User):
    User = User(nombre,nickname, email, password)
    """