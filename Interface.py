'''
Este módulo implementa una interfaz gráfica utilizando la biblioteca tkinter.
Incluye clases para manejar la ventana principal, inicio de sesión, registro, y funcionalidades de usuario como crear y ver inspirations.

Módulos utilizados:
    - tkinter
    - PIL
    - Users (clase User y Data)
    - Inspiration

Clases:
    - Principal
    - Login
    - Registrarse
    - Entrar
    - Escribir
    - ShowInspirations
    - InspirationInterfaz
    - BuscarPersona
'''

import tkinter
from tkinter import Tk, Label, Entry, Frame, messagebox, mainloop, Button, LabelFrame, Scrollbar, Canvas
from tkinter.scrolledtext import ScrolledText
from PIL import ImageTk, Image
from Users import User, Data
from Inspiration import Inspiration

class Principal:
    '''
        Clase que define la ventana principal de la aplicación.

        Métodos:
            - __init__: Inicializa la ventana principal.
            - abrir_iniciar: Abre la ventana de inicio de sesión.
            - abrir_reg: Abre la ventana de registro.
        '''
    def __init__(self):
        """Inicializa la ventana principal y su contenido."""
        Data().lectura_usuarios()
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
        '''Destruye la ventana actual y abre la ventana de inicio de sesión.'''
        self.ventana.destroy()
        Login()

    def abrir_reg(self):
        '''Destruye la ventana actual y abre la ventana de registro.'''
        self.ventana.destroy()
        Registrarse()

class Login:
   '''
        Clase que define la ventana de inicio de sesión.

        Métodos:
            - __init__: Inicializa la ventana de inicio de sesión.
            - retroceder1: Regresa a la ventana principal.
            - acceso: Verifica las credenciales del usuario.
        '''
   def __init__(self):
        '''Inicializa la ventana de inicio de sesión y su contenido.'''
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

        self.retroceder = Button(self.frame_inferior,
                                 text='↩',
                                 width=5,
                                 font=('Times', 15),
                                 bg='salmon',
                                 fg='#fff',
                                 command=self.retroceder1)

        self.retroceder.place(x=0, y=1)

        mainloop()

   def retroceder1(self):
        '''Destruye la ventana actual y regresa a la ventana principal.'''
        self.ventana.destroy()
        Principal()
   def acceso(self):
        '''Verifica las credenciales del usuario y permite el acceso si son correctas.'''
        try:
            nombre = self.entradas[0].get()
            contra = self.entradas[1].get()
            Data().lectura_usuarios()
            if nombre in Data.diccUsers:  # Verifica que el usuario exista
                if contra == Data.diccUsers[nombre]._password:

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
    '''
       Clase que define la ventana de registro de usuario.

       Métodos:
           - __init__: Inicializa la ventana de registro.
           - retroceder1: Regresa a la ventana principal.
           - verificar: Verifica los datos de registro del usuario.
       '''
    def __init__(self):
        """Inicializa la ventana de registro y su contenido."""
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

        self.retroceder = Button(self.frame_inferior,
                                text='↩',
                                width=5,
                                font=('Times', 15),
                                bg='salmon',
                                fg='#fff',
                                command=self.retroceder1)

        self.retroceder.place(x=0, y=1)

        mainloop()

    def retroceder1(self):
        '''Destruye la ventana actual y regresa a la ventana principal.'''
        self.ventana.destroy()
        Principal()

    def verificar(self):
        '''Verifica los datos de registro y crea un nuevo usuario si son válidos.'''
        nombre = self.entradas[0].get()
        user = self.entradas[1].get()
        edad = self.entradas[2].get()
        email = self.entradas[3].get()
        contra = self.entradas[4].get()


        AVerificar = User(name=nombre, nickname=user, email=email, _password=contra)

        if not(AVerificar.check_name()):
            messagebox.showinfo('Acceso incorrecto', 'Nombre no válido. Debe empezar con mayúscula')

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
            Data().guardar_user_passw()
            messagebox.showinfo('Registro exitoso', 'Usuario registrado con éxito')
            self.ventana.destroy()
            Entrar(AVerificar)

