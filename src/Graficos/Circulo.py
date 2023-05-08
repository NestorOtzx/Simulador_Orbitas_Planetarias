import pygame
from Graficos.Dibujo import Dibujo
from Pantalla import Pantalla

class Circulo(Dibujo):

    radio = 0

    def __init__(self, nombre : str, posicion, radio : int, color = (0, 0, 0)):
        super().__init__(nombre, color)
        self.posicion = posicion
        self.radio = radio
        
    # Dibujar el circulo en cada fotograma
    def dibujar(self):
        if (self.posicion[0] > 0 and self.posicion[1]>0):
            pygame.draw.circle(Pantalla().ventana, self.color, self.posicion, self.radio)

    def tick(self, deltaTime):
        self.dibujar()
    
