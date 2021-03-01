"""
    Módulos: son librerias

    En Python hay muchos y también nos permite crear u 
    usar los nuestros o de otras personas o empresas.
"""

# import mimodulo
from mimodulo import *

"""
    mimodulo.calculadora(5,7,True)

    print(mimodulo.HolaMundo("Fernando"))

    print(mimodulo.HolaMundo())
"""

print("\n============= funciones en módulo: mimodulo.py ==========\n")
calculadora(5,7,True)

print(HolaMundo("Fernando"))

print(HolaMundo())

import datetime

print("\n============= funciones en módulo: datetime ==========\n")

print(datetime.date.today())
print("\n")
print(datetime.datetime.now())

print("\n============= funciones en módulo: math ==========\n")

import math

print("Raiz cuadrada de 25 -> ", math.sqrt(25))
print("Número PI -> ", math.pi)
print("Redondear arriba PI -> ", math.ceil(math.pi))
print("Redondear PI ->", round(math.pi,3))
print("Redondear abajo PI -> ", math.floor(math.pi))

print("\n============= funciones en módulo: random ==========\n")

import random

print("Número aleatorio entre 3 y 300 -> ", random.randint(3,300))


print("\n============= ***************************** ==========\n")



#  