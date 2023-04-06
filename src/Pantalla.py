from Singleton import Singleton

#Guarda informacion basica del entorno usado una clase singleton
class Pantalla(metaclass = Singleton):

    ventana = None
    resolucion = (1200, 900)
    FPS = 60

