from tkinter import Tk, Label, Entry, Frame, messagebox, mainloop, Button
from PIL import ImageTk, Image
from app import Entrar
class Login:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry('500x700')   #Tamaño ventana
        self.ventana.title('INSPIRATION')  #Titulo de la ventana

        fondo = 'lightsalmon'

        #PARTE DE FRAMES
        self.frame_superior = Frame(self.ventana)          #Parte superior de la pantalla
        self.frame_superior.configure(background=fondo)    #Cambiar fondo
        self.frame_superior.pack(fill='both', expand=True) #'pack' = crear interface grafica,
                                                           #'fill' = indica la cantidad de espacio que tiene que rellenar el widget

        self.frame_inferior = Frame(self.ventana)
        self.frame_inferior.configure(background=fondo)
        self.frame_inferior.pack(fill='both', expand=True)

        self.frame_superior.columnconfigure(0, weight = 1) #El primer parametro indica que utiliza la primera columna de frame_interior
        self.frame_inferior.columnconfigure(1, weight=1)   #Weight indica como se distribuye en el espacio de la interfaz

        #PARTE DE TÍTULO
        self.titulo = Label(self.frame_superior,     #Crea una etiqueta en la parte superior de la pantalla
                            text = 'ERES PERFECTA!',          #texto que aparece en la parte superior
                            font = ('Times', 36, 'bold'), #la fuente del texto y demas
                            bg = fondo               #Color del fondo
                            )

        self.titulo.pack(side = 'top',  #Indica la posicion en la que estara lo indicado anteriormente, en la parte superior de la parte superior
                         pady = 20)     #Los pixels que tiene arriba y abajo el texto

        #PARTE IMAGENES
        self.img = Image.open('imagen2.PNG')   #lee la imagen
        self.img = self.img.resize((400, 400))  #tamaño de la imagen
        self.render = ImageTk.PhotoImage(self.img) #carga la imagen y muestra la imagen como una etiqueta
        self.fondo = Label(self.frame_superior, image = self.render, bg = fondo) #Crea una etiqueta en la que indica lo que ha de verse en la parte superior de la interfaz
        self.fondo.pack(expand=True, fill = 'both') #lo de antes

        #PARTE DE DATOS
        self.label_usuario = Label(self.frame_inferior,   #En la parte inferior de la interfaz se añade lo siguiente
                                   text = 'Usuario: ',
                                   font= ('Times', 18),
                                   bg = fondo,
                                   fg = 'black') #fg es el color de la letra de 'usuario'

        self.label_usuario.pack(side='top',pady=20, expand = True)
        self.label_usuario.grid(row=0, column=0, padx=10, sticky='e') #Los primeros dos parametros indican la posicion
                                                                      #El tercer parametro es el margen de la derecha y la izq
                                                                      #Lo ultimo posicion con respecto a puntos cardinales


        self.entry_usuario= Entry(self.frame_inferior,  #Se crea un widget de entrada en la parte inferior
                                  bd=0,                 #grosor del borde de la entrada
                                  width = 14,           #ancho de entrada de caracteres
                                  bg='RosyBrown2',
                                  font = ('Times', 18))


        self.entry_usuario.grid(row = 0, column = 1, padx = 5, sticky='w') #El grid es para organizar los widgets en una cuadricula

        self.label_contraseña = Label(self.frame_inferior,
                                     text='Contraseña: ',
                                     font = ('Times', 18),
                                     bg=fondo,
                                     fg = 'black')

        self.label_contraseña.grid(row = 1, column = 0, pady = 10, sticky = 'e') #pady = margen de la y

        self.entry_contraseña = Entry(self.frame_inferior,
                                      bd = 0,
                                      width = 14,
                                      font = ('Times', 18),
                                      bg = 'RosyBrown2',
                                      show = '*')

        self.entry_contraseña.grid(row = 1, column = 1, padx = 5, sticky = 'w')

        self.boton = Button(self.frame_inferior,
                            text = 'Entrar',
                            width = 16,
                            font = ('Times',12),
                            bg = 'tomato',
                            fg = '#fff',
                            command = self.verificar)

        self.boton.grid(row = 2, column = 1, pady = 35, sticky = 'w')

        mainloop()


    def verificar(self):
        nombre = self.entry_usuario.get()
        contra = self.entry_contraseña.get()

        if nombre == 'elena' and contra == '123':
            self.ventana.destroy()
            Entrar()
        else:
            messagebox.showinfo('Acceso incorrecto', 'Algún dato es erroneo')


Login()