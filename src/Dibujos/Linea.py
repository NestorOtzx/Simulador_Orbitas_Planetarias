import pygame
from Dibujos.Dibujo import Dibujo
from Pantalla import Pantalla

class Linea(Dibujo):

    cola = None
    cabeza = None
    ancho = 0


    def __init__(self, nombre : str, cola, cabeza, ancho : int, color = (0, 0, 0)):
        super().__init__(nombre, color)

        self.cola = cola
        self.cabeza = cabeza
        self.ancho = ancho

    def dibujar(self):
        pygame.draw.line(Pantalla().ventana, self.color, (self.cola[0]+ self.posicionX, self.cola[1]+self.posicionY)
                         , (self.cabeza[0]+ self.posicionX, self.cabeza[1]+self.posicionY), self.ancho)

    def tick(self, deltaTime):
        self.dibujar()

        
 
        
