"""
    input para entrada...
    if para decidir salida ...

print("################# EJEMPLO 1 #################")

color = input("Acierta el color que estoy pensando: ")

if color == "rojo":
    print("Bien, el color es rojo")
else:
    print("No has acertado...")


print("################# EJEMPLO 2 #################")

# year = 2020
year = int(input("anote el año a comparar... : "))

if year >= 2021:
    print("año igual o mayor a 2021!")
else:
    print("año menor a 2021!")



print("################# EJEMPLO 3 #################")

nombre = "Victor Robles (el profe)"
ciudad = "Barcelona"
continente = "Europa"
edad = 17
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")

    if continente == "Europa":
        print(f"{nombre} es europeo y de {ciudad}")
    else:
        print(f"{nombre} no es europeo")
else:
    print(f"{nombre} no es mayor de edad, tiene {str(edad)} años")
    # la f antes del string, formatea las variables para la salida!!!! por tanto nos evita usar str(...) para el caso del integer
    print(f"{nombre} no es mayor de edad, tiene {edad} años")
    #print(f"{nombre} no es mayor de edad, tiene " + str(edad) + " años")

 print(f"{nombre} no es mayor de edad, tiene {str(edad)} años")
 
"""

print("################# EJEMPLO 4 #################")
