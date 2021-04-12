from tkinter import *

def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos} veo que eres de {pais}"

ventana = Tk()
ventana.geometry("700x500")

texto = Label(ventana, text=pruebas(pais="Venezuela", nombre="José Vicente", apellidos="Rangel"))
texto.config(
    fg = "white",
    bg = "black",
    padx = 20, 
    pady = 20,
    font = ("Arial",15), 
    cursor = "spider"
)
texto.pack()

texto = Label(ventana, text=pruebas("Carlos Andrés", "Pérez", "Venezuela"))
texto.config(width=50, height=4, bg="#c0c0c0", cursor="circle")
texto.pack(anchor=CENTER)

ventana.mainloop()