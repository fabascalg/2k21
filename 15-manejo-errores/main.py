# la lista de 10 enteros...
"""

    MANEJO DE ERRORES

"""

print("\n************** MANEJO DE ERRORES *****************\n")

"""
# ejercicio 1

numeros = [13, 64, 52, 73, 21, 7, 91, 63]
for n in numeros:
    print(n)
print("\n")
# serlock carga el número a buscar...
serlock = int(input("Buscar un número de la lista ->"))
# comprobar determina si hemos escrito un número entero
comprobar = isinstance(serlock, int)
# mientras no sea un número o no sea menor o igual a 0 entrar otro número
while not comprobar or serlock <= 0:
    serlock = int(input("Buscar un número de la lista ->"))
else:
    print(f">>>> BUSCANDO NÚMERO: {serlock}")

try:
    # holmes carga el número de índice en caso de existir el número buscado
    holmes = numeros.index(serlock)
    print(f"!!!! ÉXITO, EL ÍNDICE DEL NÚMERO ENCONTRADO ES {holmes}\n* * * {holmes+1} en la lista de números * * *\n")
except:
    print(f"# # # # # # # # # # # # EL NÚMERO NO EXISTE EN LA LISTA.\n* * * FIN DE PROGRAMA* * *\n")

# ejercicio 2

try:
    numero = input("Número para elevarlo al cuadrado -> ")
    numero = int(numero)
    print("El cuadrado es -> ", str(numero*numero))

#except TypeError:
#    print("Se debe convertir la cadena de entrada a entero...")

#except ValueError:
#    print("\nSe debe anotar un entero...\n")

except Exception as e:
    print("Ha ocurrido un error -> ", type(e).__name__)

print("\n")
"""

# ejercicio 3

try:
    nombre = input("Nombre -> ")
    edad = int(input("Edad ->"))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no está completo")
    else:
        print(f"\nBienvenido al Master de Python {nombre}")
        print(f"Veo que tienes {edad} años.")
#except ValueError:
#    print("Introduce los datos correctamente!")
except Exception as e:
    print("Existe un error: ", e)

print("\n")