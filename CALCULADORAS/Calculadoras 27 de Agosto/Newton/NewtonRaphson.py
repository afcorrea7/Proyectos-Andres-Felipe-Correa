import sympy 
from sympy import *
from tkinter import * #libreria de GUI
import numpy as np
bucle = 1
x=symbols('x')

def process():
    fx = FuncionX.get()
    xval = PuntoX.get()
    xval = float(xval)
    errate = ErrorT.get()
    errate = float(errate)
    NewtonR(fx, xval, errate)

def NewtonR(funcion,xo,errorT):
    ite = 0
    errorR=1000 #se inicia la variable con un numero alto para que el while pueda funcionar

    while errorR>errorT and ite<50: #el bucle funciona mientras el errorR sea mayor al errorT y la iteracion sea menos a 50

        if (ite>0):
            xo=x1

        funcionDev=parse_expr(funcion) #pasa de string a una ecuación 
        
        derFuncion= funcionDev.diff(x) #hace la derivada de la funcion ya convertida.

        funcionNum=funcionDev.subs(x,xo)  #reemplaza xo en la funcion
        derFuncionNum=derFuncion.subs(x,xo) #reemplaza xo en el resultado de la derivada

        x1=xo-(funcionNum/derFuncionNum) #calculo de x1

        errorR=abs((x1-xo)/x1) #calculo del error relativo

        if(errorR<errorT): #comparación que servirá para determinar la raíz
            #print("El error relativo ",errorR," es menor al error de tolerancia ",errorT) #paso 8        
            print("hohohohoho")
            ResultadoT.insert(0, (x1))
            
        else:
            ite +=1
    if(ite==50): 
        print ("hahahahah")
        ResultadoT.insert(0, "No hay raíz")
               
            

"""while bucle==1:
    print("| --------------MéTODO DE NEWTON RAPHSON-------------- |")

   
    funcion= input("Ingrese una funcion en terminos de x: ")
    xo = float(input("Ingrese un punto Xo: ")) 
    errorT = float(input("Ingrese el error de tolerancia: ")) #El usuario debe darlo

    NewtonR(funcion,xo,errorT)

    bucle = int(input("Deseas repetir el metodo?\n 1.Si\n 0.No\n"))
"""


#-------------------------------------------------------------------------------------------
#Zona para definir comandos.
def clearcomm():
    FuncionX.delete("0", "end")
    PuntoX.delete("0","end")
    ErrorT.delete("0","end")
    ResultadoT.delete("0","end")
#-------------------------------------------------------------------------------------------
#creacion de ventana principal.
Ventana = Tk()
Ventana.title("Calculadora Newton")
Ventana.resizable(0,0) #bloqueo de tamaño.
#Ventana.iconbitmap('Interfaz\calculadora.ico') #icono.
#-------------------------------------------------------------------------------------------
#Creacion del frame.
FrameV=Frame()
FrameV.pack()
FrameV.config(bg="light grey") #color de fondo.
#-------------------------------------------------------------------------------------------
#Labels (etiquetas, todo lo que tenga "_L").
FuncionX_L=Label(FrameV, text="Funcion en X:")
FuncionX_L.grid(row=2, column=0, padx=10, pady=10)
FuncionX_L.config(bg="light grey") #color de fondo.

PuntoX_L=Label(FrameV, text="Punto X:")
PuntoX_L.grid(row=3, column=0, padx=10, pady=10)
PuntoX_L.config(bg="light grey") #color de fondo.

ErrorT_L=Label(FrameV, text="Error de tolerancia:")
ErrorT_L.grid(row=4, column=0, padx=10, pady=10)
ErrorT_L.config(bg="light grey") #color de fondo.

Resultado_L=Label(FrameV, text="Resultado:")
Resultado_L.grid(row=5, column=0, padx=10, pady=10)
Resultado_L.config(bg="light grey") #color de fondo.
#-------------------------------------------------------------------------------------------
#Cajas de texto.
FuncionX=Entry(FrameV)
FuncionX.grid(row=2, column=1, padx=10, pady=10)
FuncionX.config(justify="center")

PuntoX=Entry(FrameV)
PuntoX.grid(row=3, column=1, padx=10, pady=10)
PuntoX.config(justify="center")

ErrorT=Entry(FrameV)
ErrorT.grid(row=4, column=1, padx=10, pady=10)
ErrorT.config(justify="center")

ResultadoT=Entry(FrameV)
ResultadoT.grid(row=5, column=1, padx=10, pady=10)
ResultadoT.config(justify="center")
#ResultadoT.config(state=DISABLED)
#-------------------------------------------------------------------------------------------
#Botones.
BorrarB=Button(FrameV, text="Borrar", command=clearcomm)
BorrarB.grid(row=6, column=0, pady=10)

CalcularB=Button(FrameV, text="Calcular", command=process)
CalcularB.grid(row=6, column=1, pady=10, padx=10)

SalirB=Button(FrameV, text="Salir", command=Ventana.destroy)
SalirB.grid(row=6, column=2, pady=10, padx=10)
#-------------------------------------------------------------------------------------------
Ventana.mainloop() #es el ciclo para que la ventana "exista"