import tkinter
from tkinter import Tk, Label, Entry, Frame, messagebox, mainloop, Button
from PIL import ImageTk, Image
from Users import User, Data

Data().lectura_usuarios()

class Entrar:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry('500x700')
        self.ventana.title('INSPIRATION')

        fondo = 'antiquewhite'

        self.frames = []
        for i in range(2):
            self.frame = Frame(self.ventana, bg=fondo)
            self.frame.pack(fill='both', expand=True)
            self.frames.append(self.frame)

        for i in range(3):
            self.frames[0].rowconfigure(i, weight=1)
            self.frames[0].columnconfigure(i, weight=1)

            self.frames[1].rowconfigure(i, weight=1)
            self.frames[1].columnconfigure(i, weight=1)

        #IMAGEN Y TAL
        self.img = Image.open('imagen2.png')
        self.img = self.img.resize((25, 25))
        self.cargar = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frames[0], image=self.cargar, bg=fondo)
        self.fondo.pack(expand=True, fill='both', side='left')
        self.fondo.place(x=0, y=1)

        # Insertar título
        self.titulo = Label(self.frames[0],
                            text=f'Elena ',
                            font=('Times', 40, 'bold'),
                            bg=fondo,
                            fg='lightsalmon')
        self.titulo.grid(row=0, column=0, padx=10, pady=2, columnspan=2)

        # Insertar subtítulo
        self.subtitulo = Label(self.frames[0],
                               text='@elena333',
                               font=('Times', 15),
                               bg=fondo,
                               fg='lightsalmon')
        self.subtitulo.grid(row=1, column=0, padx=10, pady=5, columnspan = 2)

        # Etiquetas números
        self.lista_num = ['110', '1365']  # poner los numeros correspondientes de cada usuario
        self.lista_etiq = ['Seguidos', 'Seguidores']
        self.etiquetas = []

        # Configuración para centrar las etiquetas
        for i in range(2):
            self.etiqueta = Label(self.frames[0],
                                  text=f'{self.lista_num[i]} {self.lista_etiq[i]}',
                                  font=('Times', 20),
                                  bg=fondo,
                                  fg='black')
            self.etiqueta.grid(row=2, column=i, padx=10, pady=10, sticky='')

            self.etiquetas.append(self.etiqueta)

        # Botones
        self.botones = []
        self.nom_bot = ['Mis inspirations', 'Inspirations', 'Buscar persona']
        for i in range(3):
            self.boton = Button(self.frames[1],
                                text=self.nom_bot[i],
                                width=20,
                                height = 1,
                                bd = 1,
                                font=('Times', 18),
                                bg='lightcoral',
                                fg='#fff')
            # Ajuste del padding para mayor proximidad entre botones
            self.boton.grid(row=i, column=0, columnspan=2, padx=5, pady=2)
            self.botones.append(self.boton)

        mainloop()