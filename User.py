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


