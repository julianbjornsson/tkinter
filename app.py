import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter.scrolledtext import *
from tkinter import messagebox

#Estructura y layout
window = Tk()
window.title("Registro de Pacientes")
window.geometry("700x650")

style = ttk.Style(window)
style.configure("TNotebook", tabposition = 'n')

#Tab layout
tab_control = ttk.Notebook(window, style = 'TNotebook')

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)

#Añadir tabs
tab_control.add(tab1,text = f'{"Inicio":^20s}')
tab_control.add(tab2,text = f'{"Listar":^20s}')
tab_control.add(tab3,text = f'{"Busqueda":^20s}')
tab_control.add(tab4,text = f'{"Exportar":^20s}')
tab_control.add(tab5,text = "Acerca de...")

tab_control.pack(expand=1, fill="both")

label1 = Label(tab1, text = 'Ingreso de datos de pacientes', pady = 5, padx = 5)
label1.grid(column = 0, row = 0)

label2 = Label(tab2, text = 'Listado de pacientes', pady = 5, padx = 5)
label2.grid(column = 0, row = 0)

label3 = Label(tab3, text = 'Busqueda de pacientes', pady = 5, padx = 5)
label3.grid(column = 0, row = 0)

label4 = Label(tab4, text = 'Exportar a archivo', pady = 5, padx = 5)
label4.grid(column = 0, row = 0)

label5 = Label(tab5, text = 'Acerca de...', pady = 5, padx = 5)
label5.grid(column = 0, row = 0)

#Inicio
l1 = Label(tab1, text = "Nombre(s):", padx = 5, pady = 5)
l1.grid(column = 0, row = 1)
fname_raw_entry = StringVar()
inp_name = Entry(tab1, textvariable=fname_raw_entry, width = 50)
inp_name.grid(column = 1, row = 1)

l2 = Label(tab1, text = "Apellido(s):", padx = 5, pady = 5)
l2.grid(column = 0, row = 2)
lname_raw_entry = StringVar()
inp_lname = Entry(tab1, textvariable=lname_raw_entry, width = 50)
inp_lname.grid(column = 1, row = 2)

l3 = Label(tab1, text = "Correo electronico:", padx = 5, pady = 5)
l3.grid(column = 0, row = 3)
mail_raw_entry = StringVar()
inp_mail = Entry(tab1, textvariable=mail_raw_entry, width = 50)
inp_mail.grid(column = 1, row = 3)

l4 = Label(tab1, text = "Edad:", padx = 5, pady = 5)
l4.grid(column = 0, row = 4)
age_raw_entry = StringVar()
inp_age = Entry(tab1, textvariable=age_raw_entry, width = 50)
inp_age.grid(column = 1, row = 4)

l5 = Label(tab1, text = "Fecha de Nacimiento:", padx = 5, pady = 5)
l5.grid(column = 0, row = 5)
dob_raw_entry = StringVar()
inp_dob = DateEntry(tab1,width = 30, textvariable=dob_raw_entry, background = 'grey', foreground='white', borderwidth = 2, year = 2019 )
inp_dob.grid(column = 1, row = 5)

l6 = Label(tab1, text = "Direccion:", padx = 5, pady = 5)
l6.grid(column = 0, row = 6)
dire_raw_entry = StringVar()
inp_dire = Entry(tab1, textvariable=dire_raw_entry, width = 50)
inp_dire.grid(column = 1, row = 6)

l7 = Label(tab1, text = "Telefono de contacto:", padx = 5, pady = 5)
l7.grid(column = 0, row = 7)
fono_raw_entry = StringVar()
inp_fono = Entry(tab1, textvariable=fono_raw_entry, width = 50)
inp_fono.grid(column = 1, row = 7)

boton1 = Button(tab1, text = 'Añadir', width = 20, bg = '#B0AFAE', fg = '#FFFFFF' )
boton1.grid(row = 8, column = 0, pady = 45, padx = 45)

boton2 = Button(tab1, text = 'Limpiar Campos', width = 20, bg = '#B0AFAE', fg = '#FFFFFF' )
boton2.grid(row = 8, column = 1, pady = 25, padx = 25)

tab1_display = ScrolledText(tab1, height = 10)
tab1_display.grid(row = 9, pady = 5, padx = 5, columnspan = 2)

boton3 = Button(tab1, text = 'Limpiar Resultados', width = 20, bg = '#B0AFAE', fg = '#FFFFFF' )
boton3.grid(row = 10, column = 1, pady = 25, padx = 25)

#Listado

boton_ver = Button(tab2, text = 'Listar pacientes', width = 20, bg = '#B0AFAE', fg = '#FFFFFF', command = ver_todo)
boton_ver.grid(row = 1, column = 0, padx = 10, pady = 10)
#Treeview
tree = ttk.Treeview(tab2, column = ("c1", "c2", "c3", "c4", "c5", "c6", "c7"), show='headings')
tree.heading("#1", text = "Nombre")
tree.heading("#2", text = "Apellido")
tree.heading("#3", text = "eMail")
tree.heading("#4", text = "Edad")
tree.heading("#5", text = "Fecha de nacimiento")
tree.heading("#6", text = "Direccion")
tree.heading("#7", text = "Telefono")
tree.grid(column = 0, row = 10, columnspan = 3, padx = 5, pady = 5)

#Busqueda

#Exportar

#Acerca de



window.mainloop()
