import tkinter
from tkinter import Tk, Label, Entry, Frame, messagebox, mainloop, Button, LabelFrame, Scrollbar, Canvas
from tkinter.scrolledtext import ScrolledText
from PIL import ImageTk, Image
from Users import User, Data
from Inspiration import Inspiration


Data().lectura_usuarios()

class Principal:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry('500x700')
        self.ventana.title('INSPIRATION')  # Titulo de la ventana

        fondo = 'lightsalmon'

        self.frames = []
        for i in range(2):
            self.frame = Frame(self.ventana)
            self.frame.configure(background=fondo)
            self.frame.pack(fill='both', expand=True)
            self.frame.columnconfigure(i, weight=1)

            self.frames.append(self.frame)


        # PARTE DE TÍTULO
        self.titulo = Label(self.frames[0],  # Crea una etiqueta en la parte superior de la pantalla
                            text='INSPIRATION',  # texto que aparece en la parte superior
                            font=('Times', 36, 'bold'),  # la fuente del texto y demas
                            bg=fondo  # Color del fondo
                            )
        self.titulo.pack(side='top',# Indica la posicion en la que estara lo indicado anteriormente, en la parte superior de la parte superior
                         pady=20)  # Los pixels que tiene arriba y abajo el texto

        #PARTE IMAGEN
        self.img = Image.open('imagen2.png')
        self.img = self.img.resize((175, 215))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frames[0], image=self.render, bg=fondo)
        self.fondo.pack(expand=True, fill='both')

        #PARTE BOTONES
        #Botón iniciar sesion
        self.boton_iniciar = Button(self.frames[1],
                            text = 'Iniciar Sesión',
                            width = 16,
                            font = ('Times',12),
                            bg = 'tomato',
                            fg = '#fff',
                            command = self.abrir_iniciar)

        self.boton_iniciar.grid(row=0, column=0, pady=35, sticky='e')
        self.boton_iniciar.place(relx=0.5,rely=0.3,anchor=tkinter.CENTER)

        #Botón registrarse
        self.boton_reg = Button(self.frames[1],
                                    text='Registrarse',
                                    width=16,
                                    font=('Times', 12),
                                    bg='tomato',
                                    fg='#fff',
                                    command = self.abrir_reg)

        self.boton_reg.grid(row=1, column=0, pady=35, sticky='e')
        self.boton_reg.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)

        mainloop()

    def abrir_iniciar(self):
        self.ventana.destroy()
        Login()

    def abrir_reg(self):
        self.ventana.destroy()
        Registrarse()

class Login:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry('500x700')
        self.ventana.title('INSPIRATION')

        fondo = 'lightsalmon'

        self.frame_inferior = Frame(self.ventana, bg=fondo)
        self.frame_inferior.pack(fill='both', expand=True)

        # Configurar el grid del frame_inferior para que se expanda
        for i in range(3):  # 5 filas para etiquetas y entradas + 1 fila para el botón
            self.frame_inferior.grid_rowconfigure(i, weight=1)

        self.frame_inferior.grid_columnconfigure(0, weight=1)
        self.frame_inferior.grid_columnconfigure(1, weight=1)

        self.img = Image.open('imagen2.png')
        self.img = self.img.resize((150, 200))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame_inferior, image=self.render, bg=fondo)
        self.fondo.grid(row=0, column=0, columnspan=2, pady=20)

        # Crear 5 etiquetas y entradas
        self.etiquetas = []
        self.entradas = []
        self.nom_etiq = ['Usuario', 'Contraseña']
        for i in range(2):
            etiqueta = Label(self.frame_inferior,
                             text=f'{self.nom_etiq[i]} :',
                             font=('Times', 14),
                             bg=fondo,
                             fg='black')
            etiqueta.grid(row=i + 1, column=0, padx=10, sticky='e')
            self.etiquetas.append(etiqueta)

            entrada = Entry(self.frame_inferior,
                            bd=2,
                            width=14,
                            bg='RosyBrown2',
                            font=('Times', 14),
                            show='*' if i == 1 else None)

            entrada.grid(row=i + 1, column=1, padx=10, sticky='w')
            self.entradas.append(entrada)

        # Botón debajo de todas las entradas
        self.boton2 = Button(self.frame_inferior,
                             text='Entrar',
                             width=14,
                             font=('Times', 12),
                             bg='tomato',
                             fg='#fff',
                             command = self.acceso )

        self.boton2.grid(row=3, column=0, columnspan=2, pady=100)

        mainloop()

    def acceso(self):
        try:
            nombre = self.entradas[0].get()
            contra = self.entradas[1].get()
            Data().lectura_usuarios()
            if nombre in Data.diccUsers:  # Verifica que el usuario exista
                if contra == Data.diccUsers[nombre].password:

                    self.ventana.destroy()
                    userAct = Data.diccUsers[nombre]
                    Entrar(userAct)
                else:
                    raise ValueError('Datos incorrectos')
                    messagebox.showinfo('Acceso incorrecto', 'Algún dato es erroneo')
            else:
                raise ValueError('Usuario no encontrado')
                messagebox.showinfo('Acceso incorrecto', 'Usuario no encontrado')

        except ValueError as e:
            messagebox.showinfo('Acceso incorrecto', 'Algún dato es erroneo')
            print(e)

