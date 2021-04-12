"""
    CALCULADORA:
    - Dos campos de texto
    - 4 botones para las operaciones
    - Mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox as MessageBox


class Calculadora:

    def __init__(self, alertas):
        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.resultado = StringVar()
        self.alertas = MessageBox

    def cfloat(self, numero):
        try:
            result = float(numero)
        except:
            result = 0
            self.alertas.showerror("Error", "Introduce bien el número")
        return result

    def sumar(self):
        self.resultado.set(self.cfloat(self.numero1.get()) +
                           self.cfloat(self.numero2.get()))
        self.mostrarResultado()

    def restar(self):
        self.resultado.set(self.cfloat(self.numero1.get()) -
                           self.cfloat(self.numero2.get()))
        self.mostrarResultado()

    def multiplicar(self):
        self.resultado.set(self.cfloat(self.numero1.get())
                           * self.cfloat(self.numero2.get()))
        self.mostrarResultado()

    def dividir(self):
        self.resultado.set(self.cfloat(self.numero1.get()) /
                           self.cfloat(self.numero2.get()))
        self.mostrarResultado()

    def mostrarResultado(self):
        self.alertas.showinfo(
            "Resultado", f"El resultado de la operación es: {self.resultado.get()}")
        self.numero1.set("")
        self.numero2.set("")


ventana = Tk()
ventana.geometry("400x400")
ventana.config(bd=25)
ventana.title("Ejercicio completo de Tkinter | Víctor Robles")

calculadora = Calculadora(MessageBox)

marco = Frame(ventana, width=350, height=200)
marco.config(
    bd=5,
    relief=SOLID
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)


Label(marco, text=" Primer número: ").pack()
Entry(marco, textvariable=calculadora.numero1, justify="center").pack()
#Label(marco, text="").pack()
Label(marco, text="Segundo número: ").pack()
Entry(marco, textvariable=calculadora.numero2, justify="center").pack()
Label(marco, text="").pack()
Button(marco, text="Sumar", command=calculadora.sumar).pack(
    side="left", fill=X, expand=YES)
Button(marco, text="Restar", command=calculadora.restar).pack(
    side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar", command=calculadora.multiplicar).pack(
    side="left", fill=X, expand=YES)
Button(marco, text="Dividir", command=calculadora.dividir).pack(
    side="left", fill=X, expand=YES)


ventana.mainloop()
