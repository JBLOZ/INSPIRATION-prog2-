# Clase de los tweets
import datetime as dt
from User import User

class Inspirations():
    def __init__(self, user:User, text):
        self.user = user
        self.text = text
        self.likes = []
        self.comments = []
        self.fecha = dt.datetime.now()

    # Añadir like a un inspiration
    def add_like(self, like):
        self.likes.append(like)

    # Borrar like de un inspiration
    def delete_like(self, like):
        if like in self.likes:
            self.likes.remove(like)

    # Añadir comentario a un inspiration
    def add_comment(self, comment):
        self.comments.append(comment)

    # Borrar comentario de un inspiration
    def delete_comment(self, comment):
        if comment in self.comments:
            self.comments.remove(comment)

    # Reinspiration
    def reinspiration(self, user):
        user.__add__(self)

        







