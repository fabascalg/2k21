"""

    Trabajar con carpetas

"""

"""
# Crear carpeta
"""
import os, shutil, pathlib
carpeta = "./mi_carpeta"

# crear un directorio, comprobando primero que no existe...
"""
if not os.path.isdir(carpeta):
    os.mkdir(carpeta)
    print(f"\n¡Se ha creado el directorio {carpeta}!\n")
else:
    print(f"\n¡El directorio {carpeta} existe!\n")
"""

# Eliminar carpeta

#os.rmdir(carpeta)
# se produce un error al intentar borrar una carpeta que no existe!
# por tanto se comprueba primero...

carpeta_origen = str(pathlib.Path().absolute()) + r"\mi_carpeta"
carpeta_copiada = str(pathlib.Path().absolute()) + r"\mi_carpeta_C"
carpeta_movida = str(pathlib.Path().absolute()) + r"\nmi_carpeta_M"

"""
if os.path.isdir(carpeta):
    os.rmdir(carpeta)
    print(f"\nSe ha borrado la carpeta {carpeta}\n")
else:
    print(f"\nLa carpeta {carpeta} no existe.\n")


# copiar carpetas

carpeta_origen = str(pathlib.Path().absolute()) + r"\mi_carpeta"
carpeta_copiada = str(pathlib.Path().absolute()) + r"\mi_carpeta_C"
carpeta_movida = str(pathlib.Path().absolute()) + r"\nmi_carpeta_M"

if not os.path.isdir(carpeta_copiada):
    shutil.copytree(carpeta_origen,carpeta_copiada)
    print(f"\nSe copia la carpeta {carpeta_origen} a la carpeta {carpeta_copiada}\n")
else:
    print(f"\nLa carpeta destino \"{carpeta_copiada}\" existe, no se puede copiar...\n")
"""

print(f"\n\nDIR {carpeta_origen}")
caramelos_y_bolitas = len(f"DIR {carpeta_origen}")
cadena = ""
for n in range(0,caramelos_y_bolitas):
    cadena += "="
print(cadena)

contenido = os.listdir(carpeta_origen + r"/../")
contenido2 = os.listdir(carpeta_copiada)


n = 1
for objeto in contenido:
    print(f"{n}: {objeto}")
    n += 1

print(f"\n\nDIR {carpeta_copiada}")
caramelos_y_bolitas = len(f"DIR {carpeta_copiada}")
cadena = ""
for n in range(0,caramelos_y_bolitas):
    cadena += "="
print(cadena)


n = 1
for objeto in contenido2:
    print(f"{n}: {objeto}")
    n += 1

print("\n")
#print(contenido)








