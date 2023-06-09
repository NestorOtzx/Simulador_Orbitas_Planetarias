class ElementoGUI():

    #todos los objetos en la simulacion
    __instancias = []

    nombre = ""

    #Posicion en pixeles
    posicion = (0,0)
    

    def __init__(self, nombre):
        self.__instancias.append(self)
        self.nombre = nombre

    # Este metodo actualizará todos los elementos de la interfaz existentes con el metodo tick.
    @classmethod
    def tick_global(cls, deltaTime, eventos):
        for instancia in cls.__instancias:
            instancia.tick(deltaTime, eventos)
        pass

    def tick(self, deltaTime, eventos):
        pass

    def destroy(self):
        self.__instancias.remove(self)
        del self
