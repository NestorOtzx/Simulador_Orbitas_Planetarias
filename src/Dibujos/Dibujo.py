from Objeto import Objeto



class Dibujo(Objeto):

    color = (255, 0, 0)

    def __init__(self, nombre, color = (0, 0, 0)):
        super().__init__(nombre)
        self.color = color

    def dibujar(self):
        pass

