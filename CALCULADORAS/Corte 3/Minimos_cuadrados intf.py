from cgitb import text
from tkinter import *
from tkinter.tix import COLUMN #libreria de GUI
import numpy as np
from sympy import *
from matplotlib import pyplot
counter = 0
r = 0
grado_T = []
CC_T = []
arrentries =  []
arrentries2 = []

#variables
def ajustarc(puntosX, puntosY, nPuntos):
    """nPuntos=int(input("Numero de puntos: "))
    puntosX=[] #coordenadas en x
    puntosY=[] #coordenadas en y"""
    
    listXi=[] #lista de las sumatorias de puntosX con exponente del 1 al 9 | para no usar 9 variables, cada posicion de la lista es una sumatoria
    Yi=0 #es una variable y no una lista porque es un solo numero
    listXiYi=[] #lista de las sumatorias de la multiplicacion de puntosX elevados a la n con Yi

    """for i in range(nPuntos):
        print("\n Punto",i,"\n")
        xnum=int(input("X: "))
        ynum=int(input("Y: "))
        puntosX.append(xnum)
        puntosY.append(ynum)"""

    def sumatoria(listas, expo):
        listasExp = [x**expo for x in listas]
        sumPuntos = sum(listasExp)
        return sumPuntos

    for x in range (0,12):
        listXi.append(sumatoria(puntosX, x+1)) #con esta lista se llena la matriz

    Yi = sumatoria(puntosY, 1) #Yi es la suma de todos los puntos en Y

    #hacer XiYi
    for n in range(0,6): 
        suma=0 #se reinicia suma | suma es sumatoria de Xi*Yi, Xi**2*Yi,...,Xi**n*Yi
        for m in range(0,nPuntos):
            suma+= (puntosX[m]**(n+1))*puntosY[m] #n+1 para que no se eleve a la cero | suma+= 
            #print("Suma en ",n,": ",suma)
        listXiYi.append(suma)
        #print("listXiYi: ",listXiYi[n])
        

    def multiplicacion(lista1,lista2):
        lista_multi = [a*b for a,b in zip(lista1, lista2)]
        return lista_multi

    def gaussJordan(matrizIgual,matriz1):
        m = len(matrizIgual)
        x = np.zeros(m)

        for k in range(0, m):
            for r in range(k+1, m):
                factor=(matriz1[r,k]/matriz1[k,k])
                matrizIgual[r]=matrizIgual[r]-(factor*matrizIgual[k])
                for c in range(0,m):
                    matriz1[r,c]=matriz1[r,c]-(factor*matriz1[k,c])

        x[m-1]=matrizIgual[m-1]/matriz1[m-1, m-1]

        for r in range(m-2, -1, -1):
            suma = 0
            for c in range(0,m):
                suma=suma+matriz1[r,c]*x[c]
            x[r]=(matrizIgual[r]-suma)/matriz1[r, r]  
        return x



    def casoLineal(): #Primer caso, grado 1
        matriz1=np.array([[nPuntos, listXi[0]], 
            [listXi[0], listXi[1]]
            ],dtype=np.float64) #2x2 | dtype es para que la matriz sea float

        matrizIgual=np.array([Yi,listXiYi[0]],dtype=np.float64) #es una lista a modo de vector, una sola fila

        final=gaussJordan(matrizIgual,matriz1)

        #respuesta=round(final[0],3)+"+"+round(final[1],3)+"x"
        #print(respuesta)
        respuestaG = Concat(final, 1)
        CoeCor(respuestaG, 0)

    def casoCuad():
        matriz1=np.array([[nPuntos, listXi[0], listXi[1]], 
            [listXi[0], listXi[1], listXi[2]], 
            [listXi[1], listXi[2], listXi[3]]
            ],dtype=np.float64) #3x3 | dtype es para que la matriz sea float
        
        matrizIgual=np.array([Yi,listXiYi[0], listXiYi[1]],dtype=np.float64) #es una lista a modo de vector, una sola fila

        final=gaussJordan(matrizIgual,matriz1)

        respuestaG = Concat(final, 2)
        CoeCor(respuestaG, 1)

    def casoCub():
        matriz1=np.array([[nPuntos, listXi[0], listXi[1], listXi[2]], 
            [listXi[0], listXi[1], listXi[2], listXi[3]], 
            [listXi[1], listXi[2], listXi[3], listXi[4]],
            [listXi[2], listXi[3], listXi[4], listXi[5]]
            ],dtype=np.float64) #4x4 | dtype es para que la matriz sea float

        matrizIgual=np.array([Yi,listXiYi[0], listXiYi[1], listXiYi[2]],dtype=np.float64) #es una lista a modo de vector, una sola fila

        final=gaussJordan(matrizIgual,matriz1)

        respuestaG = Concat(final, 3)
        CoeCor(respuestaG, 2)

    def caso4():
        matriz1=np.array([[nPuntos, listXi[0], listXi[1], listXi[2], listXi[3]], 
            [listXi[0], listXi[1], listXi[2], listXi[3], listXi[4]], 
            [listXi[1], listXi[2], listXi[3], listXi[4], listXi[5]],
            [listXi[2], listXi[3], listXi[4], listXi[5], listXi[6]],
            [listXi[3], listXi[4], listXi[5], listXi[6], listXi[7]]
            ],dtype=np.float64) #5x5 | dtype es para que la matriz sea float

        matrizIgual=np.array([Yi,listXiYi[0], listXiYi[1], listXiYi[2], listXiYi[3]],dtype=np.float64) #es una lista a modo de vector, una sola fila

        final=gaussJordan(matrizIgual,matriz1)

        respuestaG = Concat(final, 4)
        CoeCor(respuestaG, 3)

    def caso5():
        matriz1=np.array([[nPuntos, listXi[0], listXi[1], listXi[2], listXi[3], listXi[4]], 
            [listXi[0], listXi[1], listXi[2], listXi[3], listXi[4], listXi[5]], 
            [listXi[1], listXi[2], listXi[3], listXi[4], listXi[5], listXi[6]],
            [listXi[2], listXi[3], listXi[4], listXi[5], listXi[6], listXi[7]],
            [listXi[3], listXi[4], listXi[5], listXi[6], listXi[7], listXi[8]],
            [listXi[4], listXi[5], listXi[6], listXi[7], listXi[8], listXi[9]]
            ],dtype=np.float64) #6x6 | dtype es para que la matriz sea float

        matrizIgual=np.array([Yi,listXiYi[0], listXiYi[1], listXiYi[2], listXiYi[3], listXiYi[4]],dtype=np.float64) #es una lista a modo de vector, una sola fila

        final=gaussJordan(matrizIgual,matriz1)

        respuestaG = Concat(final, 5)
        CoeCor(respuestaG, 4)

    def caso6():
        matriz1=np.array([[nPuntos, listXi[0], listXi[1], listXi[2], listXi[3], listXi[4], listXi[5]], 
            [listXi[0], listXi[1], listXi[2], listXi[3], listXi[4], listXi[5], listXi[6]],
            [listXi[1], listXi[2], listXi[3], listXi[4], listXi[5], listXi[6], listXi[7]],
            [listXi[2], listXi[3], listXi[4], listXi[5], listXi[6], listXi[7], listXi[8]],
            [listXi[3], listXi[4], listXi[5], listXi[6], listXi[7], listXi[8], listXi[9]],
            [listXi[4], listXi[5], listXi[6], listXi[7], listXi[8], listXi[9], listXi[10]],
            [listXi[5], listXi[6], listXi[7], listXi[8], listXi[9], listXi[10], listXi[11]]
            ],dtype=np.float64) #7x7 | dtype es para que la matriz sea float

        matrizIgual=np.array([Yi,listXiYi[0], listXiYi[1], listXiYi[2], listXiYi[3], listXiYi[4], listXiYi[5]],dtype=np.float64) #es una lista a modo de vector, una sola fila

        final=gaussJordan(matrizIgual,matriz1)

        respuestaG = Concat(final, 6)
        CoeCor(respuestaG, 5)


    def Concat(final, grado): #print
        global r
        respuesta=''
        for x in range(0,grado+1):
            varFin = round(final[x],3)
            print("varFin: ",varFin)
            if(final[x]>=0 and x!=0): #si es positivo
                print("Entra if >=0")
                respuesta+="+"+str(varFin)+"*x**"+str(x)
            if(x==0): #si es el primer valor
                print("Entra if =0")
                respuesta+=str(varFin)
            if(final[x]<0 and x!=0): #si es negativo
                print("Entra if <0")
                respuesta+=str(varFin)+"*x**"+str(x)
        try:
            grado_T[r].insert(0, str(respuesta))
        except:
            grado_T[r].insert(0, ":(")
        r+=1

        return respuesta
            
    def CoeCor(respuestaG, grado):
        #asi se llamaran las incognitas para que sympy las entienda
        x = symbols ('x') 

        sumCC=0
        sumCC2=0
        promY = sum(puntosY)/nPuntos
        funcRes = parse_expr(respuestaG)

        for i in range(0, nPuntos):
            fxi = funcRes.subs(x, puntosX[i])
            print("AAAAAAAAAAAA", fxi)
            #fxi = fxi(puntosX[i])
            sumCC += (puntosY[i]-fxi)**2

        for j in range(0, nPuntos):
            sumCC2 += (puntosY[j]-promY)**2

        coeficiente = sqrt((sumCC2-sumCC)/sumCC2)
        print("Coeficiente Correlacion: ", round(coeficiente,6))
        CC_T[grado].insert(0, round(coeficiente,6))


    #--------------------EJECUCION---------------------------------------------
    casoLineal()
    casoCuad()
    casoCub()
    caso4()
    caso5()
    caso6()
    #print(sumatoria(puntosX,2))

