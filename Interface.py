import tkinter
from tkinter import Tk, Label, Entry, Frame, messagebox, mainloop, Button
from PIL import ImageTk, Image
from Users import User, Data


class Principal:
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

        self.img = Image.open('imagen2.png')
        self.img = self.img.resize((175, 215))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame_superior, image=self.render, bg=fondo)
        self.fondo.pack(expand=True, fill='both')

        self.boton_iniciar = Button(self.frame_inferior,
                            text = 'Iniciar Sesión',
                            width = 16,
                            font = ('Times',12),
                            bg = 'tomato',
                            fg = '#fff',
                            command = self.abrir_iniciar)
        self.boton_iniciar.grid(row=0, column=0, pady=35, sticky='e')
        self.boton_iniciar.place(relx=0.5,rely=0.3,anchor=tkinter.CENTER)

        self.boton_reg = Button(self.frame_inferior,
                                    text='Registrarse',
                                    width=16,
                                    font=('Times', 12),
                                    bg='tomato',
                                    fg='#fff',
                                    command=self.abrir_reg
                                    )

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
                            text = 'INSPIRATION',          #texto que aparece en la parte superior
                            font = ('Times', 36, 'bold'), #la fuente del texto y demas
                            bg = fondo               #Color del fondo
                            )

        self.titulo.pack(side = 'top',  #Indica la posicion en la que estara lo indicado anteriormente, en la parte superior de la parte superior
                         pady = 20)     #Los pixels que tiene arriba y abajo el texto

        #PARTE IMAGENES
        self.img = Image.open('imagen2.PNG')   #lee la imagen
        self.img = self.img.resize((175, 215))  #tamaño de la imagen
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
                                  bd=2,                 #grosor del borde de la entrada
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
                                      bd = 2,
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
                            command = self.acceso)

        self.boton.grid(row = 2, column = 1, pady = 35, sticky = 'w')

        mainloop()


    def acceso(self):
        try:
            nombre = self.entry_usuario.get()
            contra = self.entry_contraseña.get()
            Data().lectura_usuarios()
            if nombre in Data.diccUsers:  # Verifica que el usuario exista
                if contra == Data.diccUsers[nombre].password:
                    self.ventana.destroy()
                    Entrar()
                else:
                    raise ValueError('Datos incorrectos')
            else:
                raise ValueError('Usuario no encontrado')

        except ValueError as e:
                messagebox.showinfo('Acceso incorrecto', 'Algún dato es erroneo')
                print(e)




class Entrar():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry('700x700')

        fondo = 'lightsalmon'

        self.frame_superior = Frame(self.ventana)
        self.frame_superior.configure(background=fondo)
        self.frame_superior.pack(fill='both', expand=True)

        self.frame_inferior = Frame(self.ventana)
        self.frame_inferior.configure(background=fondo)
        self.frame_inferior.pack(fill='both', expand=True)

        self.frame_superior.columnconfigure(0, weight=1)
        self.frame_inferior.columnconfigure(1, weight=1)

        self.img = Image.open('imagen2.png')
        self.img = self.img.resize((150, 200))
        self.cargar = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame_superior, image=self.cargar, bg=fondo)
        self.fondo.pack(expand=True, fill='both')

        mainloop()


