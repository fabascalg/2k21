# diccionario

contactos = [
    {
        "nombre": "Pedro",
        "email": "pedro@correo.com"
    },
    {
        "nombre": "María",
        "email": "maria@correo.com"

    },
    {
        "nombre": "Andrés",
        "email": "andres@correo.com"

    }
]

"""
persona = {
    "nombre": "Víctor",
    "apellido": "Robles",
    "web": "victorrobles.es"
}

print(persona)

print(persona["web"])
"""

print("\nLista de contactos")
print("==================================")
for contacto in contactos:
    print(f"Nombre: {contacto['nombre']}")
    print(f"Correo: {contacto['email']}")
    print("----------------------------------")

print("\n")