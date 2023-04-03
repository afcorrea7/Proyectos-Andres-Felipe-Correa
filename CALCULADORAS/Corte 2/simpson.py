
from sympy import *
import random
from random import uniform
from tkinter import *
from matplotlib import pyplot

def Multiplo2(partinum):
    if(partinum%2==1):
        partinum+=1 #Si el residuo es 1 sumale 2 a partinum
        print("numero de particiones ajustado a: ",partinum)

    return partinum

def simp(fx,a,b,partinum):
    jmas = 0
    areasucesion= 0
    listaFX=[]
    suma2=0
    suma=0
    sumaloka=0

    h= (b-a)/partinum
    expr=parse_expr(fx)
    x= symbols ('x')

    for n in range(0,partinum+1,1): #Empieza desde 0, con el +1 el rango no excluye a partinum 
            
        jmas = a+(h*n)
        areasucesion=(expr.subs(x,jmas))
        listaFX.append(areasucesion)
        print("ariasus:", areasucesion)
        
    for u in range(1,partinum,1):
        if(u%2==0):
            sumaloka+=2*(listaFX[u]) 
            print("par:", sumaloka) 
        else:
            suma+=4*(listaFX[u]) 
            print("Impar:", suma)
    
    suma2=listaFX[0]+listaFX[partinum]
    
    area=(h/3)*(suma2+suma+sumaloka)
    print("Integral:", area)
    return area
    
def CalcuError(ecua, aVal, bVal,parti): #Calcula el error
    x= symbols ('x')
    expr = parse_expr(ecua)
    deriv = diff(expr, x, 4) #funcion, qué variable, hasta qué derivada

    h = (bVal-aVal)/parti

    aleatorio = random.uniform(aVal,bVal)
    derivAleatorio = deriv.subs(x, aleatorio) #evalua f(x) donde f(x) es la cuarta derivada y x es random

    errorSimp = ((h**5)/90)*derivAleatorio

    return errorSimp

"""bucle=1
while bucle==1:
    print("| -------------- INTEGRACION NUMERICA POR SIMPSON 3/8 -------------- |")

    #asignacion de valores a variables
    ecuacion = input("Ingrese una funcion en terminos de x: ")
    aVal = float(input("Ingrese un valor para a: ")) 
    bVal = float(input("Ingrese otro valor para b: "))
    partinum = int(input("Ingrese el número de particiones: ")) #El usuario debe darlo

    nuevopartinum = Multiplo2(partinum) #Asegura que el numero de particiones ingresadas sea multiplo de 3

    simp(ecuacion,aVal,bVal,nuevopartinum)

    print("El error de este metodo esta vez es de: ",CalcuError(ecuacion,aVal,bVal))

    bucle = int(input("Deseas repetir el metodo?\n 1.Si\n 0.No\n"))"""


def calcall():
    ec = ecX.get()
    vala = aVal.get()
    valb = bVal.get()
    pt = Multiplo2(int(ptNo.get()))
    vala = float(vala)
    valb = float(valb)
    pt = int(pt)
    
    anLp.configure(text=pt)
    anLI.configure(text=simp(ec,vala,valb,pt))
    anLM.configure(text=CalcuError(ec,vala,valb,pt))

def grafica():
  x=symbols('x')
  z=0
  funcion=parse_expr(ecX.get())
  valX=[]
  valY=[]
  ini=0
  lim=30
  for i in range (ini*10,(lim*10)+1,1):
    val=i/10
    z=-1*(-1*(val)+15)
    valX.append(z)
    result=lambdify(x,funcion)
    result=result(z)
    valY.append(result)

  print("funcion",funcion)  
  pyplot.plot(valX,valY)
   
  # Establecer el color de los ejes.
  pyplot.axhline(0, color="black")
  pyplot.axvline(0, color="black")
  # Limitar los valores de los ejes.
  pyplot.xlim(-15, 15)
  pyplot.ylim(-15, 15)
  # Mostrarlo.
  pyplot.show()

#cmd------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#Zona para definir comandos.
def clearcomm():
    ecX.delete("0", "end")
    aVal.delete("0","end")
    bVal.delete("0","end")
    ptNo.delete("0","end")
    anLI.configure(text="")
    anLM.configure(text="")
    anLp.configure(text="")

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

lbp = Label(mFrame, text="Número de particiones ajustado a: ")
lbp.grid(row=4, column=0, padx=10, pady=10)
lbp.config(bg="light grey")

lb5 = Label(mFrame, text="Integral: ")
lb5.grid(row=5, column=0, padx=10, pady=10)
lb5.config(bg="light grey")

lb6 = Label(mFrame, text="Error: ")
lb6.grid(row=6, column=0, padx=10, pady=10)
lb6.config(bg="light grey")

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
anLp = Label(mFrame)
anLp.grid(row=4, column=1, padx=10, pady=10)
anLp.config(bg="light grey") 

anLI = Label(mFrame)
anLI.grid(row=5, column=1, padx=10, pady=10)
anLI.config(bg="light grey") 

anLM = Label(mFrame)
anLM.grid(row=6, column=1, padx=10, pady=10)
anLM.config(bg="light grey") 


#Button----------------------------------------------------------------------------------------------------
fn = Button(mFrame, text="calcular", command=calcall)
fn.grid(row=7, column=0, padx=10,pady=10)

Borrar = Button(mFrame, text="Borrar", command=clearcomm)
Borrar.grid(row=7, column=1, padx=10, pady=10)

Graficar = Button(mFrame, text="Graficar", command=grafica)
Graficar.grid(row=7, column=2, padx=10, pady=10)

Salir = Button(mFrame, text="Salir", command=Main.destroy)
Salir.grid(row=8, column=1, padx=10, pady=10)
#----------------------------------------------------------------------------------------------------------
Main.mainloop()