from Interfaz.Boton import Boton

class Interfaz:

    def __init__(self, plano):
        Boton("b", (200, 200, 200), self.defaultFunc, (0,0), (200, 50), "Planeta Tierra")
        
    def defaultFunc(self):
        print("Boton siendo presionado")