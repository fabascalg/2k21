"""

# FOR
for variables in elemento interable (lista, rango, etc)
    bloque de instrucciones


"""

print("################ BUCLE ################")
print("################  FOR  ################")

contador = 0
acumulador = 0

for contador in range(0,10):
    print(f"Voy por {contador}")
    acumulador += contador

print(f"Acumulador: {acumulador}")
print("Nota: en range(x,y), cuando el rango llega a y sale sin actuar...")

print("################ BUCLES ################")
print("################ FOR 2  ################")

contador = 0
for contador in range(0,10):
    print(f"{contador}",end=", ")
print(contador+1)