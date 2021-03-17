class Coche:

    # atributos o propiedades (variables)

    marca = "Ferrari"
    modelo = "Aventador"
    color = "Rojo"    
    caballaje = 1500
    plazas = 3
    velocidad = 115

    # constructor
    def __init__(self, marca, modelo, color, caballaje, plazas, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.caballaje = caballaje
        self.plazas = plazas
        self.velocidad = velocidad


    # métodos, acciones que hace el objeto (funciones)

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def setCaballaje(self, caballaje):
        self.caballaje = caballaje

    def getCaballaje(self):
        return self.caballaje

    def setPlazas(self, plazas):
        self.plazas = plazas

    def getPlazas(self):
        return self.plazas

    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def todoCoche(self):
        lista = "\n*** INSTANCIA DE COCHE ***\n"
        lista += "    Marca: " + self.getMarca() + "\n"
        lista += "   Modelo: " + self.getModelo() + "\n"
        lista += "    Color: " + self.getColor() + "\n"
        lista += "Caballaje: " + str(self.getCaballaje()) + "\n"
        lista += "   Plazas: " + str(self.getPlazas()) + "\n"
        lista += "Velocidad: " + str(self.getVelocidad()) + "\n"
        lista += "=========================="
        return lista

#fin de clase Coche