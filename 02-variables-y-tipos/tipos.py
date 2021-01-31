# tipos de datos
# None es un tipo de valor (empty/null ???)
nada = None
# string
cadena = "Desde Santurce a Bilbao, vengo por toda la orilla!"
# integer
entero = 99
# float/decimal ???
flotante = 3.1415
# booleam
booleano = True
# matriz
lista = [10, 20, 30, 100, 200]
# matriz
lista2 = [44, "cuarenta y cuatro", 30, "treinta"]
# matriz de constantes
tupla = ("master", "en", "python")
# diccionario
diccionario = {
    "nombre": "Fernando",
    "apellido": "Abascal",
    "apellido2": "González",
    "nacimiento": 11/10/1957
}
# rango... crea un array de números, sí solo se indica
# un número se crean n valores desde 0 de partida...
# por ejemplo, si ponemos 3 se crear un array 0,1,2,3,
# de 0 a 3
# sí se indica dos números se crea entre estos, ambos incluídos
# del 0,1,2,... ,15,16
rango = range(16)
# bytes
dato_byte = b"Pedro"

# imprime variable
print(nada, type(nada))
print(cadena, type(cadena))
print(entero, type(entero))
print(flotante, type(flotante))
print(booleano, type(booleano))
print(lista, type(lista))
print(lista2, type(lista2))
print(lista[1], type(lista[1]))
print(lista2[1], type(lista2[2]))
print(tupla, type(tupla))
print(tupla[1], type(tupla[1]))
print(diccionario, type(diccionario))
print(rango, type(rango))
print(dato_byte, type(dato_byte))


# mostrar tipo variable
# print(type(nada))
# print(type(cadena))
# print(type(entero))
# print(type(flotante))
# print(type(booleano))
# print(type(lista))
# print(type(lista2))
# print(type(tupla))
# print(type(diccionario))
# print(type(rango))
# print(type(dato_byte))