#==============================================================================================================================================================================
#||||||||||||||||||||||||||||||||||||||||||||||O T R O|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#==============================================================================================================================================================================
def manage():
    global counter
    x = int(numeroPuntos_T.get())

    if counter == 0: 
        for i in range(x):

            arrentries.append(Entry(FrameV))
            arrentries2.append(Entry(FrameV))
            arrentries[i].grid(row=3, column=i, padx=2, pady=5)
            arrentries2[i].grid(row=4, column=i, padx=2, pady=5)
    else:
        puntosx = []
        puntosy = []
        for i in range(x):
            puntosx.append(float(arrentries[i].get()))
            puntosy.append(float(arrentries2[i].get()))
            
        ajustarc(puntosx, puntosy, x)
    counter += 1

#-------------------------------------------------------------------------------------------
#Zona para definir comandos.
def clearcomm():
    grado_T[0].delete("0","end")
    grado_T[1].delete("0","end")
    grado_T[2].delete("0","end")
    grado_T[3].delete("0","end")
    grado_T[4].delete("0","end")
    grado_T[5].delete("0","end")

    
#-------------------------------------------------------------------------------------------
#creacion de ventana principal.
Ventana = Tk()
Ventana.title("Ajuste por minimos cuadrados")
Ventana.config(bg="grey65")
Ventana.geometry("800x500")
Ventana.resizable(0,0) #bloqueo de tamaño.
#-------------------------------------------------------------------------------------------
#Creacion del frame.
FrameV=Frame()
FrameV.pack()
FrameV.config(bg="light grey") #color de fondo.

