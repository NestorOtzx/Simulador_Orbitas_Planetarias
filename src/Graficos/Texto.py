import pygame
from Pantalla import Pantalla
from Graficos.Dibujo import Dibujo

class Texto(Dibujo):

    texto=None
    def __init__(self, nombre : str, posicion, texto, color = (0, 0, 0), size = 1):
        super().__init__(nombre, color)
        self.posicion = posicion
        self.font = pygame.font.Font(None, size*int(Pantalla().resolucion[1]/30))
        # crea una superficie de texto
        color = self.color = color
        self.texto = self.font.render(texto, True, self.color)

    def dibujar(self):
        Pantalla().ventana.blit(self.texto, self.posicion)

    def tick(self, deltaTime):
        self.dibujar()

    def modificarTexto(self, txt):
        self.texto = self.font.render(txt, True, self.color)
    