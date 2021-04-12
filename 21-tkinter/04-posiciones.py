from tkinter import *

ventana = Tk()
# ventana.geometry("700x500")

texto = Label(ventana, text="Bienvenidos a mi programa")
texto.config(
    fg="white",
    bg="black",
    padx=20,
    pady=20,
    font=("Arial", 15),
    cursor="spider"
)
texto.pack()

texto = Label(ventana, text="Mi nombre es Victor Robles")
texto.config(width=50, height=4, bg="#c0c0c0", cursor="circle")
texto.pack(side=TOP, fill=X, expand=YES)

texto = Label(ventana, text="Tercer texto creado")
texto.config(width=50, height=4, bg="yellow", cursor="heart")
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text="4º texto añadido en código")
texto.config(width=50, height=4, bg="orange", cursor="pirate")
texto.pack(side=LEFT, fill=X, expand=YES)

ventana.mainloop()
