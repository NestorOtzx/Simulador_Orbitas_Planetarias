from Graficos.Dibujo import Dibujo
from Pantalla import Pantalla
from Interfaz.Boton import Boton

import math
import numpy as np
import pygame

class Plano(Dibujo):

    #cada cuanto apareceran los puntos, por defecto 1 por cada unidad
    puntosPorUnidad = 8

    colorCuadricula = (200, 200, 200)

    distanciaCuadriculas = (100, 100)

    MAXDISTCUADRICULAS = (400, 400)


    def __init__(self, nombre):
        super().__init__(nombre)

    def zoom(self, val):
        self.setDistanciaCuadriculas(val, val)

    def setDistanciaCuadriculas(self, x,y):
        currDist =self.distanciaCuadriculas
        if (currDist[0]+x) < self.MAXDISTCUADRICULAS[0] and currDist[0]+x > 0 and currDist[1]+y < self.MAXDISTCUADRICULAS[1] and currDist[1]+y > 0:
            self.distanciaCuadriculas = (self.distanciaCuadriculas[0]+x, self.distanciaCuadriculas[1]+y)

    def dibujar(self): #Dibujar el plano
        res = Pantalla().resolucion
        # Cuadricula (tienen que dibujarse por mitades para evitar que se desfacen al no coincidir con el centro debido a su distancia de separación)
        # lado derecho
        for x in range(0, res[0], self.distanciaCuadriculas[0]):
            pygame.draw.line(Pantalla().ventana, self.colorCuadricula, (res[0]/2+x, 0), (res[0]/2+x, res[1]), 1)
        # lado izquierdo
        for x in range(0, -res[0], -self.distanciaCuadriculas[0]):
            pygame.draw.line(Pantalla().ventana, self.colorCuadricula, (res[0]/2+x, 0), (res[0]/2+x, res[1]), 1)
        # lineas horizontales
        for y in range(0, res[1], self.distanciaCuadriculas[1]):
            pygame.draw.line(Pantalla().ventana, self.colorCuadricula, (0, res[1]/2+y), (res[0], res[1]/2+y), 1)
        for y in range(0, -res[1], -self.distanciaCuadriculas[1]):
            pygame.draw.line(Pantalla().ventana, self.colorCuadricula, (0, res[1]/2+y), (res[0], res[1]/2+y), 1)

        #Eje x
        pygame.draw.line(Pantalla().ventana, (255, 0, 0), (0, res[1]/2), (res[0], res[1]/2), 5)

        #Eje y
        pygame.draw.line(Pantalla().ventana, (0, 0, 0), (res[0]/2, 0), (res[0]/2, res[1]), 5)

        font = pygame.font.Font(None, 36)

        textoX = font.render("X", True, (255, 0, 0))
        Pantalla().ventana.blit(textoX, (res[0]-20, res[1]/2+res[1]/64))

        textoY = font.render("Y", True, (0, 0, 0))
        Pantalla().ventana.blit(textoY, (res[0]/2+10, 0))

        self.GraficarFunciones()


    def GraficarFunciones(self):
        self.graficarOrbita(39.5, 1/52, (1, 0), (0, 2*math.pi), 100, (0, 255, 0))
        self.graficarOrbita(39.5, 1/52, (1, 0), (0, 2.1*math.pi), 200, (100, 100, 100))
        self.graficarOrbita(39.5, 1/520, (1, 0), (0, math.pi), 200, (0, 100, 100))



    def graficarOrbita(self, gm, dt, posInit, velInit, semanas, color = (0, 0, 255)):
        x = posInit[0]
        y = posInit[1]

        vx = velInit[0]
        vy = velInit[1]


        coords = self.coordenadasAPixeles(x,y)
        if (coords[0] > 0 and coords[1]>0):
                pygame.draw.circle(Pantalla().ventana, color, coords, 3)

        for t in range(0, semanas):
            qx = -1*gm*x/math.pow(x**2+y**2, 1.5)
            qy = -1*gm*y/math.pow(x**2+y**2, 1.5)

            vx = vx+qx*dt
            vy = vy+qy*dt

            x = x+vx*dt
            y = y+vy*dt

            coords = self.coordenadasAPixeles(x,y)
            if (coords[0] > 0 and coords[1]>0):
                pygame.draw.circle(Pantalla().ventana, color, coords, 3)

                
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
            #Circulo("C", self.coordenadasAPixeles(x, y), 2, color)
            pass

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
                        #Linea("LPunto", puntoAnterior, pos, grosorDeLineas, color)
                        pass
                    puntoAnterior = pos
                if (dibujarPuntos):
                    # Circulo("Punto"+str(x), pos, 3, color)
                    pass
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
                        #Linea("Punto", puntoAnterior, pos, grosorDeLineas, color)
                        pass
                    puntoAnterior = pos
                if (dibujarPuntos):
                    pass
                    #Circulo("Punto"+str(x), pos, 3, color)
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
        self.dibujar()

