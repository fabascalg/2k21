"""
    Ejercicio 3. 
    Cuadrado de los primeros 60 números naturales.
    Con For y con While.


numero = 0

for numero in range(1,61):
    print(f"{numero*numero}")
"""
numero = 0

while numero < 60:
    numero += 1
    print(f"{numero*numero}", end=", ")


