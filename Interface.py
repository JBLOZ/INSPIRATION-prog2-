import tkinter as tk

ventana = tk.Tk()

#dimensiones de la ventana
ventana.geometry('300x600')

ventana.configure(background ='black') #poner el fondo rosita
tk.Wm.wm_title(ventana, 'INSPIRATION') #titulo de la ventana

tk.Button(ventana,
          text = 'hola dale',
          font = ('courier', 14),      #fuente y tamaño
          bg = '#00a8e8',              #color fondo del boton
          fg = 'pink'                 #afecta al color de la fuente
          ).pack(fill = tk.BOTH,       #codigo para que llene todo lo que pueda tanto a lo ancho como a lo alto
                expand = True          #para que se ejecute cuando haya un cambio de fuente
                )

tk.label 


ventana.mainloop()