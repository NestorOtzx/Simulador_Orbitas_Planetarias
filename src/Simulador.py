import pygame
from Pantalla import Pantalla

from Objeto import Objeto
from Interfaz.ElementoGUI import ElementoGUI

from Graficos.Plano import Plano
from Interfaz.Interfaz import Interfaz

class Simulacion:

    def __init__(self):
        self.valor = 0
    
    #metodo llamado solamente al inicio de la simulacion
    def inicio(self):
        self.objeto = Objeto("Main")
        self.UI = ElementoGUI("UI")
        self.plano = Plano("Plano cartesiano")
        self.interfaz = Interfaz(self.plano)


    # Método llamado en cada frame para actualizar objetos del entorno
    def tick(self, deltaTime):
        self.objeto.tick_global(deltaTime)

    # Método llamado en cada frame para actualizar la interfaz de usuario
    def tickInterfaz(self, deltaTime, eventos):
        self.UI.tick_global(deltaTime, eventos)


    def iniciarSimulacion(self):
        pygame.init()

        # Crear la ventana de pantalla completa con el centro en (0, 0)
        ventana = pygame.display.set_mode(Pantalla.resolucion)
        
        Pantalla().ventana =ventana

        # Nombre de la ventana
        pygame.display.set_caption("Simulador de fisica")

        self.inicio()

        # Clock para calcular deltaTime
        clock = pygame.time.Clock()

        # Bucle principal
        while (True):

            #tiempo transcurrido en segundos desde el frame anterior en segundos
            deltaTime = clock.tick(60) / 1000.0 

            # Actualizar elementos
            self.tick(deltaTime)

            eventos = pygame.event.get()

            # Actualizar Interfaz
            self.tickInterfaz(deltaTime, eventos)

            # Leer input
            for evento in eventos:
                if (evento.type == pygame.QUIT):
                    pygame.quit()

                # Detecta la rueda del mouse
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 4:
                    self.plano.zoom(10)
                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 5:
                    self.plano.zoom(-10)
                
            #Actualizar Pantalla
            pygame.display.update()

            Pantalla().ventana.fill((255, 255, 255))
        pygame.quit()

