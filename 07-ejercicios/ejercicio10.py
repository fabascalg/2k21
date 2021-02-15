"""
    Ejercicio 10
    Notas de 15 alumnos y sacar el número de aprobados y suspendidos.
"""

contador = 0
aprobados = 0
nota = 0

for contador in range(1,16):
    nota = int(input(f"nota del alumno número {contador} -> "))
    if nota >= 5:
        aprobados += 1
    
print(f"Han aprobado {aprobados} alumnos.")
print(f"Han suspendido {15-aprobados} alumnos.")



