"""
    Ejercicio 2.
    Ir llenando una lista hasta "n" elementos y después mostrarla.
"""
print("\n\n#################### EJERCICIO 2 ###################")
print("  cargar e imprimir lista de 120 items (método for)")
print("====================================================")
lista = []
for n in range(0,120):
    lista.append(f"elemento: {n+1}")
    print(f"Mostrando el nuevo {lista[n]}")
print(lista)
print("\n====================================================")
print(" cargar e imprimir lista de 120 items (método while)")
print("====================================================")
del lista
lista = []
n = 0
while n < 120:
    lista.append(f"2da lista - {n+1}")
    print(lista[n])
    n += 1
print(lista)