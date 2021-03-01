def imprimeLista(lista, nombre):
    n = 1
    tipo = str(type(lista))
    cadena_devuelta = nombre.upper() + " - " + tipo + "\n"
    for elemento in lista:
        cadena_devuelta += f"{n}: {elemento}\n"
        n += 1
    return cadena_devuelta


print("################## LISTAS ##################")

peliculas = ["Batman", "Spiderman", "El señor de los anillos", ]

"""
cantantes = ["2pac", "Drake", "Jennifer López"]
numeros = (2, 3, 4, 5, 6, 7, 8, 9)
years = list(range(2020, 2050))
variada = ["Fernando", 30, 4.4, True, "Texto"]
print("\n")
print(peliculas)
print("\n")
print(cantantes)
print("\n")

print(imprimeLista(peliculas, "Películas"))
print("\n")

print(imprimeLista(cantantes, "Cantantes"))
print("\n")

print(imprimeLista(numeros, "Números"))
print("\n")

print(imprimeLista(years, "Years"))
print("\n")

print(imprimeLista(variada, "Variada"))
print("\n")


print(type(peliculas))
print(type(cantantes))
print(type(years))
print(type(numeros))
print(type(variada))
print("\n")


years.append(2050)
print(imprimeLista(years, "Years"))
print("\n")

years.insert(3,1957)
print(imprimeLista(years, "Years"))
print("\n")

years.reverse()
print(imprimeLista(years, "Years"))
print("\n")

for n in range(5,10):
    years.remove(years[n])

years.reverse()
print(imprimeLista(years, "Years"))
print("\n")

# comprobación de tipos para depurar error al ordenar!
for elemento in years:
    print(f"{elemento} -> " + str(type(elemento)))
print("\n")


years.sort()
print(imprimeLista(years, "Years"))
print("\n")

print("[3] ->",years[3])
print("[-2] ->",years[-2])
# [0:7] empieza en 0 y termina en el menor a 7!!!
print("[0:7] ->",years[0:7])
print("[10:] ->",years[10:])
print("[:10] ->",years[:10])

print("\n")
peliculas[1] = "Gran Torino"
print(imprimeLista(peliculas, "Películas"))
print("\n")


pelicula = ""
while pelicula != "parar":
    pelicula = input("Introduce la nueva película (parar para terminar) ->")
    if pelicula != "parar":
        peliculas.append(pelicula)

print(imprimeLista(peliculas, "Películas"))
print("\n")
"""

# listas multidensionales

contactos = [
    [
        'Antonio',
        'antonio@correo.com'
    ],
    [
        'Luis',
        'luis@correo.com'
    ],
    [
        'Salvador',
        'salvador@correo.com'
    ]
]

print(contactos)
print("\n")
print(contactos[1])
print("\n")
print(contactos[2][0])
print("\n")

print("\n********* listado de contactos ************\n")
for contacto in contactos:
    for campo in contacto:
        if contacto.index(campo) == 0:
            print("Nombre: ", campo)
        else:
            print("Correo: ",campo,"\n")
print("===========================================")