FrameV3=Frame()
FrameV3.pack()
FrameV3.config(bg="grey65") #color de fondo.

FrameV2=Frame()
FrameV2.pack()
FrameV2.config(bg="grey65") #color de fondo.

#-------------------------------------------------------------------------------------------
#Labels (etiquetas, todo lo que tenga "_L").
numeroPuntos_L=Label(FrameV, text="Numero de puntos")
numeroPuntos_L.grid(row=2, column=0, padx=10, pady=10)
numeroPuntos_L.config(bg="light grey") #color de fondo.

#Etiquetas grados
ejemplo_L=Label(FrameV3, text="Ajustes por grados f(x) = a₀+a₁x+a₂x²+a₃x³+...+aₙxⁿ0")
ejemplo_L.grid(row=12, column=0, padx=10, pady=10)
ejemplo_L.config(bg="grey65") #color de fondo.

grado1_L=Label(FrameV2, text="Grado 1:")
grado1_L.grid(row=3, column=0, padx=10, pady=10)
grado1_L.config(bg="grey65") #color de fondo.

grado2_L=Label(FrameV2, text="Grado 2:")
grado2_L.grid(row=4, column=0, padx=10, pady=10)
grado2_L.config(bg="grey65") #color de fondo.

grado3_L=Label(FrameV2, text="Grado 3:")
grado3_L.grid(row=5, column=0, padx=10, pady=10)
grado3_L.config(bg="grey65") #color de fondo.

grado4_L=Label(FrameV2, text="Grado 4:")
grado4_L.grid(row=6, column=0, padx=10, pady=10)
grado4_L.config(bg="grey65") #color de fondo.

