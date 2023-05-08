from Interfaz.ElementoGUI import ElementoGUI
from Pantalla import Pantalla
import pygame

class Boton(ElementoGUI):

    defColor = (255, 255, 255)
    colorActual = defColor

    funcionAlPresionar = None
    permanecePresionado = False
    presionado = False

    def __init__(self, nombre, color = (255, 255, 255), funcionAlPresionar = None, pos = (0, 0), tam = (1, 1), texto = "", colorBorde = (0,0,0), permanecePresionado = False, colorPresionado = (200, 200, 200)):
        super().__init__(nombre)
        self.defColor = color
        self.colorBorde = colorBorde
        self.boton = pygame.Rect(pos[0], pos[1], tam[0], tam[1])
        self.funcionAlPresionar = funcionAlPresionar
        self.colorActual = self.defColor
        self.colorPresionado = colorPresionado
        self.permanecePresionado = permanecePresionado

        # Si el botón contiene texto
        if len(texto) > 0:
            self.texto = texto
            self.font = pygame.font.SysFont(None, 30)
            self.textRender = self.font.render(texto, True, (0,0,0))
            self.text_rect = self.textRender.get_rect()
            self.text_rect.center = self.boton.center

    def tick(self, deltaTime, eventos):
        #interior
        pygame.draw.rect(Pantalla().ventana, self.colorActual, self.boton)

        # borde
        pygame.draw.rect(Pantalla().ventana, self.colorBorde, self.boton, 2)

        Pantalla().ventana.blit(self.textRender, self.text_rect)

        for event in eventos:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.boton.collidepoint(event.pos):
                    self.funcionAlPresionar()
                    if self.permanecePresionado:
                        self.setPresionado()

    def setPresionado(self):
        if not self.presionado:
            self.colorActual = self.colorPresionado
            self.presionado = True
        else:
            self.colorActual = self.defColor
            self.presionado = False
            pass

                
                    






