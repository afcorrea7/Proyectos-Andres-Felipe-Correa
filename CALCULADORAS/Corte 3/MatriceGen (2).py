from cProfile import label
from cgitb import text
import numpy as np
from tkinter import *

inp = []
txtv = []
txta = []
lb1 = []
lb2 = []
res = []
res2 = []
matrice = []
matrice2 = []

#Funciones de operaciones ---------------------------------------------------------------------------------
def SaveMT():
   
    x = int(FilaM_T.get())
    y = int(ColumnM_T.get())
    x1 = int(FilaM_T2.get())
    y1 = int(ColumnM_T2.get())

    for i in range(x):
        matrice.append([])
        for j in range(y):
            try:
                matrice[i].append(float(inp[i][j].get()))
            except:
                pass

    for i in range(x1):
        matrice2.append([])
        for j in range(y1):
            try:
                matrice2[i].append(float(res[i][j].get()))
            except:
                pass            
    
    print(matrice)
    print(matrice2)

def Suma():
    if len(matrice) == len(matrice2) and len(matrice[0]) == len(matrice2[0]):

        matrizResul = []
        for i in range(len(matrice)):
            matrizResul.append([])
            for j in range(len(matrice[0])):
                matrizResul[i].append(matrice[i][j] + matrice2[i] [j])

        print("\nResultado:\n")
        for fila in matrizResul :
            print("[", end=" ")
            for elemento in fila:
                print("{}".format(elemento), end=" ")
            print("]")
        print(len(matrizResul[0]))
        print(len(matrizResul))
        ansgen(int(len(matrizResul)), len(matrizResul[0]), matrizResul)
    else:
        print("No se puede operar")

def Resta():
    if (len(matrice)==len(matrice2) and len(matrice[0])==len(matrice2[0])):
        matrizResul=[]

        for t in range (len(matrice)):
            matrizResul.append([])
            for m in range (len(matrice[0])):
                matrizResul[t].append(matrice[t][m]-matrice2[t][m])
        
        print("\nResultado:\n")
        for fila in matrizResul :
            print("[", end=" ")
            for elemento in fila:
                print("{}".format(elemento), end=" ")
            print("]")
        print(len(matrizResul[0]))
        print(len(matrizResul))
        ansgen(int(len(matrizResul)), len(matrizResul[0]), matrizResul)
        
    else:
        print("No se puede operar")

def Multi():
    matrizResul=[]
    #crear matriz vacia matrizResul
    for i in range(len(matrice)): #que tenga el numero de filas de matriz1
            matrizResul.append([])
            for l in range(len(matrice2[0])): #y el numero de columnas de matriz2
                matrizResul[i].append(0)

    if(len(matrice[0])==len(matrice2)): #Solo multiplicar cuando el num de columnas de matriz1 sea el mismo que el num de filas de matriz2
        #Recorre los indices de las matrices 1 y 2 para llenar matrizFin 
        for n in range(len(matrice)):
            for m in range(len(matrice2[0])): 
                for o in range(len(matrice[0])):
                    matrizResul[n][m] += matrice[n][o]*matrice2[o][m]

        print(len(matrizResul[0]))
        print(len(matrizResul))
        ansgen(int(len(matrizResul)), len(matrizResul[0]), matrizResul)
    else:
        print("las columnas de la matriz 1 no encajan con las filas de la matriz 2.")

def Escalar():
    matrizResul=[]
    for i in range (len(matrice)): #crear matrizResul vacia con la misma longitud de matrice
        matrizResul.append([0]*len(matrice[0]))
    for i in range (len(matrice)):
        for j in range (len(matrice[0])):
            matrizResul[i][j]=matrice[i][j]*(matrice2[0][0])

    print("\nResultado:\n")
    for fila in matrizResul :
        print("[", end=" ")
        for elemento in fila:
            print("{}".format(elemento), end=" ")
        print("]")
    ansgen(int(len(matrizResul)), len(matrizResul[0]), matrizResul)

def Inversa():
    matrizResul=[]
    matrizResul = np.linalg.inv(matrice)
    print("\nResultado:\n")
    for fila in matrizResul :
        print("[", end=" ")
        for elemento in fila:
            print("{}".format(elemento), end=" ")
        print("]")
    print(len(matrizResul[0]))
    print(len(matrizResul))
    ansgen(int(len(matrizResul)), len(matrizResul[0]), matrizResul)


