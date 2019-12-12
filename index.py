from tkinter import ttk
from tkinter import *

import sqlite3

class Product:

    def __init__(self,window):
        self.wind = window
        self.wind.title('Producto')

        frame = LabelFrame(self.wind, text = 'Registra un nuevo producto')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)

        Label(frame, text = "Precio: ").grid(row = 2, column = 0)
        self.price = Entry(frame)
        self.price.grid(row = 2, column = 1)

        ttk.Button(frame, text = 'Guardar').grid(row = 3, columnspan = 3, sticky = W + E)



if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()
