from re import A
import numpy as np
import sympy
from sympy import *
from tkinter import * #libreria de GUI
from matplotlib import pyplot
from tkinter import ttk

lista1=[0,0,0,0,0]
lista2=[]

#Variables
bucle = 1
x = symbols('x')

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

def evaluar ():
    fx = Funcion_B.get()
    li = Limite_inferior_B.get()
    ls = Limite_superior_B.get()
    err = Tolerancia_deseada_B.get()
    Falsa(fx,float(li),float(ls),float(err))

def Falsa(fx,aVal,bVal,errorT):
    ite = 0
    errorR = errorT*2 #Inicia como el doble de errorT para que la segunda condicion en el while empiece siendo falsa
    r1 = 0 #raiz actual 
    r2 = 0 #raiz anterior  | se intercambian cada bucle

    expr = parse_expr(fx)
    print(expr)

    while errorR>errorT and ite<50: #Se detiene cuando se cumplan una de las 2
        print("posicion ",ite)
        fa = expr.subs(x, aVal)
        print("fa.subs: ",fa)
        fb = expr.subs(x, bVal)
        print("fb.subs: ",fb)

        r1 = bVal-fb*(aVal-bVal)/(fa-fb) #paso 2
        print("r1 es: ",r1)

        fr1 = expr.subs(x ,r1) #paso 3

        print("f(ri) es ",fr1) #checking

        cambio = np.sign(fa)*np.sign(fr1)

        if cambio>0: #paso 4 y 5
            errorR = abs(r1-aVal)
            aVal=r1  
        #mimamamemima
        else:
            errorR = abs(bVal-r1)
            bVal=r1  
        ResultadoT.delete("0","end")
        print("La raiz es: ",r1)
        ResultadoT.insert(0, r1)
        print("El error relativo es: ",errorR)
        lista1 = [ite,round(fa,4),round(fb,4),round(r1,4),round(fr1,4),round(errorR,6)]
        lista2.append(lista1)
        if (ite>0):
            if(errorR<errorT): #paso 7
                print("El error relativo ",errorR," es menor al error de tolerancia ",errorT) #paso 8
            else:
                print("Se repite el ciclo")
        ite +=1                    
            
        if(ite==50):
            print("No hay raiz")

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
    tree = ttk.Treeview(top, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings', height=15)
    #Nombres columnas:
    tree.column("# 1", anchor=CENTER, width=10)
    tree.heading("# 1", text="i")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Fa")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="Fb")
    tree.column("# 4", anchor=CENTER)
    tree.heading("# 4", text="raiz")
    tree.column("# 5", anchor=CENTER)
    tree.heading("# 5", text="Fr")
    tree.column("# 6", anchor=CENTER)
    tree.heading("# 6", text="Error")

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
Ventana.title("Falsa posicion")
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

Tolerancia_deseada_L=Label(FrameV, text="Error tolerancia:")
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
GraficaB.grid(row = 9, column= 1, padx=10, pady=10)

TablaB=Button(FrameV, text="Ver Iteraciones", command=tabla)
TablaB.grid(row=9, column=2, pady=10, padx=20)

SalirB=Button(FrameV, text="Salir", command=Ventana.destroy)
SalirB.grid(row=8, column=2, pady=10, padx=10)
#-------------------------------------------------------------------------------------------
Ventana.mainloop() #es el ciclo para que la ventana "exista"