from Graficos.Dibujo import Dibujo
from Graficos.Linea import Linea
from Pantalla import Pantalla
from Graficos.Circulo import Circulo
from Graficos.Texto import Texto

import math

class Plano(Dibujo):

    ejeX = None
    ejeY = None

    #cada cuanto apareceran los puntos, por defecto 1 por cada unidad
    puntosPorUnidad = 16

    colorCuadricula = (200, 200, 200)

    distanciaCuadriculas = (20, 20)

    def __init__(self, nombre):
        super().__init__(nombre)
        self.dibujar()

    def dibujar(self): #Este metodo solo se llama al inicio
        res = Pantalla().resolucion

        #Cuadricula (tienen que dibujarse por mitades para evitar que se desfacen al no coincidir con el centro debido a su distancia de separación)
        #lado derecho
        for x in range(0, res[0], self.distanciaCuadriculas[0]):
            Linea("Y"+str(x), (res[0]/2+x, 0), (res[0]/2+x, res[1]), 1, self.colorCuadricula)
        #lado izquierdo
        for x in range(0, -res[0], -self.distanciaCuadriculas[0]):
            Linea("Y"+str(x), (res[0]/2+x, 0), (res[0]/2+x, res[1]), 1, self.colorCuadricula)

        #lineas horizontales
        for y in range(0, res[1], self.distanciaCuadriculas[1]):
            Linea("X"+str(x), (0, res[1]/2+y), (res[0], res[1]/2+y), 1, self.colorCuadricula)
        for y in range(0, -res[1], -self.distanciaCuadriculas[1]):
            Linea("X"+str(x), (0, res[1]/2+y), (res[0], res[1]/2+y), 1, self.colorCuadricula)

        #Eje X y eje Y
        self.ejeX = Linea("X", (0, res[1]/2), (res[0], res[1]/2), 5, (255, 0, 0))
        self.ejeY = Linea("Y", (res[0]/2, 0), (res[0]/2, res[1]), 5, (0, 0, 0))


        self.graficarFuncion(self.funcionA, (255, 0, 0), True, False, 3)
        self.graficarFuncion(self.funcionB, (255, 0, 0), True, False, 3)

        xLetra = Texto("Txt1", (res[0]-20, res[1]/2+res[1]/64), "X", (255, 0, 0))
        yLetra = Texto("Txt2", (res[0]/2+10, 0), "Y", (0, 0, 0))

        # crea un objeto de fuente
    
    

    def graficarFuncion(self, funcion, color = (0, 0, 255), dibujarLineas = False, dibujarPuntos = True, grosorDeLineas = 4):
        res = Pantalla().resolucion

        #Tambien deben dibujarse por mitades para evitar que se desfacen del centro
        #lado derecho
        puntoAnterior = None
        for x in range(int(res[0]/2), int(res[0]), int(self.distanciaCuadriculas[0]/self.puntosPorUnidad)):
            coords = self.pixelesACoordenadas(x, 0)
            try:
                print(str(coords[0])+" | "+str(funcion(coords[0])))
                pos = self.coordenadasAPixeles(coords[0], funcion(coords[0]))

                if (dibujarLineas):
                    if not puntoAnterior is None:
                        Linea("LPunto", puntoAnterior, pos, grosorDeLineas, color)
                    puntoAnterior = pos
                if (dibujarPuntos):
                    Circulo("Punto"+str(x), pos, 5, color)
            except:
                pass

        puntoAnterior = None
        #lado izquierdo
        for x in range(int(res[0]/2), 0, -int(self.distanciaCuadriculas[0]/self.puntosPorUnidad)):
            coords = self.pixelesACoordenadas(x, 0)
            try:
                pos = self.coordenadasAPixeles(coords[0], funcion(coords[0]))

                if (dibujarLineas):
                    if not puntoAnterior is None:
                        Linea("Punto", puntoAnterior, pos, grosorDeLineas, color)
                    puntoAnterior = pos
                if (dibujarPuntos):
                    Circulo("Punto"+str(x), pos, 5, color)
            except:
                pass

    def pixelesACoordenadas(self, xPix, yPix):
        res = Pantalla().resolucion
        xCoord = (xPix - res[0]/2)/self.distanciaCuadriculas[0]
        yCoord = -(yPix - res[1]/2)/self.distanciaCuadriculas[1]

        print("Pixeles: ("+str(xPix)+" , "+str(yPix)+")" +" Coord: ("+str(xCoord)+" , "+str(yCoord)+")")
        return (xCoord, yCoord)
    
    def coordenadasAPixeles(self, xCoord : float, yCoord: float):
        res = Pantalla().resolucion
        xPix = (xCoord*self.distanciaCuadriculas[0] + res[0]/2)
        yPix = (-yCoord*self.distanciaCuadriculas[1] + res[1]/2)
        #print("Coord: ("+str(xCoord)+" , "+str(yCoord)+")" + " Pixeles: ("+str(xPix)+" , "+str(yPix)+")" )
        return (xPix, yPix)

    def funcionA(self, x):
        return math.pow(x, math.sin(x))
    
    def funcionB(self, x):
        return -math.pow(x, math.sin(x))


    def xFunc(self, x):
        return x

    def tick(self, deltaTime):
        pass

