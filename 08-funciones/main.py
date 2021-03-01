"""

    main.py dentro de \08-funciones

    empezar a usar funciones



print("########## EJEMPLO 1 ##########")

# se deben definir antes de ser invocadas!

def muestraNombre():
    print("Víctor")
    print("Manuel")
    print("Carolina")

muestraNombre()



# uso de parámetros

print("########## EJEMPLO 2 ##########")

def muestraNombre(nombre):
    print(f"{nombre}")


muestraNombre("Marbella")
muestraNombre("Fernando")
muestraNombre("Fabiana")
muestraNombre("Sebastián")



print("########## EJEMPLO 2-1 ##########")

def muestraNombre(nombre,edad):
    print(f"el nombre es {nombre}")
    if edad < 18:
        print(f"tienes {edad}, eres menor de edad")
    else:
        print(f"tienes {edad}, eres mayor de edad")

nombre = input("anota tu hombre")
edad = int(input("anota tu edad -> "))
muestraNombre(nombre, edad)

"""

"""
print("########## EJEMPLO 3 ##########")

# función con parámetros, tabla de multiplicar

numero = int(input("Tabla del número -> "))

def TablaDeNumero(numero):
    print(f"##### La tabla del {numero} #####")
    for contador in range(0,11):
        print(f"{numero} x {contador} = {numero*contador}")
    print("***** fin del 3 *****")

TablaDeNumero(numero)

"""
"""

print("########## EJEMPLO 4 ##########")
print("  de parámetros opcionales en funciones...")
print("\n")

def mostrarDatos(nombre, edad = None):
    print(f"Nombre: {nombre}")
    if edad != None:
        print(f"Edad: {edad}")
    else:
        print("Sin edad???")    

mostrarDatos("Fernando")
mostrarDatos("Fernando",34)
mostrarDatos("Sebastián",23)

"""

"""

print("########## EJEMPLO 5 ##########")
print(" devolver un valor desde una función...")

def saludo(nombre):
    cadena = f"Hola, saludos {nombre}"
    return cadena

print(saludo("Andrés"))

print("##### fin del ejemplo 5 #####")



print("########## EJEMPLO 6 ##########")
print(" devolver un conjunto de cálculos desde una función que usa varios parámetros")

numero1 = 0
numero2 = 0

def calculadora(numero1,numero2,basicas=False):
    cadena = f"Suma            {numero1}+{numero2}={numero1+numero2}"
    cadena += "\n"
    cadena += f"Resta           {numero1}-{numero2}={numero1-numero2}"
    cadena += "\n"
    if basicas == False:
        cadena += f"Multiplicación  {numero1}x{numero2}={numero1*numero2}"
        cadena += "\n"
        cadena += f"División        {numero1}/{numero2}={numero1/numero2}"
        cadena += "\n"
    return cadena

print(calculadora(5,7,False))



print("########## EJEMPLO 7 ##########")
print(" Invocar a una función desde otra")

def getNombre(nombre):
    texto = f"El nombres es " + nombre
    return texto

def getApellidos(apellidos):
    texto = f"Los apellidos son " + apellidos
    return texto

def getNombreCompleto(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(getNombreCompleto("Fernando","Abascal González"))

"""

print("########## EJEMPLO 8 ##########")
print(" función lambda")

# funciones lambda, anónimas de una sola línea

devuelve_entero = lambda numero: f"El entero es {numero}"

print(devuelve_entero(11101957))










