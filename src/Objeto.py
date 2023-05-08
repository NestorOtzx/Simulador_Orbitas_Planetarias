
# Clase base para todos los objetos del entorno de la simulación
class Objeto():

    #todos los objetos en la simulacion
    __instancias = []

    nombre = ""

    #Posicion en pixeles
    posicion = (0,0)
    

    def __init__(self, nombre):
        self.__instancias.append(self)
        self.nombre = nombre

    # Este metodo actualizará todos los objetos existentes con el metodo tick.
    @classmethod
    def tick_global(cls, deltaTime):
        for instancia in cls.__instancias:
            instancia.tick(deltaTime)
        pass

    def tick(self, deltaTime):
        pass

    def destroy(self):
        self.__instancias.remove(self)
        del self

