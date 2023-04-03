from sympy import *
import numpy as np
import scipy as sp
from tkinter import *

x = symbols('x')


def derecha(fx,a,b,n):
 
    deltax=(b-a)/n
    suma=0
    funcionDev=parse_expr(fx) #pasa de string a una ecuación 
    x=symbols('x')

    #calcular los puntos medios de cada intervalo
    for i in range (n):
        if i==0:
            x1=a
        else:
            x1=x2
        x2=x1+deltax

        suma+=funcionDev.subs(x,x2)
        integr=deltax*suma

    print(integr)
    return integr


def Izquierdos(ecuacion,aVal,bVal,partinum):
    area=0
    juno=0

    expr = parse_expr(ecuacion)
    print("ecuacion: ",expr)
    
    #Delta x
    deltaX = (bVal-aVal)/partinum
    print("deltaX: ",deltaX)

    #area
    for n in range(partinum):
        print(n)
        if(n==0):
            j=aVal
        else:
            juno = deltaX + j
            j = juno

        area += expr.subs(x, j)
        print("area ahora mismo: ",area)

    #final
    areaFin = area*deltaX
    print("Punto Extremo Izquierdo: ", areaFin)
    return areaFin


def puntoMedio(fx,a,b,n):

    deltax=(b-a)/n
    suma=0
    funcionDev=parse_expr(fx) #pasa de string a una ecuación 
    x=symbols('x')
    x1=0
    #calcular los puntos medios de cada intervalo
    for i in range (0,n,1):

        if i==0:
            xo=a
        else:
            xo=x1
        x1=xo+deltax

        medio=(xo+x1)/2

        suma+=funcionDev.subs(x,medio)
        integr=deltax*suma

    print("El valor en punto medio es :",integr)
    return integr
    

"""bucle=1
while bucle==1:
    print("| --------------INTEGRACION NUMERICA PUNTO MEDIO-------------- |")

    #asignacion de valores a variables
    ecuacion = input("Ingrese una funcion en terminos de x: ")
    aVal = float(input("Ingrese un valor para a: ")) 
    bVal = float(input("Ingrese otro valor para b: "))
    partinum = int(input("Ingrese el número de particiones: ")) #El usuario debe darlo

    puntoMedio(ecuacion,aVal,bVal,partinum)

    bucle = int(input("Deseas repetir el metodo?\n 1.Si\n 0.No\n"))"""

def calcall():
    ec = ecX.get()
    vala = aVal.get()
    valb = bVal.get()
    pt = ptNo.get()
    vala = float(vala)
    valb = float(valb)
    pt = int(pt)

    anLI.configure(text=Izquierdos(ec,vala,valb,pt))
    anLM.configure(text=puntoMedio(ec,vala,valb,pt))
    anLD.configure(text=derecha(ec,vala,valb,pt))

#cmd------------------------------------------------------------------------------------------------------


#maincanv-------------------------------------------------------------------------------------------------
Main = Tk()
Main.title("Calculadora")
Main.resizable(0,0)
#FrmCr----------------------------------------------------------------------------------------------------
mFrame = Frame()
mFrame.pack()
mFrame.config(bg= "light grey")
#Label----------------------------------------------------------------------------------------------------
lb1 = Label(mFrame, text="Ecuación en x: ")
lb1.grid(row=0, column=0, padx=10, pady=10)
lb1.config(bg="light grey", )

lb2 = Label(mFrame, text="Valor para a: ")
lb2.grid(row=1, column=0, padx=10, pady=10)
lb2.config(bg="light grey", )

lb3 = Label(mFrame, text="Valor para b: ")
lb3.grid(row=2, column=0, padx=10, pady=10)
lb3.config(bg="light grey", )

lb4 = Label(mFrame, text="Número de particiones: ")
lb4.grid(row=3, column=0, padx=10, pady=10)
lb4.config(bg="light grey")

lb5 = Label(mFrame, text="Izquierda: ")
lb5.grid(row=4, column=0, padx=10, pady=10)
lb5.config(bg="light grey")

lb6 = Label(mFrame, text="Medio: ")
lb6.grid(row=5, column=0, padx=10, pady=10)
lb6.config(bg="light grey")

lb7 = Label(mFrame, text="Derecha: ")
lb7.grid(row=6, column=0, padx=10, pady=10)
lb7.config(bg="light grey")
#Input----------------------------------------------------------------------------------------------------
ecX = Entry(mFrame)
ecX.grid(row=0,column=1,padx=10,pady=10)

aVal = Entry(mFrame)
aVal.grid(row=1,column=1,padx=10,pady=10)

bVal = Entry(mFrame)
bVal.grid(row=2,column=1,padx=10,pady=10)

ptNo = Entry(mFrame)
ptNo.grid(row=3,column=1,padx=10,pady=10)
#Answer---------------------------------------------------------------------------------------------------
anLI = Label(mFrame)
anLI.grid(row=4, column=1, padx=10, pady=10)
anLI.config(bg="light grey") 

anLM = Label(mFrame)
anLM.grid(row=5, column=1, padx=10, pady=10)
anLM.config(bg="light grey") 

anLD = Label(mFrame)
anLD.grid(row=6, column=1, padx=10, pady=10)
anLD.config(bg="light grey") 
#Button----------------------------------------------------------------------------------------------------
fn = Button(mFrame, text="calcular", command=calcall)
fn.grid(row=7, column=0, padx=10,pady=10)
Main.mainloop()