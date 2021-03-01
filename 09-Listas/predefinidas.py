cantantes = ['2pac', 'Drake', 'Bad Bunny', 'Julio Iglesias']
numeros = [1, 2, 5, 8, 3, 4]

print(cantantes)
print(f"ordenar cantantes ...")
cantantes.sort()
print(cantantes)
print("\n")

print(numeros)
print("ordenar números...")
numeros.sort()
print(numeros)
print("\n")

print("cantantes, agregar ...")
cantantes.append("Natos y Waor")
print(cantantes)
print("\n")

print("numeros, agregar ...")
numeros.append(7)
print(numeros)
print("\n")

print("cantantes, insertar en índice 1...")
cantantes.insert(1, "David Bisbal")
print(cantantes)
print("\n")

print("numeros, insertar en índice 1 ...")
numeros.insert(1, 6)
print(numeros)
print("\n")

print("cantantes, eliminar índice 3 ...")
cantantes.pop(3)
print(cantantes)
print("\n")

print("numeros, eliminar índice 3 ...")
numeros.pop(3)
print(numeros)
print("\n")

print("cantantes, remover 2pac ...")
cantantes.remove('2pac')
print(cantantes)
print("\n")

print("numeros, remover el 7 ...")
numeros.remove(7)
print(numeros)
print("\n")

print("cantantes, dar la vuelta a la lista ...")
cantantes.reverse()
print(cantantes)
print("\n")

print("numeros, dar la vuelta a la lista ...")
numeros.reverse()
print(numeros)
print("\n")

print("saber si Bad Bunny esta en la lista de cantantes...")
print("Bad Bunny" in cantantes)
print("\n")

print("saber si el 4 esta en la lista de números ...")
print(4 in numeros)
print("\n")

print("saber si Plácido Domingo esta en la lista de cantantes...")
print("Plácido Domingo" in cantantes)
print("\n")

print("saber si el 11 esta en la lista de números ...")
print(11 in numeros)
print("\n")

print("numeros, agregar un 8 ...")
numeros.append(8)
print(numeros)
print(f"contar los 8 que hay en números -> {numeros.count(8)}")
print(numeros)
print("\n")

print("cantantes, índice de Bad Bunny ...")
# cantantes.reverse()
print(cantantes.index("Bad Bunny"))
print(cantantes[cantantes.index("Bad Bunny")])
print("\n")

print("añadir a cantantes la lista de números ...")
cantantes.extend(numeros)
print(cantantes)
print("\n")


