""" 

    Trabajando con ficheros.

    Librerías necesarias.

"""

from io import open
import pathlib
import math
import pathlib

# Abrir archivo para "añadir información"
# sí se hace una referencia relativa o absoluta correcta
# se creará el archivo en caso de no existir!

archivo = open("nota.txt", "a+")

#pi = math.pi

archivo.write("***** añadido *****\n")

archivo.close()

archivo_lectura = open("nota.txt", "r")

lista = archivo_lectura.readlines()

n = 1

for frase in lista:
    print(f"línea {n}: {frase}")
    n += 1

ruta_original = str(pathlib.Path().absolute()) + r"\nota.txt"
ruta_destino = str(pathlib.Path().absolute()) + r"\nota (1).txt"
ruta_movido = str(pathlib.Path().absolute()) + r"\nota (2).txt"

import shutil

shutil.copyfile(ruta_original, ruta_destino)

shutil.move(ruta_destino, ruta_movido)

shutil.copyfile(ruta_movido, ruta_destino)

import os

os.remove(ruta_movido)

if os.path.isfile(ruta_destino):
    print(f"El fichero {ruta_destino} existe.")
else:
    print(f"El fichero {ruta_destino} no existe.")

if os.path.isfile(ruta_movido):
    print(f"El fichero {ruta_movido} existe.")
else:
    print(f"El fichero {ruta_movido} no existe.")

