import tkinter
from tkinter import *
from Inspiration import Inspiration
from Users import User
class MyInspirations:
    def __init__(self, usuario):
        fondo = 'antiquewhite'
        self.usuario = usuario

        self.ventana = Tk()
        self.ventana.geometry('500x700')
        self.ventana.title('Inspirations')

        # Crear un widget Scrollbar
        self.scrollbar = Scrollbar(self.ventana)
        self.scrollbar.pack(side='right', fill='y')

        # Crear un Canvas para crear un area en la que estara el texto
        self.canvas = Canvas(self.ventana)
        self.canvas.pack(fill='both', expand=True)

        # Crear un frame dentro del area donde se encuentra el textp
        self.frame_textos = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame_textos, anchor='nw') #Se crea una ventana en la posicion (0,0)  en la que colocaremos los textos

        self.textos= ['No hay mal que por bien no venga', 'Dios los crea y ellos se juntan', 'A caballo regalado no le quites el dentado', 'Con dios', 'Al mal tiempo buena cara', 'La avaricia rompe el saco']
        for texto in self.textos:
            self.frame = LabelFrame(self.frame_textos, text='@elena')
            self.frame.pack(pady=15, padx = 15)

            self.texto = Label(self.frame,
                               text=texto,
                               font=('Times', 12),
                               bg=fondo,
                               fg='black',
                               padx=20,
                               width=45,
                               height=5)
            self.texto.pack(fill='both', expand=True)

            self.boton = Button(self.frame,
                                text='ME GUSTA',
                                font=('Times', 9),
                                bg=fondo,
                                fg='black')
            self.boton.pack(side='left')  # Empaquetar el botón en una línea separada

            self.boton2 = Button(self.frame,
                                text='COMENTAR',
                                font=('Times', 9),
                                bg=fondo,
                                fg='black')
            self.boton2.pack(side='right')  # Empaquetar el botón en una línea separada

        # Configurar el desplazamiento del canvas
        self.canvas.config(yscrollcommand=self.scrollbar.set) #se configura el scrollbar para que funcione de forma vincuada al frame
        self.scrollbar.config(command=self.canvas.yview) # Se configura el comando del scrollbar para que
                                                         # esté vinculado al método yview() del canvas que permite el
                                                         # desplazamiento vertical del frame canvas

        # Configurar la actualización del canvas cuando se modifica su tamaño
        self.frame_textos.bind('<Configure>', self.config_tamaño_frame) #event = configure para que se modifique el frame canvas cuando se desplace verticalmenta

        self.ventana.mainloop()

    def config_tamaño_frame(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all")) #para que todos los elementos del canvas tengan el mismo tamaño

    '''def megusta(self):

        Inspiration().add_like(self.usuario)'''

    def cambiar_color(self):
        if self.usuario.comprobar_mg():
            self.boton.configure(bg = 'tomato')
# Crear una instancia de la clase
MyInspirations()