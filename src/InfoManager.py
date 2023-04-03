
#Guarda informacion basica del entorno usado una clase singleton
class InfoManager:

    __instancia = None

    ventana = None
    resolucion = (960, 540)
    FPS = 60


    def __new__(cls):
        if InfoManager.__instancia is None:
            print("new")
            InfoManager.__instancia = object.__new__(cls)
        else:
            print("viejo")
        return InfoManager.__instancia
