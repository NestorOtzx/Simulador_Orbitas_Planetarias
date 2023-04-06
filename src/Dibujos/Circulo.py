import pygame
from Dibujos.Dibujo import Dibujo
from Pantalla import Pantalla
class Circulo(Dibujo):

    radio = 0

    def __init__(self, nombre : str, posicion, radio : int, color = (0, 0, 0)):
        super().__init__(nombre, color)
        self.posicion = posicion
        self.radio = radio
        

    def dibujar(self):
        pygame.draw.circle(Pantalla().ventana, self.color, self.posicion, self.radio)

    def tick(self, deltaTime):
        self.dibujar()
    
