import User

class Client(User.User):
    def __init__(self, nickname, password, nombre, apellido, edad, listaSeguidores, listaSiguiendo):
        super().__init__(nickname, password, nombre, apellido, edad, listaSeguidores, listaSiguiendo)
        self.listaInspirations = []

    def crear_inspiration(self):
        try:
            pass

        except Exception as e:
            print(e)

    def show_inspirations(self):
        for i in self.listaInspirations:
            print(f'Título: {i[0]}')
            print(f'Contenido: {i[1]}')
            print()

    def seguir(self, other):
        try:
            if other.nickname in self.listaSiguiendo:
                raise ValueError('Ya sigues a este usuario')
            self.listaSiguiendo.append(other.nickname)
            other.listaSeguidores.append(self.nickname)
            User.diccUsers[self.nickname] = self
            User.guardar_usuarios()

        except ValueError as e:
            print(e)


    def dejar_de_seguir(self, other):
        try:
            if other.nickname not in self.listaSiguiendo:
                raise ValueError('No sigues a este usuario')
            self.listaSiguiendo.remove(other.nickname)
            other.listaSeguidores.remove(self.nickname)
            User.diccUsers[self.nickname] = self
            User.guardar_usuarios()
        except ValueError as e:
            print(e)

    def mostrar_perfil(self):
        pass

    def buscar_usuarios(self):
        try:
            nickname = input('Ingrese el nickname del usuario que desea buscar: ')
            if nickname not in User.diccUsers:
                raise ValueError('Usuario no encontrado')
            User.diccUsers[nickname].mostrar_perfil()
        except ValueError as e:
            print(e)
    def