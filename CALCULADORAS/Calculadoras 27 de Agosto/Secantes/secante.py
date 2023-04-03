import numpy as np
from tkinter import * #libreria de GUI
from tkinter import ttk
import scipy.optimize as optimize
from sympy import *
from matplotlib import pyplot
xS = symbols('x')
#def f(x):
lista1=[0,0,0,0]
lista2=[]

#    return np.sin(2*x+1)-3*x/5+1
def evaluar():
    fun = Funcion_B.get()
    ls = Limite_superior_B.get()
    li = Limite_inferior_B.get()
    err = Tolerancia_deseada_B.get()
    fun= parse_expr(fun)   
    secante(fun, float(li), float(ls), float(err))


def secante(f, x0, x1,emax, n= 100):
    for k in range(n):
        fp = ((f.subs(xS,x1))-(f.subs(xS,x0)))/(x1-x0)
        x = x1-(f.subs(xS,x1))/fp
        print(fp)
        print("x: ",x)
        ResultadoT.delete("0","end")      
        ResultadoT.insert(0, x)
        print(x1,"-",f.subs(xS,x1),"/",fp)
        e = abs((x-x1)/x)
        print (k,x,fp,e)
        lista1=[k,round(x,4),round(fp,4),round(e,4)]
        lista2.append(lista1)
        if e<emax:
            break
        x0=x1
        x1=x

def grafica():
  x=symbols('x')
  z=0
  funcion=parse_expr(Funcion_B.get())
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

#-------------------------------------------------------------------------------------------
#Zona para definir comandos.
def clearcomm():
    Funcion_B.delete("0", "end")
    Limite_inferior_B.delete("0","end")
    Limite_superior_B.delete("0","end")
    Tolerancia_deseada_B.delete("0", "end")
    ResultadoT.delete("0","end")

def tabla():
    top=Tk()
    top.geometry('600x500')
    tree = ttk.Treeview(top, column=("c1", "c2", "c3", "c4"), show='headings', height=12)
    #Nombres columnas:
    tree.column("# 1", anchor=CENTER, width=10)
    tree.heading("# 1", text="i")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Fr")
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
Ventana.title("Calculadora Secante")
Ventana.resizable(0,0) #bloqueo de tamaño.
#Ventana.iconbitmap('calculadora.ico') #icono.
#-------------------------------------------------------------------------------------------
#Creacion del frame.
FrameV=Frame()
FrameV.pack()
FrameV.config(bg="light grey") #color de fondo.
#-------------------------------------------------------------------------------------------
#Labels (etiquetas, todo lo que tenga "_L").
Funcion_L=Label(FrameV, text="Funcion:")
Funcion_L.grid(row=2, column=0, padx=10, pady=10)
Funcion_L.config(bg="light grey") #color de fondo.

Limite_inferior_L=Label(FrameV, text="Limite inferior:")
Limite_inferior_L.grid(row=3, column=0, padx=10, pady=10)
Limite_inferior_L.config(bg="light grey") #color de fondo.

Limite_superior_L=Label(FrameV, text="Limite superior:")
Limite_superior_L.grid(row=4, column=0, padx=10, pady=10)
Limite_superior_L.config(bg="light grey") #color de fondo.

Tolerancia_deseada_L=Label(FrameV, text="Tolerancia deseada:")
Tolerancia_deseada_L.grid(row=5, column=0, padx=10, pady=10)
Tolerancia_deseada_L.config(bg="light grey") #color de fondo.

Resultado_L=Label(FrameV, text="Resultado:")
Resultado_L.grid(row=6, column=0, padx=10, pady=10)
Resultado_L.config(bg="light grey") #color de fondo.

#-------------------------------------------------------------------------------------------
#Cajas de texto.
Funcion_B=Entry(FrameV)
Funcion_B.grid(row=2, column=1, padx=10, pady=10)
Funcion_B.config(justify="center")

Limite_inferior_B=Entry(FrameV)
Limite_inferior_B.grid(row=3, column=1, padx=10, pady=10)
Limite_inferior_B.config(justify="center")

Limite_superior_B=Entry(FrameV)
Limite_superior_B.grid(row=4, column=1, padx=10, pady=10)
Limite_superior_B.config(justify="center")

Tolerancia_deseada_B=Entry(FrameV)
Tolerancia_deseada_B.grid(row=5, column=1, padx=10, pady=10)
Tolerancia_deseada_B.config(justify="center")

ResultadoT=Entry(FrameV)
ResultadoT.grid(row=6, column=1, padx=10, pady=10)
ResultadoT.config(justify="center")

#-------------------------------------------------------------------------------------------
#Botones.
BorrarB=Button(FrameV, text="Borrar", command=clearcomm)
BorrarB.grid(row=8, column=0, pady=10)

CalcularB=Button(FrameV, text="Calcular", command=evaluar)
CalcularB.grid(row=8, column=1, pady=10, padx=10)

GraficaB=Button(FrameV, text="Graficar", command= grafica)
GraficaB.grid(row = 8, column= 3, padx=10, pady=10)

TablaB=Button(FrameV, text="Ver Iteraciones", command=tabla)
TablaB.grid(row=9, column=0, pady=10, padx=20)

SalirB=Button(FrameV, text="Salir", command=Ventana.destroy)
SalirB.grid(row=8, column=2, pady=10, padx=10)
#-------------------------------------------------------------------------------------------
Ventana.mainloop() #es el ciclo para que la ventana "exista"