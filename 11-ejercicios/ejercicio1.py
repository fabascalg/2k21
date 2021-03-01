"""
    Ejercicio 1.
    Hacer un programa que tenga una lista de 8 números 
    enteros y que haga lo siguiente:
    - recorrer la lista y mostrarla
    - hacer función que recorra listas de números y devuelva
    un string
    - ordenarla y mostrarla
    - mostrar su longitud
    - buscar algún elemento (que el usuario pida por teclado)
"""

# la lista de 10 enteros...
numeros = [13, 64, 52, 73, 21, 7, 91, 63]

print("########## EJERCICIO 1 ##########")
print("=================================")

# función para devolver la lista de números como un string


def lista_ver(lista, ordenar=False):
    lista_bis = lista
    if ordenar:
        lista_bis.sort()
    cadena_retorno = ""
    for elemento in lista_bis:
        cadena_retorno = cadena_retorno + str(elemento) + "\n"
    return cadena_retorno


# mostrar lista original
print("Lista original:")
print(numeros)
print("\n")

"""
print("Lista original método each:")
for n in numeros:
    print(n)
print("\n")
"""

print("Lista devuelta como cadena por función:")
print(lista_ver(numeros))
# print("\n")
print("Lista ordenada y devuelta por función ")
print(lista_ver(numeros,True))
# print("\n")
print("Dimensión de la lista: (número de items)")
print(len(numeros))
print("\n")
print("De nuevo la lista original:")
print(numeros)
print("\n")
print("=================================")
n = int(input("Anote el elemento a buscar en la lista de números:"))
indice = numeros.index(n)
73
print(f"El índice del elemento {n} en la lista es: {indice}")
print(f"Extrayendo únicamente el elemento {n} de la lista: {numeros[indice]}")




