import notas.nota as modelo


class Acciones:

    def crear(self, usuario):

        print(f"\nOk {usuario[1]}!! Vamos a crear una nota")
        titulo = input("Introduce el título de tu nota => ")
        descripcion = input("Mete el contenido de tu nota => ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto has guardado la nota: {nota.titulo}")
        else:
            print(f"\nNo se ha guardado la nota, lo siento {usuario.nombre}")

    def mostrar(self, usuario):
        print(f"Vale {usuario[1]}!! Aquí tienes tus notas: ")

        nota = modelo.Nota(usuario[0])

        notas = nota.listar()

        print("\n**************************************")
        
        if len(notas) >= 1:


            for i in notas:
                print(f"*** {i[1]} - {i[2]} ***")
                print(i[2])
                print(i[3])

            print("**** fin de listado ****\n")

        else:

            print("\n*** No se han encontrado notas... ***\n")


    def borrar(self, usuario):
        print(f"\nOkey {usuario[1]}!! Vamor a borrar notas")
        titulo = input("Introduce el título de la nota a borrar: ")
        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()
        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota: {nota.titulo}")
        else:
            print("No se ha borrado la nota, prueba luego...")
