"""
    Calculadora.
    Entra dos enteros y calcula las cuatro operaciones básicas.
"""

numero1 = int(input("número 1 -> "))
numero2 = int(input("número 2 -> "))

print("###### CALCULADORA ######")
print(f"{numero1} + {numero2} = {numero1+numero2}")
print(f"{numero1} - {numero2} = {numero1-numero2}")
print(f"{numero1} x {numero2} = {numero1*numero2}")
print(f"{numero1} / {numero2} = {int(numero1/numero2)}")
