import numpy as np
from sympy import *
from matplotlib import pyplot
#variables
nPuntos=int(input("Numero de puntos: "))
puntosX=[] #coordenadas en x
puntosY=[] #coordenadas en y
listXi=[] #lista de las sumatorias de puntosX con exponente del 1 al 9 | para no usar 9 variables, cada posicion de la lista es una sumatoria
Yi=0 #es una variable y no una lista porque es un solo numero
listXiYi=[] #lista de las sumatorias de la multiplicacion de puntosX elevados a la n con Yi

for i in range(nPuntos):
    print("\n Punto",i,"\n")
    xnum=int(input("X: "))
    ynum=int(input("Y: "))
    puntosX.append(xnum)
    puntosY.append(ynum)

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
    Concat(final, 1)

def casoCuad():
    matriz1=np.array([[nPuntos, listXi[0], listXi[1]], 
        [listXi[0], listXi[1], listXi[2]], 
        [listXi[1], listXi[2], listXi[3]]
        ],dtype=np.float64) #3x3 | dtype es para que la matriz sea float
    
    matrizIgual=np.array([Yi,listXiYi[0], listXiYi[1]],dtype=np.float64) #es una lista a modo de vector, una sola fila

    final=gaussJordan(matrizIgual,matriz1)

    Concat(final, 2)

def casoCub():
    matriz1=np.array([[nPuntos, listXi[0], listXi[1], listXi[2]], 
        [listXi[0], listXi[1], listXi[2], listXi[3]], 
        [listXi[1], listXi[2], listXi[3], listXi[4]],
        [listXi[2], listXi[3], listXi[4], listXi[5]]
        ],dtype=np.float64) #4x4 | dtype es para que la matriz sea float

    matrizIgual=np.array([Yi,listXiYi[0], listXiYi[1], listXiYi[2]],dtype=np.float64) #es una lista a modo de vector, una sola fila

    final=gaussJordan(matrizIgual,matriz1)

    Concat(final, 3)

def caso4():
    matriz1=np.array([[nPuntos, listXi[0], listXi[1], listXi[2], listXi[3]], 
        [listXi[0], listXi[1], listXi[2], listXi[3], listXi[4]], 
        [listXi[1], listXi[2], listXi[3], listXi[4], listXi[5]],
        [listXi[2], listXi[3], listXi[4], listXi[5], listXi[6]],
        [listXi[3], listXi[4], listXi[5], listXi[6], listXi[7]]
        ],dtype=np.float64) #5x5 | dtype es para que la matriz sea float

    matrizIgual=np.array([Yi,listXiYi[0], listXiYi[1], listXiYi[2], listXiYi[3]],dtype=np.float64) #es una lista a modo de vector, una sola fila

    final=gaussJordan(matrizIgual,matriz1)

    Concat(final, 4)

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

    Concat(final, 5)

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

    Concat(final, 6)



def Concat(final, grado): #print
    respuesta=''

    for x in range(0,grado+1):
        varFin = round(final[x],3)
        print("varFin: ",varFin)
        if(final[x]>=0 and x!=0): #si es positivo
            respuesta+=" + "+str(varFin)+"x^"+str(x)
        if(x==0): #si es el primer valor
            respuesta+=str(varFin)
        if(final[x]<0 and x!=0): #si es negativo
            respuesta+=str(varFin)+"x^"+str(x)
    print(respuesta)
        
#--------------------EJECUCION---------------------------------------------
casoLineal()
casoCuad()
casoCub()
caso4()
caso5()
caso6()
#print(sumatoria(puntosX,2))