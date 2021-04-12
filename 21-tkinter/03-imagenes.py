
from tkinter import *

from PIL import Image, ImageTk

ventana = Tk()

ventana.geometry("700x500")

Label(ventana, text="Hola, soy Victor").pack(anchor=W)

#imagen = Image.open('./21-tkinter/imagenes/Lobo-gris.jpg')
imagen = Image.open('./imagenes/Lobo-gris.jpg')
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack()

ventana.mainloop()

