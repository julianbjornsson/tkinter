from tkinter import ttk
from tkinter import *

import sqlite3

class Product:

    db_prod = 'database.db'

    def __init__(self,window):
        self.window = window
        self.window.title('Control de Productos')

        frame = LabelFrame(self.window, text = 'Registra un nuevo producto')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)

        Label(frame, text = "Precio: ").grid(row = 2, column = 0)
        self.price = Entry(frame)
        self.price.grid(row = 2, column = 1)

        button = ttk.Button(frame, text = 'Guardar')
        button.grid(row = 3, columnspan = 3, sticky = W + E)

        self.tree = ttk.Treeview(height = 10, columns = 2)
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        self.tree.heading('#0', text = "Nombre", anchor = CENTER)
        self.tree.heading('#1', text = "Precio", anchor = CENTER)



if __name__ == '__main__':
    winsdow = Tk()
    application = Product(winsdow)
    winsdow.mainloop()
