# POO o OOP

# definir una clase

class Coche:

    # atributos o propiedades (variables)

    marca = "Ferrari"
    modelo = "Aventador"
    color = "Rojo"    
    caballaje = 1500
    plazas = 3
    velocidad = 115

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
        lista = ""
        lista = "Marca: " + self.marca + "\n"
        lista += "Modelo: " + self.modelo + "\n"
        lista += "Color: " + self.color + "\n"
        lista += "Caballaje: " + str(self.caballaje) + "\n"
        lista += "plazas: " + str(self.plazas) + "\n"
        lista += "velocidad: " + str(self.velocidad) + "\n"
        return lista


coche = Coche()

coche.caballaje = 300
coche.color = "rojo"
coche.marca = "Chevrolet"
coche.modelo = "Chevette"
coche.plazas = 5
coche.velocidad = 0
#print("\n")
#print(coche.marca, coche.modelo, coche.color, coche.caballaje, coche.plazas, coche.velocidad)
print("\n")
print(coche.todoCoche())
print("\n... acelerar a cien\n")
for n in range(0,100):
    coche.acelerar()
print("\n")
#print(coche.marca, coche.modelo, coche.color, coche.caballaje, coche.plazas, coche.velocidad)
print(coche.todoCoche())
print("\n... desacelerar a venticinco\n")
for n in range(0,75):
    coche.frenar()
print("\n")
print(coche.todoCoche())
print("\n")


