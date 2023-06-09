from Interfaz.Boton import Boton
from Pantalla import Pantalla
from Graficos.Texto import Texto
import math

class Interfaz:

    colorBotones = (255, 255, 255)
    colorBorde = (200, 200, 200)

    personalizadoVisible = False

    elementosPersonalizado = []

    textoPosx = None
    textoPosy = None
    textoVelx = None
    textoVely = None
    textoPuntos = None

    def __init__(self, plano):
        self.plano = plano
        res = Pantalla().resolucion

        # Botones de cada planeta
        Boton("b1", self.colorBotones, self.mercurio, (0,0), (res[0]/6, res[1]/18), "Mercurio", self.colorBorde, permanecePresionado=True)
        Boton("b2", self.colorBotones, self.venus, (0, 1*res[1]/16), (res[0]/6, res[1]/18), "Venus", self.colorBorde, permanecePresionado=True)
        Boton("b3", self.colorBotones, self.tierra, (0,2*res[1]/16), (res[0]/6, res[1]/18), "Tierra", self.colorBorde, permanecePresionado=True)
        Boton("b4", self.colorBotones, self.marte, (0,3*res[1]/16), (res[0]/6, res[1]/18), "Marte", self.colorBorde, permanecePresionado=True)
        Boton("b5", self.colorBotones, self.jupiter, (0,4*res[1]/16), (res[0]/6, res[1]/18), "Jupiter", self.colorBorde, permanecePresionado=True)
        Boton("b6", self.colorBotones, self.saturno, (0,5*res[1]/16), (res[0]/6, res[1]/18), "Saturno", self.colorBorde, permanecePresionado=True)
        Boton("b7", self.colorBotones, self.urano, (0,6*res[1]/16), (res[0]/6, res[1]/18), "Urano", self.colorBorde, permanecePresionado=True)
        Boton("b8", self.colorBotones, self.neptuno, (0,7*res[1]/16), (res[0]/6, res[1]/18), "Neptuno", self.colorBorde, permanecePresionado=True)
        
        # Boton personalizado
        Boton("personalizado", self.colorBotones, self.planetaPersonalizado, (res[0]-res[0]/6, 0), (res[0]/6, res[1]/18), "Personalizado", self.colorBorde, permanecePresionado=True)

    # Menú del planeta personalizado
    def planetaPersonalizado(self):
        self.personalizado()

        if not self.personalizadoVisible: # Mostrar el menú del planeta personalizado
            res = Pantalla().resolucion
            self.personalizadoVisible = True
            datos = self.plano.datosPersonalizado

            self.textoPuntos = Texto("puntos", (res[0]-res[0]/3.75, 1.25*res[1]/16), "Puntos a graficar: "+str(datos["puntos"]), (255, 0, 0))
            self.elementosPersonalizado.append(Boton("IncPts", self.colorBotones, self.incPuntos, (res[0]-res[0]/6.5,  2*res[1]/16), (res[1]/18,  res[1]/18), "+", self.colorBorde))
            self.elementosPersonalizado.append(Boton("DecPts", self.colorBotones, self.decPuntos, (res[0]-res[0]/4.5,  2*res[1]/16), (res[1]/18,  res[1]/18), "-", self.colorBorde))

            posxFormat = "{:.1f}".format(datos["posx"])
            self.textoPosx = Texto("posx", (res[0]-res[0]/4, 3.25*res[1]/16), "Posicion X: "+posxFormat+" UA", (255, 0, 0))
            self.elementosPersonalizado.append(Boton("IncMasa", self.colorBotones, self.incPosx, (res[0]-res[0]/6.5,  4*res[1]/16), (res[1]/18,  res[1]/18), "+", self.colorBorde))
            self.elementosPersonalizado.append(Boton("DecMasa", self.colorBotones, self.decPosx, (res[0]-res[0]/4.5,  4*res[1]/16), (res[1]/18,  res[1]/18), "-", self.colorBorde))

            posyFormat = "{:.1f}".format(datos["posy"])
            self.textoPosy = Texto("posy", (res[0]-res[0]/4, 5.25*res[1]/16), "Posicion Y: "+posyFormat+" UA", (255, 0, 0))
            self.elementosPersonalizado.append(Boton("IncMasa", self.colorBotones, self.incPosy, (res[0]-res[0]/6.5,  6*res[1]/16), (res[1]/18,  res[1]/18), "+", self.colorBorde))
            self.elementosPersonalizado.append(Boton("DecMasa", self.colorBotones, self.decPosy, (res[0]-res[0]/4.5,  6*res[1]/16), (res[1]/18,  res[1]/18), "-", self.colorBorde))

            velxFormat = "{:.4f}".format(datos["velx"])
            self.textoVelx = Texto("vx", (res[0]-res[0]/3.5, 7.25*res[1]/16), "Velocidad X: "+velxFormat+" UA/año", (255, 0, 0))
            self.elementosPersonalizado.append(Boton("IncMasa", self.colorBotones, self.incVelx, (res[0]-res[0]/6.5,  8*res[1]/16), (res[1]/18,  res[1]/18), "+", self.colorBorde))
            self.elementosPersonalizado.append(Boton("DecMasa", self.colorBotones, self.decVelx, (res[0]-res[0]/4.5,  8*res[1]/16), (res[1]/18,  res[1]/18), "-", self.colorBorde))

            velyFormat = "{:.4f}".format(datos["vely"])
            self.textoVely = Texto("vy", (res[0]-res[0]/3.5, 9.25*res[1]/16), "Velocidad Y: "+velyFormat+" UA/año", (255, 0, 0))
            self.elementosPersonalizado.append(Boton("IncMasa", self.colorBotones, self.incVely, (res[0]-res[0]/6.5,  10*res[1]/16), (res[1]/18,  res[1]/18), "+", self.colorBorde))
            self.elementosPersonalizado.append(Boton("DecMasa", self.colorBotones, self.decVely, (res[0]-res[0]/4.5,  10*res[1]/16), (res[1]/18,  res[1]/18), "-", self.colorBorde))

            

        else: # Cerrar el menú del planeta personalizado
            for objeto in self.elementosPersonalizado:
                objeto.destroy()
            self.textoPosx.destroy()
            self.textoPosy.destroy()
            self.textoVelx.destroy()
            self.textoVely.destroy()
            self.textoPuntos.destroy()

            self.elementosPersonalizado = []
            self.personalizadoVisible = False

    def incPosx(self):
        self.modificarAtributo("posx", "Posicion X: ", 0.1, self.textoPosx, " UA", decimales=1)

    def decPosx(self):
        self.modificarAtributo("posx", "Posicion X: ", -0.1, self.textoPosx, " UA",  decimales=1)

    def incPosy(self):
        self.modificarAtributo("posy", "Posicion Y: ", 0.1, self.textoPosy, " UA",  decimales=1)

    def decPosy(self):
        self.modificarAtributo("posy", "Posicion Y: ", -0.1, self.textoPosy, " UA",  decimales=1)

    def incVelx(self):
        self.modificarAtributo("velx", "Velocidad X: ", math.pi/8, self.textoVelx, " UA/año")

    def decVelx(self):
        self.modificarAtributo("velx", "Velocidad X: ", -math.pi/8, self.textoVelx, " UA/año")

    def incVely(self):
        self.modificarAtributo("vely", "Velocidad Y: ", math.pi/8, self.textoVely, " UA/año")

    def decVely(self):
        self.modificarAtributo("vely", "Velocidad Y: ", -math.pi/8, self.textoVely, " UA/año")

    def incPuntos(self):
        self.modificarAtributo("puntos", "Puntos a graficar: ", 20, self.textoPuntos, format = False, puedeserNegativo=False)

    def decPuntos(self):
        self.modificarAtributo("puntos", "Puntos a graficar: ", -20, self.textoPuntos, format = False, puedeserNegativo=False)

    # Modificar características del planeta personalizado
    def modificarAtributo(self, keyAtributo, textoAtributo, valor, contenedorTexto, textoFinal="", format = True, puedeserNegativo = True, decimales = 4):
        if puedeserNegativo or not puedeserNegativo and self.plano.datosPersonalizado[keyAtributo] + valor >= 0:
            self.plano.datosPersonalizado[keyAtributo] += valor
        else:
            return

        if format:
            formato = "{:.%df}" % decimales

            textoValor = formato.format(self.plano.datosPersonalizado[keyAtributo])
        else:
            textoValor = str(self.plano.datosPersonalizado[keyAtributo])

        print(textoFinal)
        contenedorTexto.modificarTexto(textoAtributo + textoValor + textoFinal)

    def mercurio(self):
        self.plano.togglePlaneta(0)

    def venus(self):
        self.plano.togglePlaneta(1)

    def tierra(self):
        self.plano.togglePlaneta(2)

    def marte(self):
        self.plano.togglePlaneta(3)

    def jupiter(self):
        self.plano.togglePlaneta(4)

    def saturno(self):
        self.plano.togglePlaneta(5)

    def urano(self):
        self.plano.togglePlaneta(6)

    def neptuno(self):
        self.plano.togglePlaneta(7)

    def personalizado(self):
        self.plano.togglePlaneta(8)
        
    def defaultFunc(self):
        print("Boton siendo presionado")