grado5_L=Label(FrameV2, text="Grado 5:")
grado5_L.grid(row=7, column=0, padx=10, pady=10)
grado5_L.config(bg="grey65") #color de fondo.

grado6_L=Label(FrameV2, text="Grado 6:")
grado6_L.grid(row=8, column=0, padx=10, pady=10)
grado6_L.config(bg="grey65") #color de fondo.

#Etiquetas Coeficientes Correlacion
cc1_L=Label(FrameV2, text="C.C :")
cc1_L.grid(row=3, column=2, padx=10, pady=10)
cc1_L.config(bg="grey65") #color de fondo.

cc2_L=Label(FrameV2, text="C.C :")
cc2_L.grid(row=4, column=2, padx=10, pady=10)
cc2_L.config(bg="grey65") #color de fondo.

cc3_L=Label(FrameV2, text="C.C :")
cc3_L.grid(row=5, column=2, padx=10, pady=10)
cc3_L.config(bg="grey65") #color de fondo.

cc4_L=Label(FrameV2, text="C.C :")
cc4_L.grid(row=6, column=2, padx=10, pady=10)
cc4_L.config(bg="grey65") #color de fondo.

cc5_L=Label(FrameV2, text="C.C :")
cc5_L.grid(row=7, column=2, padx=10, pady=10)
cc5_L.config(bg="grey65") #color de fondo.

cc6_L=Label(FrameV2, text="C.C :")
cc6_L.grid(row=8, column=2, padx=10, pady=10)
cc6_L.config(bg="grey65") #color de fondo.

#-------------------------------------------------------------------------------------------
#Cajas de texto. ----------
numeroPuntos_T=Entry(FrameV)
numeroPuntos_T.grid(row=2, column=1, padx=10, pady=10)
numeroPuntos_T.config(justify="center")
#Outputs grados
grado_T.append(Entry(FrameV2, width=70))
grado_T[0].grid(row=3, column=1, padx=10, pady=10)
grado_T[0].config(justify="center")

grado_T.append(Entry(FrameV2, width=70))
grado_T[1].grid(row=4, column=1, padx=10, pady=10)
grado_T[1].config(justify="center")

grado_T.append(Entry(FrameV2, width=70))
grado_T[2].grid(row=5, column=1, padx=10, pady=10)
grado_T[2].config(justify="center")

grado_T.append(Entry(FrameV2, width=70))
grado_T[3].grid(row=6, column=1, padx=10, pady=10)
grado_T[3].config(justify="center")

grado_T.append(Entry(FrameV2, width=70))
grado_T[4].grid(row=7, column=1, padx=10, pady=10)
grado_T[4].config(justify="center")

grado_T.append(Entry(FrameV2, width=70))
grado_T[5].grid(row=8, column=1, padx=10, pady=10)
grado_T[5].config(justify="center")

#Outputs Coeficiente Correlacion | tienen que estar alineados con sus grados
CC_T.append(Entry(FrameV2, width=15))
CC_T[0].grid(row=3, column=3, padx=10, pady=10)

CC_T.append(Entry(FrameV2, width=15))
CC_T[1].grid(row=4, column=3, padx=10, pady=10)

CC_T.append(Entry(FrameV2, width=15))
CC_T[2].grid(row=5, column=3, padx=10, pady=10)

CC_T.append(Entry(FrameV2, width=15))
CC_T[3].grid(row=6, column=3, padx=10, pady=10)

CC_T.append(Entry(FrameV2, width=15))
CC_T[4].grid(row=7, column=3, padx=10, pady=10)

CC_T.append(Entry(FrameV2, width=15))
CC_T[5].grid(row=8, column=3, padx=10, pady=10)

#-------------------------------------------------------------------------------------------
#Botones.
BorrarB=Button(FrameV, text="Borrar", command=clearcomm)
BorrarB.grid(row=11, column=0, pady=10)

CalcularB=Button(FrameV, text="Calcular", command=manage)
CalcularB.grid(row=11, column=1, pady=10, padx=10)

SalirB=Button(FrameV, text="Salir", command=Ventana.destroy)
SalirB.grid(row=11, column=2, pady=10, padx=10)
#-------------------------------------------------------------------------------------------
Ventana.mainloop() #es el ciclo para que la ventana "exista"