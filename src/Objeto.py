
class Objeto():

    #todos los objetos en la simulacion
    __instancias = []


    def __init__(self):
        self.__instancias.append(self)
        print("Instancia padre en accion ")

    #este metodo actualizara a todos los objetos por el metodo tick.
    @classmethod
    def tick_global(cls, deltaTime):
        for instancia in cls.__instancias:
            instancia.tick(deltaTime)
        pass

    def tick(self, deltaTime):
        pass



