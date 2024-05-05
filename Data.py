import pickle as plk
import subprocess

archivo = 'usuarios.pickle'
diccUsers = {}

def lectura_usuarios():
    try:
        with open(archivo, "rb") as rfile:
            return plk.load(rfile)
    except EOFError:
        print('Archivo vacío')
    except Exception as e:
        print(e)


def guardar_usuarios():
    try:
        with open(archivo, "wb") as wfile:
            plk.dump(diccUsers, wfile)
    except Exception as e:
        print(e)


