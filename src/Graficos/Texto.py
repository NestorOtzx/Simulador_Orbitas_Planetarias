import pygame
from Pantalla import Pantalla
from Graficos.Dibujo import Dibujo

class Texto(Dibujo):

    texto=None
    def __init__(self, nombre : str, posicion, texto, color = (0, 0, 0)):
        super().__init__(nombre, color)
        self.posicion = posicion
        font = pygame.font.Font(None, 36)
        # crea una superficie de texto
        self.texto = font.render(texto, True, color)

    def dibujar(self):
        Pantalla().ventana.blit(self.texto, self.posicion)

    def tick(self, deltaTime):
        self.dibujar()
    