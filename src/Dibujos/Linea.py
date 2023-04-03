from Dibujos.Dibujo import Dibujo
from InfoManager import InfoManager
from typing import Tuple
import pygame

class Linea(Dibujo):

    cola = (500, 0)
    cabeza = (1000, 0)
    ancho = 5

    def __init__(self, cola, cabeza, ancho):
        super().__init__()
        self.cola = cola
        self.cabeza = cabeza
        self.ancho = ancho

    def dibujar(self):
        pygame.draw.line(InfoManager().ventana, self.color, self.cola, self.cabeza, self.ancho)

    def tick(self, deltaTime):
        self.dibujar()