class Registrarse:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry('500x700')
        self.ventana.title('INSPIRATION')

        fondo = 'lightsalmon'

        #PARTE DE FRAMES
        self.frame_superior = Frame(self.ventana)
        self.frame_superior.configure(background=fondo)
        self.frame_superior.pack(fill='both', expand=True)

        self.frame_inferior = Frame(self.ventana)
        self.frame_inferior.configure(background=fondo)
        self.frame_inferior.pack(fill='both', expand=True)

        self.frame_superior.columnconfigure(0, weight=1)
        self.frame_inferior.columnconfigure(1, weight=1)

        #PARTE DE IMAGEN
        self.img = Image.open('imagen2.png')
        self.img = self.img.resize((150, 200))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame_superior, image=self.render, bg=fondo)
        self.fondo.pack(expand=True, fill='both')

        #PARTE ETIQUETAS
        self.nombre = Label(self.frame_inferior,
                            text = 'Nombre: ',
                            font= ('Times', 15),
                            bg = fondo,
                            fg = 'black'
                            )
        self.nombre.pack(expand = True, fill = 'both')
        self.nombre.grid(row=0, column=0, padx=10, pady = 5, sticky='e')


        self.usu = Label(self.frame_inferior,
                            text='Nombre de usuario: ',
                            font=('Times', 15),
                            bg=fondo,
                            fg='black'
                            )

        self.usu.grid(row=2, column=0, padx=10,pady = 5, sticky='e')

        self.edad = Label(self.frame_inferior,
                          text = 'Edad: ',
                          font = ('Times', 15),
                          bg = fondo,
                          fg = 'black')

        self.edad.grid(row=4, column=0, padx=10,pady = 5, sticky='e')

        self.email = Label(self.frame_inferior,
                            text='Email: ',
                            font=('Times', 15),
                            bg=fondo,
                            fg='black'
                            )
        self.email.grid(row=6, column=0, padx=10,pady = 5, sticky='e')

        self.contraseña = Label(self.frame_inferior,
                            text='Contraseña: ',
                            font=('Times', 15),
                            bg=fondo,
                            fg='black'
                            )
        self.contraseña.grid(row=8, column=0, padx=10,pady = 5, sticky='e')

        #PARTE DE ENTRADAS
        self.entrar_nombre = Entry(self.frame_inferior,
                                   bd=2,
                                   width=14,
                                   bg='RosyBrown2',
                                   font=('Times', 12)
                                   )

        self.entrar_nombre.grid(row=0, column=1, padx=5,pady = 5, sticky = 'w')

        self.entrar_usu = Entry(self.frame_inferior,
                                   bd=2,
                                   width=14,
                                   bg='RosyBrown2',
                                   font=('Times', 12)

                                   )

        self.entrar_usu.grid(row=2, column=1, padx=5,pady = 5, sticky='w')

        self.entrar_edad = Entry(self.frame_inferior,
                                bd=2,
                                width=14,
                                bg='RosyBrown2',
                                font=('Times', 12)
                                )

        self.entrar_edad.grid(row=4, column=1, padx=5, pady=5, sticky='w')

        self.entrar_email = Entry(self.frame_inferior,
                                   bd=2,
                                   width=14,
                                   bg='RosyBrown2',
                                   font=('Times', 12)
                                   )
        self.entrar_email.grid(row=6, column=1, padx=5,pady = 5, sticky='w')

        self.entrar_contraseña = Entry(self.frame_inferior,
                                   bd=2,
                                   width=14,
                                   bg='RosyBrown2',
                                   font=('Times', 12),
                                   show = '*'
                                   )
        self.entrar_contraseña.grid(row=8, column=1, padx=5, pady = 5,sticky='w')

        #BOTON DE ENTRAR

        self.boton1 = Button(self.frame_inferior,
                             text='Registrarse',
                             width=14,
                             font=('Times', 12),
                             bg='tomato',
                             fg='#fff',
                            command = self.verificar

                             )

        self.boton1.grid(row=1, column=5, pady=35, sticky='w')
        self.boton1.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

        mainloop()

    def verificar(self):

        nombre = self.entrar_nombre.get()
        user = self.entrar_usu.get()
        email = self.entrar_email.get()
        contra = self.entrar_contraseña.get()
        edad = self.entrar_edad.get()

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
            print(Data.diccUsers)

            messagebox.showinfo('Registro exitoso', 'Usuario registrado con éxito')
            self.ventana.destroy()
            Principal()

Data().lectura_usuarios()
print(Data.diccUsers)
for i in Data.diccUsers:
    print(Data.diccUsers[i].password)


Principal()