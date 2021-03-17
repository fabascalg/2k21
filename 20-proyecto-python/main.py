"""
    aplicación de consola, q trabaja con una base de datos y login
    al iniciar sin login válido
    - registro
    - login
    al haberse registrado y después acceder a login
    - crear nota
    - mostrar nota
    - eliminar nota
    - salir
"""

from usuarios import acciones

print("""
Acciones disponibles:
    - registro
    - login
""")

tareas = acciones.Acciones()

accion = input("¿Qué quieres hacer? -> ")

if accion == "registro":
    tareas.registro()

if accion == "login":
    tareas.login()