class Registrarse:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry('500x700')
        self.ventana.title('INSPIRATION')

        fondo = 'lightsalmon'

        self.frame_inferior = Frame(self.ventana, bg=fondo)
        self.frame_inferior.pack(fill='both', expand=True)

        # Configurar el grid del frame_inferior para que se expanda
        for i in range(7):  # 5 filas para etiquetas y entradas + 1 fila para el botón
            self.frame_inferior.grid_rowconfigure(i, weight=1)

        self.frame_inferior.grid_columnconfigure(0, weight=1)
        self.frame_inferior.grid_columnconfigure(1, weight=1)

        self.img = Image.open('imagen2.png')
        self.img = self.img.resize((150, 200))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame_inferior, image=self.render, bg=fondo)
        self.fondo.grid(row=0, column=0, columnspan=2, pady=20)

        # Crear 5 etiquetas y entradas
        self.etiquetas = []
        self.entradas = []
        self.nom_etiq = ['Nombre', 'Nombre de usuario', 'Edad', 'Email', 'Contraseña']
        for i in range(1, 6):
            etiqueta = Label(self.frame_inferior,
                             text=f'{self.nom_etiq[i - 1]} :',
                             font=('Times', 14),
                             bg=fondo,
                             fg='black')
            etiqueta.grid(row=i, column=0, padx=10, pady=0, sticky='e')
            self.etiquetas.append(etiqueta)


            entrada = Entry(self.frame_inferior,
                            bd=2,
                            width=14,
                            bg='RosyBrown2',
                            font=('Times', 14),
                            show = '*' if i==5 else None)

            entrada.grid(row=i, column=1, padx=10, pady=0, sticky='w')
            self.entradas.append(entrada)

        # Botón debajo de todas las entradas
        self.boton3 = Button(self.frame_inferior,
                             text='Registrarse',
                             width=14,
                             font=('Times', 12),
                             bg='tomato',
                             fg='#fff',
                             command = self.verificar)

        self.boton3.grid(row=6, column=0, columnspan=2, pady=20)

        mainloop()

    def verificar(self):
        nombre = self.entradas[0].get()
        user = self.entradas[1].get()
        edad = self.entradas[2].get()
        email = self.entradas[3].get()
        contra = self.entradas[4].get()


        AVerificar = User(name=nombre, nickname=user, email=email, password=contra)

        if not(AVerificar.check_name()):
            messagebox.showinfo('Acceso incorrecto', 'Nombre no válido')

        elif not(AVerificar.check_nickname()):
            messagebox.showinfo('Acceso incorrecto', 'Nombre de usuario no válido')

        elif edad.isdigit() == False:
            messagebox.showinfo('Acceso incorrecto', 'Edad no válida')

        elif int(edad) < 14:
            messagebox.showinfo('Acceso incorrecto', 'Debes ser mayor de 14 años')
            self.ventana.destroy()

        elif not(AVerificar.check_email()):
            messagebox.showinfo('Acceso incorrecto', 'Email no válido')

        elif not(AVerificar.check_password()):
            messagebox.showinfo('Acceso incorrecto', 'La contraseña no es válida')

        else:
            Data.diccUsers[user] = AVerificar
            Data().guardar_usuarios()
            messagebox.showinfo('Registro exitoso', 'Usuario registrado con éxito')
            self.ventana.destroy()
            Entrar(AVerificar)