class Entrar:
    '''
        Clase que define la ventana principal una vez el usuario ha iniciado sesión.

        Métodos:
            - __init__: Inicializa la ventana principal después del inicio de sesión.
            - escribir: Abre la ventana para escribir un inspiration.
            - mostrar: Muestra los inspirations del usuario.
            - buscar_persona: Abre la ventana para buscar inspirations de otros usuarios.
            - retroceder: Regresa a la ventana de inicio de sesión.
        '''
    def __init__(self, usuario):
        '''Inicializa la ventana principal después del inicio de sesión y su contenido.'''
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
        self.nom_bot = ['Crear Inspiration','Inspirations', 'Mis Inspirations', 'Buscar persona']
        self.listita =[self.crear_inspiration, self.mostrar_mis_inspirations, self.mostrar_inspirations,self.buscar_personas]
        for i in range(4):
            self.boton = Button(self.frames[1],
                                text=self.nom_bot[i],
                                width=20,
                                height = 1,
                                bd = 1,
                                font=('Times', 18),
                                bg='lightcoral',
                                fg='#fff',
                                command = self.listita[i])

            # Ajuste del padding para mayor proximidad entre botones
            self.boton.grid(row=i, column=0, columnspan=2, padx=5, pady=2)
            self.botones.append(self.boton)

        mainloop()

    def crear_inspiration(self):
        '''Abre la ventana para escribir un nuevo inspiration.'''
        self.ventana.destroy()
        Escribir(self.usuario)

    def mostrar_inspirations(self):
        '''Abre la ventana para mostrar los inspirations del usuario.'''
        self.ventana.destroy()
        ShowInspirations(self.usuario, False)

    def mostrar_mis_inspirations(self):
        '''Abre la ventana para mostrar los inspirations del usuario.'''
        self.ventana.destroy()
        ShowInspirations(self.usuario, True)

    def buscar_personas(self):
        '''Abre la ventana para buscar otros usuarios.'''
        self.ventana.destroy()
        BuscarPersona(self.usuario)

class Escribir():
    '''
       Clase que define la ventana para escribir un nuevo inspiration.

       Métodos:
           - __init__: Inicializa la ventana para escribir un inspiration.
           - retroceder: Regresa a la ventana principal.
           - publicar: Publica el inspiration escrito.
       '''
    def __init__(self, usuario):
        '''Inicializa la ventana para escribir un inspiration y su contenido.'''

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

        self.retroceder = Button(self.ventana,
                                 text='↩',
                                 width=2,
                                 font=('Times', 15),
                                 bg='lightsalmon',
                                 fg='#fff',
                                 command=self.retroceder1)
        self.retroceder.pack(expand=True, side='right')

        mainloop()

    def retroceder1(self):
        ''' Destruye la ventana actual y regresa a la ventana principal. '''
        self.ventana.destroy()
        Entrar(self.usuario)

    def publicar(self):
        '''Publica la inspiración escrita y la guarda en el perfil del usuario.'''
        texto = self.texto.get("1.0", tkinter.END).strip()
        self.usuario.create_inspiration(texto)
        print(texto)
        self.ventana.destroy()
        Entrar(self.usuario)


