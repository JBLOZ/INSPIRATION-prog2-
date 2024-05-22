import tkinter
from tkinter import Tk, Label, Entry, Frame, mainloop, Button
from tkinter.scrolledtext import ScrolledText
from PIL import ImageTk, Image
from Users import User, Data



class Escribir():
    def __init__(self, usuario):

        self.usuario = usuario
        self.ventana = Tk()

        self.texto = Text(self.ventana,
                            width= 48,
                            height= 10,
                            wrap = 'word',
                            bg = 'white',
                            fg = 'black',
                            padx = 40,
                            pady = 30,
                            font= ('Helvetica', 12))
        self.texto.pack()

        self.img = Image.open('imagen2.png')
        self.img = self.img.resize((25, 25))
        self.cargar = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.ventana, image=self.cargar, bg='white')
        self.fondo.pack(expand=True, fill='both', side='left')
        self.fondo.place(x=0, y=1)

        #boton
        self.boton_publicar = Button(self.ventana,
                                     text = 'Publicar',
                                     width = 10,
                                     font = ('Helvetica', 12),
                                     bg = 'lightsalmon',
                                     fg = 'white',
                                     command = self.publicar)

        self.boton_publicar.pack(expand=True,side='right' )
        self.fondo.place(x=0, y=1)


        mainloop()
    def publicar(self):

        texto = self.texto.get('1.0', 'end')
        self.usuario.create_inspiration(texto)
        Data().guardar_usuarios()
        self.ventana.destroy()
        Entrar(self.usuario)