class Entrar:
    def __init__(self, usuario):

        self.usuario = usuario
        self.ventana = Tk()
        self.ventana.geometry('500x700')
        self.ventana.title('INSPIRATION')

        fondo = 'antiquewhite'

        self.frames = []
        for i in range(2):
            self.frame = Frame(self.ventana, bg=fondo)
            self.frame.pack(fill='both', expand=True)
            self.frames.append(self.frame)

        for i in range(4):
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
                            text= usuario.name,
                            font=('Times', 40, 'bold'),
                            bg=fondo,
                            fg='lightsalmon')
        self.titulo.grid(row=0, column=0, padx=10, pady=2, columnspan=2)

        # Insertar subtítulo
        self.subtitulo = Label(self.frames[0],
                               text=f'@{usuario.nickname}',
                               font=('Times', 15),
                               bg=fondo,
                               fg='lightsalmon')
        self.subtitulo.grid(row=1, column=0, padx=10, pady=5, columnspan = 2)

        # Etiquetas números
        self.lista_num = [len(usuario.listaSiguiendo),len(usuario.listaSeguidores)]  # poner los numeros correspondientes de cada usuario
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
        self.nom_bot = ['Crear Inspiration','Mis Inspirations', 'Inspirations', 'Buscar persona']
        for i in range(4):
            self.boton = Button(self.frames[1],
                                text=self.nom_bot[i],
                                width=20,
                                height = 1,
                                bd = 1,
                                font=('Times', 18),
                                bg='lightcoral',
                                fg='#fff',
                                command = self.escribir_boton if i==0 self.mostrar_insp if i==2 else None)

            # Ajuste del padding para mayor proximidad entre botones
            self.boton.grid(row=i, column=0, columnspan=2, padx=5, pady=2)
            self.botones.append(self.boton)

        mainloop()

    def escribir_boton(self):
        self.ventana.destroy()
        Escribir(self.usuario)

    def mostrar_insp(self):
        self.ventana.destroy()
        MyInspirations(self.usuario)

class Escribir():
    def __init__(self, usuario):

        self.usuario = usuario
        self.ventana = Tk()

        self.texto = (ScrolledText(self.ventana,
                                  width= 48,
                                  height= 10,
                                  wrap = 'word',
                                  bg = 'white',
                                  fg = 'black',
                                  padx = 40,
                                  pady = 30,
                                  font= ('Helvetica', 12)))
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
        texto = self.texto.get("1.0", tkinter.END).strip()
        self.usuario.create_inspiration(texto)
        print(texto)
        self.ventana.destroy()
        Entrar(self.usuario)

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

        self.textos = self.usuario.show_inspirations()
        for inspiration in self.textos:
            self.frame = LabelFrame(self.frame_textos, text=self.usuario)
            self.frame.pack(pady=15, padx = 15)

            self.texto = Label(self.frame,
                               text=inspiration,
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
                                bg='antiquewhite' if self.usuario.comprobar_mg(inspiration) == False else 'tomato',
                                fg='black'
                                )
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

        self.usuario.me_gusta()

    def cambiar_color(self):
        if self.usuario.comprobar_mg() == False:
            self.boton.configure(bg = 'tomato')

        else:
            self.boton = self.boton'''


Data().lectura_usuarios()
print(Data.diccUsers['jord'].password)
Principal()


print(Data.diccUsers['jord'].listaInspirations[0].text)









