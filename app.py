from tkinter import Tk, Label, Entry, Frame, messagebox, mainloop, Button
from PIL import ImageTk, Image

class Entrar():

    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry('500x700')

        fondo = 'lightsalmon'

        self.frame_superior = Frame(self.ventana)
        self.frame_superior.configure(background=fondo)
        self.frame_superior.pack(fill='both', expand=True)

        self.frame_inferior = Frame(self.ventana)
        self.frame_inferior.configure(background=fondo)
        self.frame_inferior.pack(fill='both', expand=True)

        self.frame_superior.columnconfigure(0, weight=1)
        self.frame_inferior.columnconfigure(1, weight=1)

        self.img = Image.open('imagen2.jpg')
        self.img = self.img.resize((250, 400))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame_superior, image=self.render, bg=fondo)
        self.fondo.pack(expand=True, fill='both')

        mainloop()