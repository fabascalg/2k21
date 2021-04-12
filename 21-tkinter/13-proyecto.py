"""
Crear un programa que tenga:
    (hecho) ventana
    (hecho) tamaño fijo
    (hecho) no redimensionable
    (hecho) un menu (inicio, añadir, información, salir)
    (hecho) opcion salir
    (hecho) diferentes pantallas
    - formulario de añadir productos
    - guardar datos temporalmente
    - mostrar datos listados en la pantalla home
    - opcion de salir
"""

from tkinter import *

# definir ventana y propiedades
ventana = Tk()
ventana.geometry("400x400")
ventana.title("Proyecto Tkinter - Master en Python")
ventana.resizable(0, 0)

# pantallas


def home():
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=160,
        pady=20
    )
    home_label.grid(row=0, column=0)
    # home_label.grid_remove()
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    return True


def add():
    # encabezado
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=140,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=10)
    home_label.grid_remove()
    # add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    # campos del formulario
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=NW)
    add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    add_description_entry.config(
        width=30,
        height=5,
        font=("Consola", 12),
        padx=15,
        pady=15
    )

    add_separator.grid(row=4)

    boton.grid(row=5, column=1, padx=5, pady=5, sticky=NW)
    boton.config(
        padx=15,
        pady=5,
        bg="green",
        fg="white"
    )

    return True


def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=110,
        pady=20
    )
    info_label.grid(row=0, column=0)
    data_label.grid(row=1, column=0)
    home_label.grid_remove()
    add_label.grid_remove()
    # info_label.grid_remove()
    # data_label.grid_remove()
    return True


# variables importantes
name_data = StringVar()
price_data = StringVar()

# definir pantalla home
home_label = Label(ventana, text="Inicio")

# definir pantalla add
add_label = Label(ventana, text="Añadir")

# campos add
add_name_label = Label(ventana, text="Nombre:")
add_name_entry = Entry(ventana, textvariable=name_data)

add_price_label = Label(ventana, text="Precio:")
add_price_entry = Entry(ventana, textvariable=price_data)

add_description_label = Label(ventana, text="Descripción: ")
add_description_entry = Text(ventana)

add_separator = Label(ventana, text="")

boton = Button(ventana, text="Guardar")

# definir pantalla info
info_label = Label(ventana, text="Información")
data_label = Label(
    ventana, text="Creado por Víctor Robles - Curso Python 2021")

# cargar pantalla inicio
home()

# menú definir
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir producto", command=add)
menu_superior.add_command(label="Información", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)

# cargar menú
ventana.config(menu=menu_superior)


# cargar ventana
ventana.mainloop()
