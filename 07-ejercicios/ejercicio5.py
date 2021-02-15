"""
    Ejercicio 5
    Imprimir números entre dos límites pedidos por teclado.
"""

numero1 = int(input("Número 1 -> "))
numero2 = int(input("Número 2 -> "))

if numero1 < numero2:
    for numero in range(numero1,numero2+1):
        print(f"{numero}")

else:
    print(f"el número 2 -> {numero2} es menor o igual que el número 1 -> {numero1}")
    print("programa cancelado")