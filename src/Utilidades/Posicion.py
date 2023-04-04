from Pantalla import Pantalla

#Crear valores de posicion respecto al centro de la pantalla
class Posicion:
    x = 0
    y = 0

    def __init__(self, x, y, multiplicador = 1):
        #el eje y esta invertido, por eso se resta
        self.x = (Pantalla.resolucion[0]/2+(x*multiplicador)) 
        self.y = ((Pantalla.resolucion[1]/2)-(y*multiplicador))
        print("Original")
        print("X: "+ str(x)+" Y: "+str(y))
        print("Procesado")
        print("X: "+ str(self.x)+" Y: "+str(self.y))

        self.value = (self.x, self.y)
