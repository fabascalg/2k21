"""
    CALCULADORA:
    - Dos campos de texto
    - 4 botones para las operaciones
    - Mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox as MessageBox


ventana = Tk()
ventana.geometry("400x400")
ventana.config(bd=25)
ventana.title("Ejercicio completo de Tkinter | Víctor Robles")


def cfloat(numero):
    try:
        result = float(numero)
    except:
        result = 0
        MessageBox.showerror("Error", "Introduce bien el número")
    return result


def sumar():
    resultado.set(cfloat(numero1.get()) + cfloat(numero2.get()))
    mostrarResultado()


def restar():
    resultado.set(cfloat(numero1.get()) - cfloat(numero2.get()))
    mostrarResultado()


def multiplicar():
    resultado.set(cfloat(numero1.get()) * cfloat(numero2.get()))
    mostrarResultado()


def dividir():
    resultado.set(cfloat(numero1.get()) / cfloat(numero2.get()))
    mostrarResultado()


def mostrarResultado():
    MessageBox.showinfo(
        "Resultado", f"El resultado de la operación es: {resultado.get()}")
    numero1.set("")
    numero2.set("")


marco = Frame(ventana, width=350, height=200)
marco.config(
    bd=5,
    relief=SOLID
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

Label(marco, text=" Primer número: ").pack()
Entry(marco, textvariable=numero1, justify="center").pack()
#Label(marco, text="").pack()
Label(marco, text="Segundo número: ").pack()
Entry(marco, textvariable=numero2, justify="center").pack()
Label(marco, text="").pack()
Button(marco, text="Sumar", command=sumar).pack(
    side="left", fill=X, expand=YES)
Button(marco, text="Restar", command=restar).pack(
    side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar", command=multiplicar).pack(
    side="left", fill=X, expand=YES)
Button(marco, text="Dividir", command=dividir).pack(
    side="left", fill=X, expand=YES)


ventana.mainloop()
