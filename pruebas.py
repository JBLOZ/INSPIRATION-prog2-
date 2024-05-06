from Users import User
import re
import tkinter
from tkinter import Tk, Label, Entry, Frame, messagebox, mainloop, Button
from PIL import ImageTk, Image

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
                                   font=('Times', 12),
                                   )

        self.entrar_nombre.grid(row=0, column=1, padx=5,pady = 5, sticky = 'w')

        self.entrar_usu = Entry(self.frame_inferior,
                                   bd=2,
                                   width=14,
                                   bg='RosyBrown2',
                                   font=('Times', 12),

                                   )

        self.entrar_usu.grid(row=2, column=1, padx=5,pady = 5, sticky='w')

        self.entrar_edad = Entry(self.frame_inferior,
                                bd=2,
                                width=14,
                                bg='RosyBrown2',
                                font=('Times', 12),
                                )

        self.entrar_edad.grid(row=4, column=1, padx=5, pady=5, sticky='w')

        self.entrar_email = Entry(self.frame_inferior,
                                   bd=2,
                                   width=14,
                                   bg='RosyBrown2',
                                   font=('Times', 12),
                                   )
        self.entrar_email.grid(row=6, column=1, padx=5,pady = 5, sticky='w')

        self.entrar_contraseña = Entry(self.frame_inferior,
                                   bd=2,
                                   width=14,
                                   bg='RosyBrown2',
                                   font=('Times', 12),
                                   show = '*',
                                   )
        self.entrar_contraseña.grid(row=8, column=1, padx=5, pady = 5,sticky='w')

        #BOTON DE ENTRAR

        self.boton1 = Button(self.frame_inferior,
                             text='Registrarse',
                             width=14,
                             font=('Times', 12),
                             bg='tomato',
                             fg='#fff',
                             command = self.verificar)

        self.boton1.grid(row=1, column=5, pady=35, sticky='w')
        self.boton1.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

        mainloop()

    def verificar(self):
        nombre = self.entrar_nombre.get()
        user = self.entrar_usu.get()
        email = self.entrar_email.get()
        contra = self.entrar_contraseña.get()

        if User().check_nombre(nombre) != True:
            messagebox.showinfo('Acceso incorrecto', 'Nombre no válido')

        elif User().check_nickname(user) != True:
            messagebox.showinfo('Acceso incorrecto', 'Nombre de usuario no válido')

        elif User().check_email(user) != True:
            messagebox.showinfo('Acceso incorrecto', 'Email no válido')

        elif User().check_password(contra) != True:
            messagebox.showinfo('Acceso incorrecto', 'La contraseña no es válida')

        else:
            usu = User(self.nombre, self.user, self.email, self.password)
            User.guardar_usuario(usu)
