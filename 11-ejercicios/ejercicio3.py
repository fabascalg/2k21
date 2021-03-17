"""
    poner una cadena vacía contenido en minúsculas y mostrarlo en mayúsculas
"""

#texto = "Desde Santurce a Bilbao, vengo por toda la orilla ..."
texto = ""


if len( texto.strip()) == 0:
    texto="esta cadena está en minúsculas"
    print(f"{texto.upper()}")
else:
    print("La cadena texto no está vacía.")
    print(f"{texto}")

print("\n")

