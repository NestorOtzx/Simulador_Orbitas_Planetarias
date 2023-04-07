from Graficos.Dibujo import Dibujo
from Graficos.Linea import Linea
from Pantalla import Pantalla
from Graficos.Circulo import Circulo
from Graficos.Texto import Texto
import math

import numpy as np



class Plano(Dibujo):

    ejeX = None
    ejeY = None

    #cada cuanto apareceran los puntos, por defecto 1 por cada unidad
    puntosPorUnidad = 8

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


        self.graficarEcuacion(self.ecuacion)

        #self.graficarFuncion(self.funcionA, (255, 0, 0), True, False, 3)

        xLetra = Texto("Txt1", (res[0]-20, res[1]/2+res[1]/64), "X", (255, 0, 0))
        yLetra = Texto("Txt2", (res[0]/2+10, 0), "Y", (0, 0, 0))

    def f(self, x, y):
        return x - 5*x/np.sqrt(x**2 + y**2)

    def graficarEcuacion(self, ecuacion, color = (0, 0, 255), dibujarLineas = False, dibujarPuntos = True, grosorDeLineas = 4):
        # Generar un rango de valores para x y y
        x = np.linspace(-25, 25, 1000)
        y = np.linspace(-25, 25, 1000)

        # Generar la malla de puntos correspondientes a la cuadrícula
        X, Y = np.meshgrid(x, y)

        # Evaluar la función en los puntos de la malla
        Z = self.f(X, Y)

        # recorrer la matriz Z
        sol_indices = np.where(np.abs(Z) < 0.01)

        # Obtener los valores de X e Y correspondientes a las soluciones
        sol_x = X[sol_indices]
        sol_y = Y[sol_indices]

        # Imprimir las soluciones
        for x, y in zip(sol_x, sol_y):
            print(f"La solución es x={x:.2f}, y={y:.2f}")
            Circulo("C", self.coordenadasAPixeles(x, y), 2, (0,0,0))
        

    def ecuacion(self, x):
       
        return x


    def graficarFuncion(self, funcion, color = (0, 0, 255), dibujarLineas = False, dibujarPuntos = True, grosorDeLineas = 4):
        res = Pantalla().resolucion

        #Tambien deben dibujarse por mitades para evitar que se desfacen del centro
        #lado derecho
        puntoAnterior = None
        for x in range(int(res[0]/2), int(res[0]), int(self.distanciaCuadriculas[0]/self.puntosPorUnidad)):
            coords = self.pixelesACoordenadas(x, 0)
            try:
                puntoGrafica =funcion(coords[0], coords[0])
                pos = self.coordenadasAPixeles(puntoGrafica[0], puntoGrafica[1])

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
                puntoGrafica =funcion(coords[0], coords[0])
                pos = self.coordenadasAPixeles(puntoGrafica[0], puntoGrafica[1])

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

        #print("Pixeles: ("+str(xPix)+" , "+str(yPix)+")" +" Coord: ("+str(xCoord)+" , "+str(yCoord)+")")
        return (xCoord, yCoord)
    
    def coordenadasAPixeles(self, xCoord : float, yCoord: float):
        res = Pantalla().resolucion
        xPix = (xCoord*self.distanciaCuadriculas[0] + res[0]/2)
        yPix = (-yCoord*self.distanciaCuadriculas[1] + res[1]/2)
        return (xPix, yPix)

    def tick(self, deltaTime):
        pass

