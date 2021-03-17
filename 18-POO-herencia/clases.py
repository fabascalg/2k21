# herencia

class Persona:
    """
    nombre
    apellidos
    altura
    edad
    """

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setAltura(self, altura):
        self.altura = altura

    def setEdad(self, edad):
        self.edad = edad

    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos

    def getAltura(self):
        return self.altura

    def getEdad(self):
        return self.edad

    def caminar(self):
        return "Estoy caminando"

    def hablar(self):
        return "Estoy hablando"

    def dormir(self):
        return "Estoy roncando"

    def informe(self):
        lista = "\n*** Instancia de Persona ***"
        lista += "\nNombre -> " + self.getNombre()
        lista += "\nApellidos -> " + self.getApellidos()
        lista += "\nAltura -> " + self.getAltura()
        lista += "\nEdad -> " + self.getEdad() + "\n====================\n"
        return lista


class Informatico(Persona):
    """
        lenguajes
        experiencia
    """

    def __init__(self):
        self.lenguajes = "HTML, CSS, Javascript, PHP"
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguajes

    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes

    def programar(self):
        return "Estoy programando"

    def repararOrdenador(self):
        return "Estoy reparando un ordenador"

class TecnicoRedes(Informatico):

    def __init__(self):
        super().__init__()      #fuerzo a inicializar al padre
        self.auditarRedes = "experto"
        self.experienciaRedes = 15
    
    def auditoria(self):
        return "Estoy auditando una red"

    def getExperiencia(self):
        return self.experienciaRedes
    
    def getAuditarRedes(self):
        return self.auditarRedes

    