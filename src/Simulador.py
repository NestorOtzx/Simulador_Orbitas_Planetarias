import pygame
from InfoManager import InfoManager

from Dibujos.Circulo import Circulo
from Dibujos.Linea import Linea
from Objeto import Objeto

from typing import Tuple
class Simulacion:


    def __init__(self):
        self.valor = 0

    #metodo llamado solamente al inicio de la simulacion
    def inicio(self):
        print("--Inicio de la simulacion--")

        #dibujar linea
        linea = Linea((0,0), (300, 0), 5)
        #dibujar circulo
        circulo = Circulo((100, 100), 40)
 

    #metodo llamado en cada fotograma, donde deltatime es el tiempo transcurrido desde el fotograma anterior
    def tick(self, deltaTime):
        #Actualizar todos los objetos
        #Logica del simulador
        
        Objeto.tick_global(deltaTime)

    def iniciarSimulacion(self):

        #--Inicializacion basica--
        #frames a los que se espera que el programa se ejecute
        #clock = pygame.time.Clock()
        
        pygame.init()

        #resolucion
        ventana =  pygame.display.set_mode(InfoManager.resolucion)
        InfoManager().ventana =ventana

        #nombre de la ventana
        pygame.display.set_caption("Simulador de fisica")

        self.inicio()

        #bucle principal
        while (True):

            #tiempo transcurrido en segundos desde el frame anterior
            delta_time = 0

            
            
            self.tick(delta_time)

            pygame.display.update()
            
            for evento in pygame.event.get():
                if (evento.type == pygame.QUIT):
                    pygame.quit()

            InfoManager().ventana.fill((255, 255, 255))

        pygame.quit()