def Transpuesta():
    transp=[]

    for x in range (len(matrice[0])):
        transp.append([])
        for y in range (len(matrice)):
            transp[x].append(matrice[y][x])

    print("\nMatriz original:\n")
    for fila in matrice :
        print("[", end=" ")
        for elemento in fila:
            print("{}".format(elemento), end=" ")
        print("]")

    print("\nResultado:\n")
    for fila in transp :
        print("[", end=" ")
        for elemento in fila:
            print("{}".format(elemento), end=" ")
        print("]")

def Gauss():
    m = len(matrice2[0])
    x = np.zeros(m)
    if(len(matrice2)==1 and len(matrice2[0])==len(matrice)): #El vector debe tener el mismo num de columnas que el num de filas de m1
        for k in range(0, m):
            for r in range(k+1, m):
                factor=(matrice[r][k]/matrice[k][k])
                matrice2[0][r]=matrice2[0][r]-(factor*matrice2[0][k])
                for c in range(0,m):
                    matrice[r][c]=matrice[r][c]-(factor*matrice[k][c])

        x[m-1]=(matrice2[0][m-1])/(matrice[m-1][m-1])

        for r in range(m-2, -1, -1):
            suma = 0
            for c in range(0,m):
                suma=suma+matrice[r][c]*x[c]
            x[r]=(matrice2[0][r]-suma)/matrice[r][r] 
            
        print(x)

        #for fila in x:
            #matrizResul.append(x[fila])
        matrizResul = Label(FrameAbajo2, text=str(x), bg="light gray") #No encontré como llamarlo con ansgen porque sacaba error x has no len()
        matrizResul.grid(row=3, column=4, padx=10, pady=10)
        #ansgen(int(len(matrizResul)), len(matrizResul), matrizResul) 
    else:
        print("No se puede realizar GJ,numero de columnas en M1 erroneo o M2 debe ser un vector (solo una fila)")

def Deter():
    matrizResul=[]
    matrizResul = np.linalg.det(matrice)
    print("\nResultado:\n")
    for fila in matrizResul :
        print("[", end=" ")
        for elemento in fila:
            print("{}".format(elemento), end=" ")
        print("]")
    print(len(matrizResul[0]))
    print(len(matrizResul))
    ansgen(int(len(matrizResul)), len(matrizResul[0]), matrizResul)

#Ventana Operaciones---------------------------------------------------------------------------------------
def fgen():
    #Matrix 1----------------------------------------------------------------------
    x = int(FilaM_T.get())
    y = int(ColumnM_T.get())
    val = 0
    for i in range(x+1):        
        for j in range(y+1):
            if (i == 0 or j == 0) and not(i == 0 and j == 0):
                if i == 0:
                    lb1.append(Label(FrameAbajo, text="col " + str(j), bg="gray"))
                    lb1[val].grid(row=i+1, column=j+1, padx=10, pady=10)
                    val+=1
                if j == 0:
                    lb1.append(Label(FrameAbajo, text="fila " + str(i), bg="gray"))
                    lb1[val].grid(row=i+1, column=j+1, padx=10, pady=10)
                    val+=1
            elif i == 0 and j == 0:
                    lb1.append(Label(FrameAbajo, text=" ... ", bg="gray"))
                    lb1[val].grid(row=i+1, column=j+1, padx=10, pady=10)
                    val+=1
    
    for i in range(x):
        txtv.append([])
        inp.append([])
        for j in range(y):
            txtv[i].append(StringVar)
            inp[i].append(Entry(FrameAbajo, textvariable=txtv[i][j]))
            inp[i][j].grid(row=i+2, column=j+2, padx=10, pady=10)
    

    #Matrix 2----------------------------------------------------------------------
    x1 = int(FilaM_T2.get())
    y1 = int(ColumnM_T2.get())
    val = 0
    for i in range(x1+1):        
        for j in range(y1+1):
            if (i == 0 or j == 0) and not(i == 0 and j == 0):
                if i == 0:
                    lb2.append(Label(FrameAbajo, text="col " + str(j),  bg="gray"))
                    lb2[val].grid(row=i+1, column=y+j+4, padx=10, pady=10)
                    val+=1
                if j == 0:
                    lb2.append(Label(FrameAbajo, text="fila " + str(i), bg="gray"))
                    lb2[val].grid(row=i+1, column=y+j+4, padx=10, pady=10)
                    val+=1
            elif i == 0 and j == 0:
                    lb2.append(Label(FrameAbajo, text=" ... ", bg="gray"))
                    lb2[val].grid(row=i+1, column=y+j+4, padx=10, pady=10)
                    val+=1
    for i in range(x1):
        txta.append([])
        res.append([])

        for j in range(y1):
            txta[i].append(StringVar)
            res[i].append(Entry(FrameAbajo, textvariable=txta[i][j]))
            res[i][j].grid(row=i+2, column=y+j+5, padx=10, pady=10)