class ShowInspirations:
    '''
        Clase que define la ventana para mostrar los inspirations del usuario.

        Métodos:
            - __init__: Inicializa la ventana para mostrar los inspirations.
            - retroceder: Regresa a la ventana principal.
        '''
    def __init__(self, usuario, mios=False):
        '''Inicializa la ventana para mostrar los inspìrations del usuario y su contenido.'''
        fondo = 'antiquewhite'
        self.usuario = usuario

        self.ventana = Tk()
        self.ventana.geometry('500x700')
        self.ventana.title('Inspirations')

        # Crear un widget Scrollbar
        self.scrollbar = Scrollbar(self.ventana)
        self.scrollbar.pack(side='right', fill='y')

        # Crear un Canvas para crear un área en la que estará el texto
        self.canvas = Canvas(self.ventana)
        self.canvas.pack(fill='both', expand=True)

        # Crear un frame dentro del área donde se encuentra el texto
        self.frame_textos = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame_textos, anchor='nw')

        if mios :
            self.textos = self.usuario.listaInspirations
        else:
            self.textos = self.usuario.show_inspirations()

        try:
            if len(self.textos) == 0:
                Label(self.canvas,
                      text='No hay inspirations',
                      font=('Times', 18)).pack(expand=True)

                raise ValueError('No hay inspirations')

            else:
                self.textos = self.usuario.show_inspirations()
                for inspiration in self.textos:
                    InspirationInterfaz(self, inspiration, fondo)
        except ValueError as e:
            print(e)

        self.retroceder = Button(self.canvas,
                                 text='↩',
                                 width=2,
                                 height=1,
                                 font=('Times', 7),
                                 bg='brown',
                                 fg='#fff',
                                 command=self.retroceder1)
        self.retroceder.place(x=0, y=1)

        mainloop()

    def retroceder1(self):
        '''Destruye la ventana actual y regresa a la ventana principal.'''
        self.ventana.destroy()
        Entrar(self.usuario)


class InspirationInterfaz:
    '''
        Clase que define los inspirations como etiquetas.

        Métodos:
        - __init__: Inicializa la ventana.
        - bt_me_gusta: registra y actualiza el estado de "Me gusta" de un inspiration.
    '''

    def __init__(self, padre, inspiration, fondo):
        self.padre = padre
        self.inspiration = inspiration

        self.frame = LabelFrame(self.padre.frame_textos, text=f'@{self.inspiration.user.nickname}')
        self.frame.pack(pady=15, padx=20)

        # Etiqueta para mostrar la fecha en la parte superior derecha
        self.fecha_label = Label(self.frame,
                                    text=inspiration.fecha.strftime('%H:%M    %m-%d'),
                                    font=('Times', 9),
                                    bg=fondo,
                                    fg='black')

        self.fecha_label.pack(side='top', anchor='ne', padx=5, pady=5)

        self.texto = Label(self.frame,
                              text=inspiration.text,
                              font=('Times', 12),
                              bg=fondo,
                              fg='black',
                              padx=20,
                              width=45,
                              height=5)
        self.texto.pack(fill='both', expand=True)

        self.botonMg = Button(self.frame,
                                 text='ME GUSTA',
                                 font=('Times', 9),
                                 bg='tomato' if self.padre.usuario in inspiration.likes else 'antiquewhite',
                                 fg='black',
                                 command=self.bt_me_gusta)

        self.labelMg = Label(self.frame,
                                text=f'{len(inspiration.likes)}',
                                font=('Times', 9),
                                bg=fondo,
                                fg='black')
        self.labelMg.pack(side='left')

        self.botonMg.pack(side='left')  # Empaquetar el botón en una línea separada

        self.boton2 = Button(self.frame,
                                text='COMENTAR',
                                font=('Times', 9),
                                bg=fondo,
                                fg='black')
        self.boton2.pack(side='right')  # Empaquetar el botón en una línea separada

    def bt_me_gusta(self):
        self.padre.usuario.me_gusta(self.inspiration)
        self.botonMg.configure(bg='tomato' if self.padre.usuario in self.inspiration.likes else 'antiquewhite')
        self.labelMg.configure(text=f'{len(self.inspiration.likes)}')


