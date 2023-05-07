from Interfaz.ElementoGUI import ElementoGUI
from Pantalla import Pantalla
import pygame

class Boton(ElementoGUI):

    color = (255, 0, 0)

    funcionAlPresionar = None

    def __init__(self, nombre, color = (0, 0, 0), funcionAlPresionar = None, pos = (0, 0), tam = (1, 1), texto = "", colorBorde = (0,0,0)):
        super().__init__(nombre)
        self.color = color
        self.colorBorde = colorBorde
        self.boton = pygame.Rect(pos[0], pos[1], tam[0], tam[1])
        self.funcionAlPresionar = funcionAlPresionar



        if len(texto) > 0:
            self.texto = texto
            self.font = pygame.font.SysFont(None, 30)
            self.textRender = self.font.render(texto, True, (0,0,0))
            self.text_rect = self.textRender.get_rect()
            self.text_rect.center = self.boton.center

    def tick(self, deltaTime, eventos):
        #interior
        pygame.draw.rect(Pantalla().ventana, self.color, self.boton)

        # borde
        pygame.draw.rect(Pantalla().ventana, self.colorBorde, self.boton, 2)

        Pantalla().ventana.blit(self.textRender, self.text_rect)

        for event in eventos:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.boton.collidepoint(event.pos):
                    self.funcionAlPresionar()     
                
                    






