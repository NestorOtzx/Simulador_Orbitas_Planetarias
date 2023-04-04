
class Objeto():

    #todos los objetos en la simulacion
    __instancias = []

    nombre = ""

    posicionX = 0
    posicionY = 0

    def __init__(self, nombre):
        self.__instancias.append(self)
        self.nombre = nombre

    #este metodo actualizara a todos los objetos por el metodo tick.
    @classmethod
    def tick_global(cls, deltaTime):
        for instancia in cls.__instancias:
            instancia.tick(deltaTime)
        pass

    def tick(self, deltaTime):
        pass

    def mover(self, posicion):
        self.posicionX += posicion[0]
        self.posicionY += posicion[1]

