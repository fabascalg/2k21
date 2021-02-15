"""
    Ejercicio 7
    Imprimir impares entre dos números introducidos por teclado.
"""

numero1 = int(input("número \"desde\" -> "))
numero2 = int(input("número \"hasta\" -> "))

if numero1 >= numero2:
    print(f"error, el número desde -> {numero1} es mayor o igual al número hasta -> {numero2}")
else:
    for contador in range(numero1, numero2+1):
        if contador%2 != 0:
            print(f"{contador}")
        
