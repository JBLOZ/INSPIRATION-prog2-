import User

class Client(User.User):
    def __init__(self, nickname, password, nombre, apellido, edad, listaSeguidores, listaSiguiendo):
        super().__init__(nickname, password, nombre, apellido, edad, listaSeguidores, listaSiguiendo)
        self.listaInspirations = []


    def show_inspirations(self):
        pass

    def create_inspiration(self):
        pass

    def search_users(self):
        pass

    def show_profile(self):
        pass

