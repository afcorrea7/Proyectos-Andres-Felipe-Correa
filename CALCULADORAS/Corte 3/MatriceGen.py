import numpy as np
from tkinter import *
from matplotlib import pyplot

inp = []
txtv = []
txta = []
res = []
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
    pass

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
        return matrizResul
    else:
        print("No se puede operar")

def Multi():
    pass

def Escalar():
    pass

def Inversa():
    pass 

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
    
#Ventana Operaciones---------------------------------------------------------------------------------------
def fgen():
    Matrices = Tk()
    Matrices.title("jiji")
    x = int(FilaM_T.get())
    y = int(ColumnM_T.get())

    for i in range(x):
        txtv.append([])
        inp.append([])

        for j in range(y):
            txtv[i].append(StringVar)
            inp[i].append(Entry(Matrices, textvariable=txtv[i][j]))
            inp[i][j].grid(row=i+1, column=j+1, padx=10, pady=10)

    #botones----------------------------------------------------------------------
    bt = Button(Matrices, text="guardar", command=SaveMT)
    bt.grid(row=round((i+2)/2), column=j+2,padx=10, pady=10)

    bt1 = Button(Matrices, text="sumar", command=Suma)
    bt1.grid(row=round((i+2)/2)+1, column=j+2,padx=10, pady=10)

    bt2 = Button(Matrices, text="restar", command=Resta)
    bt2.grid(row=round((i+2)/2)+2, column=j+2,padx=10, pady=10)

    bt3 = Button(Matrices, text="multiplicar", command=Multi)
    bt3.grid(row=round((i+2)/2)+3, column=j+2,padx=10, pady=10) 

    bt4 = Button(Matrices, text="por escalar m1", command=Escalar)
    bt4.grid(row=round((i+2)/2)+4, column=j+2,padx=10, pady=10)
    
    In_Esc = Entry(Matrices, width=4)
    In_Esc.grid(row=round((i+2)/2)+4, column=j+3, padx=10, pady=10)

    bt5 = Button(Matrices, text="inversa m1", command=Inversa)
    bt5.grid(row=round((i+2)/2)+5, column=j+2,padx=10, pady=10)

    bt6 = Button(Matrices, text="transpuesta m1", command=Transpuesta)
    bt6.grid(row=round((i+2)/2)+6, column=j+2,padx=10, pady=10)

    x1 = int(FilaM_T2.get())
    y1 = int(ColumnM_T2.get())

    for i in range(x1):
        txta.append([])
        res.append([])

        for j in range(y1):
            txta[i].append(StringVar)
            res[i].append(Entry(Matrices, textvariable=txta[i][j]))
            res[i][j].grid(row=i+1, column=y+j+3, padx=10, pady=10)



#-------------------------------------------------------------------------------------------
#Zona para definir comandos.
def clearcomm():
    FilaM_T.delete("0", "end")
    ColumnM_T.delete("0","end")
  
#-------------------------------------------------------------------------------------------
#creacion de ventana principal.  
Ventana = Tk()
Ventana.title("Matrix")

#Ventana.resizable(0,0)
#-------------------------------------------------------------------------------------------
#Creacion del frame.
FrameV=Frame()
FrameV.pack()
FrameV.config(bg="light grey")
#-------------------------------------------------------------------------------------------
#Etiquetas
FilaM = Label(FrameV, text="Filas matrix")
FilaM.grid(row=1, column=0, padx=10, pady=10)
FilaM.config(bg="light grey")

ColumnM = Label(FrameV, text="Columnas matrix")
ColumnM.grid(row=2, column=0, padx=10, pady=10)
ColumnM.config(bg="light grey")

FilaM2 = Label(FrameV, text="Filas matrix 2")
FilaM2.grid(row=3, column=0, padx=10, pady=10)
FilaM2.config(bg="light grey")

ColumnM2 = Label(FrameV, text="Columnas matrix 2")
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
#-------------------------------------------------------------------------------------------
#Botones
calcular = Button(FrameV, text="Calcular", command=fgen)
calcular.grid(row=7, column=1, padx=10, pady=10)

Salir = Button(FrameV, text="Salir", command=Ventana.destroy)
Salir.grid(row=7, column=2, padx=10, pady=10)

Borrar = Button(FrameV, text="Borrar", command=clearcomm)
Borrar.grid(row=7, column=0, padx=10, pady=10)
#-------------------------------------------------------------------------------------------
Ventana.mainloop()