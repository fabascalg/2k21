from tkinter import *

ventana = Tk()
ventana.title("Marcos | Master en Python")
ventana.geometry("500x500")

marco_padre = Frame(ventana)
marco_padre.config(
    bg="lightblue"
)
marco = Frame(marco_padre, width=100, height=100)
marco.config(
    bg="red",
    bd=2,
    relief=SOLID
)
marco.pack(side=LEFT, anchor=SW)
marco.pack_propagate(False)

texto = Label(marco, text="Primer marco")
texto.config(
    bg="red",
    fg="white",
    font=("Arial", 10),
    # height=10,
    # width=10,
    #bd=1,
    #relief=SOLID,
    anchor=CENTER
)

texto.pack(fill=Y, expand=YES)

marco = Frame(marco_padre, width=100, height=100)
marco.config(
    bg="green",
    bd=2,
    relief=SOLID
)
marco.pack(side=RIGHT, anchor=SE)

marco_padre.pack(side=TOP, anchor=N, fill=X, expand=YES)

marco_padre_dos = Frame(ventana)
marco_padre_dos.config(
    bg="#f0A0f0"
)

marco = Frame(marco_padre_dos, width=100, height=100)
marco.config(
    bg="pink",
    bd=2,
    relief=SOLID
)

marco.pack(side=LEFT, anchor=NE)

marco = Frame(marco_padre_dos, width=100, height=100)
marco.config(
    bg="orange",
    bd=2,
    relief=SOLID
)

marco.pack(side=RIGHT, anchor=NW)

marco_padre_dos.pack(side=BOTTOM, anchor=S, fill=X, expand=YES)

ventana.mainloop()
