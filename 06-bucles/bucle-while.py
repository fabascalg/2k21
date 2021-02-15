print("################ BUCLE ################")
print("################ WHILE ################")
contador = 1
while contador <= 100:
    print(f"Estoy en el número: {contador}")
    contador += 1

print(f"--- salida del primer while....")

contador = 1
muestrame = str(0)
while contador <= 100:
    muestrame = muestrame + ", " + str(contador)
    contador += 1
print(muestrame)

print(f"--- salida del segundo while....")

numero_usuario = int(input("imprimir la tabla del? => "))

contador = 1
while contador <= 10:
    print(f"{numero_usuario} x {contador} = {numero_usuario * contador}")
    contador += 1
else:
    print(f"Tabla del {numero_usuario} terminada.")

print(f"--- salida del tercer while....")