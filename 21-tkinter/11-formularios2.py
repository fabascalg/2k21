from tkinter import *


ventana = Tk()
ventana.geometry("800x500")

encabezado = Label(ventana, text="Formularios 2")
encabezado.config(
    padx=15,
    pady=15,
    fg="white",
    bg="green",
    font=("Consolas", 20)
)
encabezado.grid(row=0, column=0, columnspan=6, sticky=W)

# button check

web = IntVar()
movil = IntVar()


def mostrarProfesion():
    texto = ""
    if web.get():
        texto += "desarrollo web"
    if movil.get():
        if web.get():
            texto += " y "
        texto += "desarrollo móvil"
    mostrar.config(
        text=texto,
        bg="green",
        fg="white"
    )


Label(ventana, text="¿A qué te dedicas?").grid(row=1, column=0)
Checkbutton(
    ventana,
    text="Desarrollo web",
    variable=web,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=2, column=0)
Checkbutton(
    ventana,
    text="Desarrollo móvil",
    variable=movil,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=3, column=0)

mostrar = Label(ventana)
mostrar.grid(row=4, column=0)

# botón radio button


def marcar():
    mostrar.config(text=opcion.get())


opcion = StringVar()
opcion.set(None)

Label(ventana, text="¿Cuál es tú género?").grid(row=5, column=0)
Radiobutton(
    ventana,
    text="Masculino",
    value="Masculino",
    variable=opcion,
    command=marcar
).grid(row=6)
Radiobutton(
    ventana,
    text="Femenino",
    value="Femenino",
    variable=opcion,
    command=marcar
).grid(row=7)

mostrar = Label(ventana)
mostrar.grid(row=8, column=0)

# option menu


def seleccionar():
    seleccionado.config(text=opcion.get())


opcion = StringVar()
opcion.set("Opción 2")

Label(ventana, text="Selecciona una opción").grid(row=5, column=1)

select = OptionMenu(ventana, opcion, "Opción 1", "Opción 2", "Opción 3")
select.grid(row=6, column=1)

Button(ventana, text="ver", command=seleccionar).grid(row=7, column=1)

seleccionado = Label(ventana)
seleccionado.grid(row=8, column=1)

ventana.mainloop()
