from tkinter import *
ventana = Tk()
ventana.geometry("700x700")
ventana.config(
    bd=50,
    # bg="#cccccc"
)


def getDato():
    resultado.set(dato.get())


dato = StringVar()
resultado = StringVar()
Label(ventana, text="Mete un texto: ").pack(anchor=NW)
Entry(ventana, textvariable=dato).pack(anchor=NW)
Label(ventana, text="Dato recogido: ").pack(anchor=NW)
Label(ventana, textvariable=resultado).pack(ancho=NW)
Button(ventana, text="cargar dato", command=getDato).pack(ancho=NW)

ventana.mainloop()
