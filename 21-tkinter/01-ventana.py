from tkinter import *
import os.path


class Programa:

    def __init__(self):
        self.title = "MI SUPER VENTANA EN ¡PYTHON!"
        self.icon = "./imagenes/helicopter_whirlybird_icon_183201.ico"
        self.icon = "./imagenes/helicopter_whirlybird_icon_183201.ico"
        self.icon_alt = "./21-tkinter/imagenes/helicopter_whirlybird_icon_183201.ico"
        self.size = "770x470"
        self.resizable = False

    def cargar(self):

        # crear ventana
        ventana = Tk()

        self.ventana = ventana

        # tamaño ventana
        ventana.geometry(self.size)

        # redimesionar 0 horizontal 0 vertical o combinaciones con 1
        if self.resizable:
            ventana.resizable(1, 1)
        else:
            ventana.resizable(0, 0)

        # comprobando la ruta de la imagen a cargar
        ruta_icono = self.icon

        # comprobar si la ruta y archivo existe...
        if not os.path.isfile(ruta_icono):
            ruta_icono = self.icon_alt

        # mostrar texto en la ventana
        texto = Label(ventana, text=ruta_icono)
        texto.pack()

        # favicon de ventana (.ico)
        ventana.iconbitmap(ruta_icono)

        # ventana title
        ventana.title(self.title)

    def addTexto(self, dato = "Hoja desde un método"):
        texto = Label(self.ventana, text=dato)
        texto.pack()

    def mostrar(self):
        self.ventana.mainloop()



programa = Programa()
programa.cargar()
programa.addTexto()
programa.addTexto("Otra línea de texto")
programa.addTexto("Más cosucas, creo que van tres...")
programa.mostrar()
