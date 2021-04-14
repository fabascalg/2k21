"""
Crear un programa que tenga:
    (hecho) ventana
    (hecho) tamaño fijo
    (hecho) no redimensionable
    (hecho) un menu (inicio, añadir, información, salir)
    (hecho) opcion salir
    (hecho) diferentes pantallas
    (hecho) formulario de añadir productos
    (hecho) guardar datos temporalmente
    (hecho) mostrar datos listados en la pantalla home
    (hecho) opcion de salir
"""

from tkinter import *
from tkinter import ttk

# definir ventana y propiedades
ventana = Tk()
# ventana.geometry("400x400")
ventana.minsize(400, 300)
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
    products_box.grid(row=2)

    # listar productos
    """
    for product in products:
        if len(product) == 3:
            product.append("added")
            Label(products_box, text=product[0]).grid()
            Label(products_box, text=product[1]).grid()
            Label(products_box, text=product[2]).grid()
            Label(products_box, text="--------------------").grid()
    """
    for product in products:
        if len(product) == 3:
            product.append("added")
            products_box.insert("", 0, text=product[0], values=(product[1]))

    # home_label.grid_remove()
    # add_label.grid_remove()
    add_frame.grid_remove()
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
    products_box.grid_remove()
    # add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    # campos del formulario
    add_frame.grid(row=1)
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
    products_box.grid_remove()
    add_label.grid_remove()
    add_frame.grid_remove()
    # info_label.grid_remove()
    # data_label.grid_remove()
    return True


def add_products():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get("1.0", "end-1c")
    ])
    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0", END)
    home()


# variables importantes
products = []
name_data = StringVar()
price_data = StringVar()

# definir pantalla home
home_label = Label(ventana, text="Inicio")
#products_box = Frame(ventana, width="250")

# Label(products_box).grid(row=0)
Label(ventana).grid(row=1)
products_box = ttk.Treeview(height=6, columns=2)
products_box.grid(row=1, column=0, columnspan=2)
products_box.heading("#0", text="Producto", anchor=W)
products_box.heading("#1", text="Precio", anchor=W)


# definir pantalla add
add_label = Label(ventana, text="Añadir")

# campos add

add_frame = Frame(ventana)

add_name_label = Label(add_frame, text="Nombre:")
add_name_entry = Entry(add_frame, textvariable=name_data)

add_price_label = Label(add_frame, text="Precio:")
add_price_entry = Entry(add_frame, textvariable=price_data)

add_description_label = Label(add_frame, text="Descripción: ")
add_description_entry = Text(add_frame)

add_separator = Label(add_frame, text="")

boton = Button(add_frame, text="Guardar", command=add_products)

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
