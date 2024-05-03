# Clase de los tweets
import datetime as dt


class Inspiration():
    def __init__(self, user, text):
        self.user = user
        self.text = text
        self.likes = []
        self.comments = []
        self.fecha = dt.datetime.now()
        self.reinspirations = []

    # Añadir like a un inspiration
    def add_like(self, user):
        self.likes.append(user)

    # Borrar like de un inspiration
    def remove_like(self, user):
        if user in self.likes:
            self.likes.remove(user)

    # Añadir comentario a un inspiration
    def add_comment(self, user, comment):
        self.comments.append((user, comment))

    # Borrar comentario de un inspiration
    def remove_comment(self, user, comment):
        if (user, comment) in self.comments:
            self.comments.remove((user, comment))

"""
class Inspiratiion:
    def __init__(self):
        self.inspirations = []

    def add_inspiration(self, inspiration):
        self.inspiration.append(inspiration)

    def view_inspirations(self):
        if self.inspirations:
            print("Inspirations:")
            for i, inspiration in (self.inspirations):
                print(f'{i}. {inspiration}')
        else:
            print("Todavía no hay inspirations.")
            
"""

        







