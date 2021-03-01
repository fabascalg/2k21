"""
    módulo de funciones o librería
"""

def HolaMundo(nombre = "jefe"):
    return f"Hola que tal estás, {nombre}"

def calculadora(numero1, numero2, basicas = False):

    print("\n########## CALCULADORA ###########")
    print("==================================")

    print(f"\t{numero1} + {numero2} = {numero1+numero2}")
    print(f"\t{numero1} - {numero2} = {numero1-numero2}")
    if basicas:
        print(f"\t{numero1} x {numero2} = {numero1*numero2}")
        print(f"\t{numero1} / {numero2} = {int(numero1/numero2)}")    
    print("==================================\n")
