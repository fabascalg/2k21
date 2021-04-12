from tkinter import *
ventana = Tk()
ventana.geometry("700x400")
ventana.title("Formularios en TKinter | Víctor Robles")

# texto encabezado

encabezado = Label(ventana, text="Formularios con TKinter - Víctor Robles")
encabezado.config(
    fg="white",
    bg="darkgrey",
    font=("Open Sans", 18),
    padx=20,
    pady=20
)
#encabezado.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
encabezado.grid(row=0, column=0, columnspan=8, sticky=W)

# label para el camop

label = Label(ventana, text="Nombre")
label.grid(row=1, column=0, padx=5, pady=5, sticky=E)

# campo de texto "nombre"

campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, padx=5, pady=5, sticky=W)

# label de texto "apellidos"

label = Label(ventana, text="Apellidos")
label.grid(row=2, column=0, padx=5, pady=5, sticky=E)

# campo de texto "apellidos"

campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, padx=5, pady=5, sticky=W)

# campo memo
campo_memo = Text(ventana)
campo_memo.grid(row=3, column=1, sticky=W)
campo_memo.config(
    width=30,
    height=5,
    font=("Arial", 10),
    padx=5,
    pady=5
)

# label como separador vertical, para distanciar el memo del botón

Label(ventana).grid(row=4, column=1)

# botón

boton = Button(ventana, text="Enviar")
boton.grid(row=5, column=1, sticky=W)
boton.config(
    padx=15,
    pady=15, 
    bg="green",
    fg="white"
)


ventana.mainloop()
