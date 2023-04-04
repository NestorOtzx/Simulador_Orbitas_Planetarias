from Singleton import Singleton

#Guarda informacion basica del entorno usado una clase singleton
class Pantalla(metaclass = Singleton):

    ventana = None
    resolucion = (960, 540)
    FPS = 60

