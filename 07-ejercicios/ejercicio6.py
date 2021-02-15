"""

    Ejercicio 6.
    Mostrar tablas del 1 al 10

"""

contador = 0
contador2 = 0

print("########## TABLAS DEL 1 AL 10 ##########")

for contador in range(1,11):
    print(f"### Tabla del {contador} ###")
    for contador2 in range(11):
        print(f"{contador} x {contador2} = {contador*contador2}")
    print("__________________________________")
print("--- fin ---")


