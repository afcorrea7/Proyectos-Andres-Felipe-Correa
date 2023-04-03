import sympy 
from sympy import *
from tkinter import * #libreria de GUI
from tkinter import ttk
import numpy as np
from matplotlib import pyplot
from sympy import *
#Variables
lista1=[0,0,0,0]
lista2=[]
bucle = 1
x=symbols('x')

def grafica():
  x=symbols('x')
  z=0
  funcion=parse_expr(FuncionX.get())
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

        lista1 = [ite, round(funcionNum,4), round(x1,4),round(errorR,4)]
        lista2.append(lista1)

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
    
def tabla():
    top=Tk()
    top.geometry('500x400')
    tree = ttk.Treeview(top, column=("c1", "c2", "c3", "c4"), show='headings', height=12)
    #Nombres columnas:
    tree.column("# 1", anchor=CENTER, width=10)
    tree.heading("# 1", text="i")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Fx")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="Raiz")
    tree.column("# 4", anchor=CENTER)
    tree.heading("# 4", text="Error")

    titulo = Label(top, text= "ITERACIONES")

    scroll = Scrollbar(top)
    scroll.pack(side=RIGHT, fill=BOTH)

    for n in range(0,len(lista2),1):
        print(lista2[n])
        tree.insert('', 'end', text="1", values=(lista2[n]))
        
    tree.config(yscrollcommand = scroll.set)
    scroll.config(command = tree.yview)

    titulo.pack()
    tree.pack()

    top.mainloop()

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
Aviso_L=Label(FrameV, text="Ejemplo de como escribir la función: a*x**2+b*x+c")
Aviso_L.grid(row=1, column=1, padx=10, pady=10)
Aviso_L.config(bg="light grey") #color de fondo.

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

GraficaB=Button(FrameV, text="Graficar", command= grafica)
GraficaB.grid(row = 7, column= 1, padx=10, pady=10)

TablaB=Button(FrameV, text="Ver Iteraciones", command=tabla)
TablaB.grid(row=7, column=2, pady=10, padx=20)

SalirB=Button(FrameV, text="Salir", command=Ventana.destroy)
SalirB.grid(row=6, column=2, pady=10, padx=10)
#-------------------------------------------------------------------------------------------
Ventana.mainloop() #es el ciclo para que la ventana "exista"