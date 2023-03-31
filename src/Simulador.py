import pygame


class Simulacion:
    def __init__(self):
        self.valor = 0

    #metodo llamado en cada fotograma, donde deltatime es el tiempo transcurrido desde el fotograma anterior
    def tick(self, deltaTime):
        print("tick: " + str(deltaTime))

    def iniciarSimulacion(self):

        print("---Inicio de simulacion---")
        #--Inicializacion basica--
        #frames a los que se espera que el programa se ejecute
        FPS = 60

        clock = pygame.time.Clock()
        
        pygame.init()

        #resolucion
        ventana = pygame.display.set_mode((960, 540))
        #nombre de la ventana
        pygame.display.set_caption("Simulador de fisica")

        #bucle principal
        while (True):

            #tiempo transcurrido en segundos desde el frame anterior
            delta_time = clock.tick(FPS) / 1000.0 
            
            for evento in pygame.event.get():
                if (evento.type == pygame.QUIT):
                    pygame.quit()

            #Logica del simulador
            self.tick(delta_time)

            #redibujar la pantalla
            ventana.fill((255, 255, 255))
            pygame.display.flip()

        pygame.quit()

