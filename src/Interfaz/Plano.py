from Dibujos.Dibujo import Dibujo
from Dibujos.Linea import Linea
from Pantalla import Pantalla
from Dibujos.Circulo import Circulo
from Utilidades.Posicion import Posicion

class Plano(Dibujo):

    ejeX = None
    ejeY = None

    def __init__(self, nombre):
        super().__init__(nombre)
        self.dibujar()

    def dibujar(self):
        res = Pantalla().resolucion

        #Eje X y eje Y
        self.ejeX = Linea("L1", Posicion(-res[0]/2, 0).value, Posicion(res[0]/2, 0).value, 3, (255, 0, 0))
        self.ejeY = Linea("L1", Posicion(0, -res[1]/2).value, Posicion(0, res[1]/2).value, 3, (0, 0, 0))

        #simple parabola
        for x in range(-100, 100):
            circulo = Circulo("", Posicion(x, x**2, 10).value, 5, (0, 0, 255),)

    def tick(self, deltaTime):
        pass

