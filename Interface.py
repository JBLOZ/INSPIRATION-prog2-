import tkinter as tk

ventana = tk.Tk()
palabra = tk.StringVar(ventana)
entrada = tk.StringVar(ventana)
#dimensiones de la ventana
ventana.geometry('300x600')

ventana.configure(background ='black') #poner el fondo rosita
tk.Wm.wm_title(ventana, 'INSPIRATION') #titulo de la ventana

tk.Button(ventana,
          text = 'hola dale',
          font = ('courier', 14),      #fuente y tamaño
          bg = '#00a8e8',              #color fondo del boton
          fg = 'pink',                 #afecta al color de la fuente
          relief = 'flat',
          command = lambda: print('JORDI ' + entrada.get())
).pack(fill = tk.BOTH,       #codigo para que llene todo lo que pueda tanto a lo ancho como a lo alto
       expand = True,        #para que se ejecute cuando haya un cambio de fuente
)

tk.Label(ventana,
    text = 'tu puta madre',
    fg = 'white',
    bg = 'black',
    justify = 'center',
).pack(fill = tk.BOTH,
       expand = True,
)
tk.Entry(ventana,
         text='tu puta madre',
         fg='white',
         bg='black',
         justify='center',
         textvariable = entrada
).pack(fill=tk.BOTH,
       expand=True,
)




ventana.mainloop()