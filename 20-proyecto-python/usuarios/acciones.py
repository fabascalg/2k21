import usuarios.usuario as modelo


class Acciones:

    def registro(self):
        print("Ok! Vamos a registrarte en el sistema...")
        nombre = input("Introduce tu nombre -> ")
        apellidos = input("Introduce tus apellidos -> ")
        email = input("Introduce tu correo -> ")
        password = input("Introduce tu contraseña -> ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registro()

        if registro[0] >= 1:
            print(
                f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nNo te has registrado correctamente.")

    def login(self):
        print("Vale! Identificate en el sistema...")
        try:
            email = input("Introduce tu correo -> ")
            password = input("Introduce tu contraseña -> ")

            persona = modelo.Usuario('', '', email, password)
            entrada = persona.identificar()

            for e in entrada:
                print(e)

            print("fin")

            if email == entrada[3]:
                print(f"\nBienvenido {entrada[1]}")
                self.proximasacciones(entrada)
        except Exception as e:
            #print("\n===== error =====")
            # print(type(e))
            # print(type(e).__name__)
            print("\nLogin incorrecto!! Intentalo más tarde\n")

    def proximasacciones(self, entrada):
        print("""
        Acciones disponibles:
        - Crear nota (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar nota (eliminar)
        . Salir (salir)
        """)

        accion = input("Qué quieres hacer? => ")

        if accion == "crear":
            print("vamor a crear")
        elif accion == "mostrar":
            print("vamor a mostrar")
        elif accion == "eliminar":
            print("vamor a eliminar")
        elif accion == "salir":
            exit()

        return None
