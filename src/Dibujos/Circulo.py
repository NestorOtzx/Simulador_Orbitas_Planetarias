from Dibujos.Dibujo import Dibujo
import pygame
from InfoManager import InfoManager

class Circulo(Dibujo):

    radio = 0
    posicion = 0

    def __init__(self, posicion, radio):
        super().__init__()
        self.posicion = posicion
        self.radio = radio

    def dibujar(self):
        pygame.draw.circle(InfoManager().ventana, self.color, self.posicion, self.radio)

    def tick(self, deltaTime):
        self.dibujar()
    
