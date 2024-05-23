import tkinter
from tkinter import *
from Inspiration import Inspiration
from Users import User
'''class MyInspirations:
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

    def megusta(self):

        self.usuario.me_gusta()

    def cambiar_color(self):
        if self.usuario.comprobar_mg() == False:
            self.boton.configure(bg = 'tomato')

        else:
            self.boton = self.boton




MyInspirations('jord')'''
import tkinter as tk
from tkinter import ttk


# Función que se llamará al presionar el botón
def mostrar_contenido():
    # Limpiar el contenido previo en el frame de scroll
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    # Obtener el texto de la entrada
    texto = entrada.get()

    # Crear etiquetas con el texto de entrada
    for i in range(50):  # Crear 50 etiquetas de ejemplo
        ttk.Label(scrollable_frame, text=f"{texto} {i + 1}").pack()

    # Actualizar la región de scroll del canvas
    scrollable_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))


# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Scrollbar en Tkinter")

# Crear el entry para la entrada de texto
entrada = ttk.Entry(root, width=50)
entrada.pack(pady=10)

# Crear el botón que mostrará el contenido
boton = ttk.Button(root, text="Mostrar Contenido", command=mostrar_contenido)
boton.pack(pady=10)

# Crear un frame para contener el canvas y el scrollbar
frame_canvas = tk.Frame(root)
frame_canvas.pack(fill=tk.BOTH, expand=True)

# Crear el canvas
canvas = tk.Canvas(frame_canvas)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Crear el scrollbar vertical y vincularlo al canvas
scrollbar = ttk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

# Crear un frame dentro del canvas para los widgets desplazables
scrollable_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Ajustar la región de scroll cuando cambie el tamaño del frame
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

# Iniciar el loop principal de la aplicación
root.mainloop()