def ansgen(x, y, v):
    res2 
    for i in range(x):
        res2.append([])

        for j in range(y):
            res2[i].append(Label(FrameAbajo2, text=str(v[i][j]), bg="light gray"))
            res2[i][j].grid(row=i+1, column=j+1, padx=10, pady=10)


#-------------------------------------------------------------------------------------------
#Zona para definir comandos.
def clearcomm():
    FilaM_T.delete("0", "end")
    ColumnM_T.delete("0","end")
    FilaM_T2.delete("0", "end")
    ColumnM_T2.delete("0","end")
    for i in range(len(res2)):
        for j in range(len(res2[0])):
            res2[i][j].config(text="")


  
#-------------------------------------------------------------------------------------------
#creacion de ventana principal.  
Ventana = Tk()
Ventana.title("Matrix")
Ventana.config(bg="light grey")

#Ventana.resizable(0,0)
#-------------------------------------------------------------------------------------------
#Creacion del frame.
FrameV=Frame()
FrameV.pack()
FrameV.config(bg="light grey")

FrameAbajo = Frame()
FrameAbajo.pack()
FrameAbajo.config(bg="gray")

FrameAbajo2 = Frame()
FrameAbajo2.pack()
FrameAbajo2.config(bg="light gray")
#-------------------------------------------------------------------------------------------
#Etiquetas
FilaM = Label(FrameV, text="Numero de filas matrix")
FilaM.grid(row=1, column=0, padx=10, pady=10)
FilaM.config(bg="light grey")

ColumnM = Label(FrameV, text="Numero de columnas matrix")
ColumnM.grid(row=2, column=0, padx=10, pady=10)
ColumnM.config(bg="light grey")

FilaM2 = Label(FrameV, text="Numero de filas matrix 2")
FilaM2.grid(row=3, column=0, padx=10, pady=10)
FilaM2.config(bg="light grey")

ColumnM2 = Label(FrameV, text="Numero de columnas matrix 2")
ColumnM2.grid(row=4, column=0, padx=10, pady=10)
ColumnM2.config(bg="light grey")
#-------------------------------------------------------------------------------------------
#Cajas de texto
FilaM_T = Entry(FrameV)
FilaM_T.grid(row=1, column=1, padx=10, pady=10)
FilaM_T.config(justify="center")

ColumnM_T = Entry(FrameV)
ColumnM_T.grid(row=2, column=1, padx=10, pady=10)
ColumnM_T.config(justify="center")

FilaM_T2 = Entry(FrameV)
FilaM_T2.grid(row=3, column=1, padx=10, pady=10)
FilaM_T2.config(justify="center")

ColumnM_T2 = Entry(FrameV)
ColumnM_T2.grid(row=4, column=1, padx=10, pady=10)
ColumnM_T2.config(justify="center")

#Botones
calcular = Button(FrameV, text="Crear", command=fgen)
calcular.grid(row=7, column=1, padx=10, pady=10)

Salir = Button(FrameV, text="Salir", command=Ventana.destroy)
Salir.grid(row=7, column=2, padx=10, pady=10)

Borrar = Button(FrameV, text="Borrar", command=clearcomm)
Borrar.grid(row=7, column=0, padx=10, pady=10)
#-------------------------------------------------------------------------------------------
#Botones Operaciones

bt1 = Button(FrameV, text="Sumar", command=Suma)
bt1.grid(row=1, column=4, padx=10, pady=10)

bt2 = Button(FrameV, text="Restar", command=Resta)
bt2.grid(row=1, column=5, padx=10, pady=10)

bt3 = Button(FrameV, text="Multiplicar", command=Multi)
bt3.grid(row=2, column=4, padx=10, pady=10)

bt4 = Button(FrameV, text="Por Escalar M1", command=Escalar)
bt4.grid(row=2, column=5, padx=10, pady=10)

bt5 = Button(FrameV, text="Inversa M1", command=Inversa)
bt5.grid(row=3, column=4, padx=10, pady=10)

bt6 = Button(FrameV, text="Transpuesta M1", command=Transpuesta)
bt6.grid(row=3, column=5, padx=10, pady=10)

bt7 = Button(FrameV, text="Gauss-Jordan", command=Gauss)
bt7.grid(row=4, column=4, padx=10, pady=10)

bt8 = Button(FrameV, text="Determinante", command=Deter)
bt8.grid(row=4, column=5, padx=10, pady=10)

bt = Button(FrameV, text="Guardar", command=SaveMT)
bt.grid(row=5, column=4, padx=10, pady=10)
#-------------------------------------------------------------------------------------------
Ventana.mainloop()