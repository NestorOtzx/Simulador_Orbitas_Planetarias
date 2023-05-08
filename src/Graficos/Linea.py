import pygame
from Graficos.Dibujo import Dibujo
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

    # Dibujar la linea en cada fotograma
    def dibujar(self):
        pygame.draw.line(Pantalla().ventana, self.color, (self.cola[0]+ self.posicion[0], self.cola[1]+self.posicion[1])
                         , (self.cabeza[0]+ self.posicion[0], self.cabeza[1]+self.posicion[1]), self.ancho)

    def tick(self, deltaTime):
        self.dibujar()

        
 
        