class BuscarPersona:
    '''
        Clase que define la ventana para buscar usuarios registrados y seguir o dejar de seguir..

        Métodos:
            - __init__: Inicializa la ventana para buscar inspirations de otros usuarios.
            - mostrar_usuarios: muestra los usuarios según el carácter introducido.
            - retroceder: Regresa a la ventana principal.
            - seguir_usuario: permite seguir a un usuario.
            - dejar_seguir_usuario: permite dejar de seguir a un usuario.
        '''
    def __init__(self, usuario):
        self.usuario = usuario
        self.data = Data()
        self.data.lectura_usuarios()

        self.ventana = Tk()
        self.ventana.geometry('500x700')
        self.ventana.title('BUSCADOR')
        self.ventana.configure(bg='antiquewhite')

        self.frame_top = Frame(self.ventana, bg='antiquewhite')
        self.frame_top.pack(pady=10)

        # Cargar la imagen
        self.img = Image.open('imagen2.png')
        self.img = self.img.resize((25, 25))
        self.cargar = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame_top, image=self.cargar, bg='antiquewhite')
        self.fondo.grid(row=0, column=0, padx=5, pady=10, sticky='w')

        self.buscador = Entry(self.frame_top, width=14, bg='mistyrose', font=('Times', 14) )
        self.buscador.grid(row=0, column=1, padx=5, pady=10)

        self.buscar_boton = Button(self.frame_top, text='Buscar',bg = 'lightsalmon', command=self.mostrar_usuarios)
        self.buscar_boton.grid(row=0, column=2, padx=5, pady=10)

        self.canvas_bottom = Canvas(self.ventana, bg='antiquewhite')
        self.canvas_bottom.pack(side='left', fill='both', expand=True)

        self.scrollbar = Scrollbar(self.ventana, orient='vertical', bg='antiquewhite',command=self.canvas_bottom.yview)
        self.scrollbar.pack(side='right', fill='y')

        self.canvas_bottom.configure(yscrollcommand=self.scrollbar.set)

        self.frame_bottom = Frame(self.canvas_bottom, bg='antiquewhite')
        self.canvas_bottom.create_window((0, 0), window=self.frame_bottom, anchor='nw')

        self.frame_bottom.bind('<Configure>', self.on_frame_configure)

        self.retroceder = Button(self.ventana,
                                 text='↩',
                                 width=5,
                                 font=('Times', 10),
                                 bg='salmon',
                                 fg='#fff',
                                 command=self.retroceder1)
        self.retroceder.place(x=0, y=1)

        mainloop()

    def retroceder1(self):
        self.ventana.destroy()
        Entrar(self.usuario)

    def on_frame_configure(self, event):
        self.canvas_bottom.configure(scrollregion=self.canvas_bottom.bbox("all"))

    def mostrar_usuarios(self):
        # Clear previous results
        for widget in self.frame_bottom.winfo_children():
            widget.destroy()

        # Get the text from the search entry
        search_text = self.buscador.get().lower()
        self.lista_usuarios = []
        i = 0

        search_usu =  User().search_user(search_text)
        if self.usuario.nickname in search_usu:
            search_usu.remove(self.usuario.nickname)
        else:
            search_usu == search_usu

        # Add matching users to the result frame
        for usuario in search_usu:

            etiqueta = Label(self.frame_bottom, bg='antiquewhite',text=usuario)
            etiqueta.grid(row=i, column=0, padx=5, pady=5, sticky='w')

            if usuario in self.usuario.listaSiguiendo:
                texto = 'Dejar de seguir'
                command = lambda u=usuario: self.dejar_seguir_usuario(u)
            else:
                texto = 'Seguir'
                command = lambda u=usuario: self.seguir_usuario(u)

            seguir_boton = Button(self.frame_bottom,bg='peachpuff',text=texto, command=command)
            seguir_boton.grid(row=i, column=1, padx=5, pady=5, sticky='w')

            self.lista_usuarios.append(usuario)
            i += 1

            # Update the scroll region
        self.frame_bottom.update_idletasks()
        self.canvas_bottom.configure(scrollregion=self.canvas_bottom.bbox("all"))

    def seguir_usuario(self, usuario_seguir):
        self.usuario.follow(usuario_seguir)
        self.mostrar_usuarios()

    def dejar_seguir_usuario(self, usuario_dejar):
        self.usuario.unfollow(usuario_dejar)
        self.mostrar_usuarios()


Principal()