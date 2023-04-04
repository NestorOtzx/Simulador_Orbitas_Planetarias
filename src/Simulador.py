import pygame
from Pantalla import Pantalla

from Objeto import Objeto
from Interfaz.Plano import Plano

from typing import Tuple
class Simulacion:

    #objeto global
    objeto = None    

    fondo = None

    def __init__(self):
        self.valor = 0
    
    #metodo llamado solamente al inicio de la simulacion
    def inicio(self):
        self.objeto = Objeto("Main")
        self.fondo = Plano("Plano cartesiano")


    #metodo llamado en cada fotograma, donde deltatime es el tiempo transcurrido desde el fotograma anterior
    def tick(self, deltaTime):
        #Actualizar todos los objetos
        self.objeto.tick_global(deltaTime)

    def iniciarSimulacion(self):

        #--Inicializacion basica--
        pygame.init()

        #Crear la ventana de pantalla completa con el centro en (0, 0)
        ventana = pygame.display.set_mode(Pantalla.resolucion)
        
        Pantalla().ventana =ventana


        #nombre de la ventana
        pygame.display.set_caption("Simulador de fisica")

        self.inicio()

        #Clock para calcular deltaTime
        clock = pygame.time.Clock()

        #bucle principal
        while (True):

            #tiempo transcurrido en segundos desde el frame anterior en segundos
            deltaTime = clock.tick(60) / 1000.0 

            self.tick(deltaTime)

            

            for evento in pygame.event.get():
                if (evento.type == pygame.QUIT):
                    pygame.quit()
            pygame.display.update()

            Pantalla().ventana.fill((255, 255, 255))

        pygame.quit()

