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
 
print("################# EJEMPLO 4 #################")

dia = int(input("Introduce el número de día de la semana: "))

if dia == 1:
    print("el lunes")
elif dia ==2:
    print("es martes")
elif dia ==3:
    print("es miércoles")
elif dia == 4:
    print("es jueves")
elif dia == 5:
    print("es viernes")
elif dia == 6:
    print("es sábado")
elif dia == 7:
    print("es domingo")
else:
    print(f"es un error, no existe el {dia} como número de día de la semana...")

"""

print("################# EJEMPLO 5 #################")

edad_desde = 18.0
edad_maxima = 66.5

edad_real = float(input("introduce tu edad para comprobar si estas en edad de trabajar: "))

if edad_real >= edad_desde and edad_real <= edad_maxima:
    print("estas en edad de trabajar")
else:
    print("no estas en edad de trabajar")
    if edad_real < edad_desde:
        print(f"demasiado joven, tienes solo {edad_real} años")
    else:
        print(f"demasiado mayor, has alcanzado los {edad_real} años")

