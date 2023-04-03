from sympy import *
from tkinter import *
from matplotlib import pyplot

x = symbols('x')
bucle=1

def Trapecios(ecu,aVal,bVal,n):
    fun=0
    suma=0
    valO=0 
    val1=0
    expr = parse_expr(ecu) #pone la ecuacion en terminos que sympy entienda
    #Delta x
    deltaX = (bVal-aVal)/n

    for i in range(n):
        if i==0: #f(x0)
            xo=aVal
            valO=expr.subs(x,xo)
        if(i<n-1): #f(x1) + f(x2) + ... + f(xn)
            x1=xo+deltaX
            xo=x1
            fun=expr.subs(x,xo)
            suma+=2*fun
        if(i==n-1): #f(xn-1)
            xo=bVal
            val1=expr.subs(x,xo)

    integral=(deltaX/2)*(valO+suma+val1)

    print("Valor de la integral: ",integral)
    return integral
    

def calcular():
    ecuacion = FuncionX_T.get()
    aVal = ValA_T.get()
    bVal = ValB_T.get()
    part = partes_T.get()

    resultado_T.insert(0,Trapecios(ecuacion, float(aVal), float(bVal), int(part)))

def grafica():
  x=symbols('x')
  z=0
  funcion=parse_expr(FuncionX_T.get())
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

"""while bucle==1:
    print("| --------------INTEGRACION POR TRAPECIOS -------------- |")

    #asignacion de valores a variables
    ecuacion = input("Ingrese una funcion en terminos de x: ")
    aVal = float(input("Ingrese un valor para a: ")) 
    bVal = float(input("Ingrese otro valor para b: "))
    partinum = int(input("Ingrese el número de particiones: ")) #El usuario debe darlo
    
    Trapecios(ecuacion,aVal,bVal,partinum)

    bucle = int(input("Deseas repetir el metodo?\n 1.Si\n 0.No\n"))"""


#-------------------------------------------------------------------------------------------
#Zona para definir comandos.
def clearcomm():
    FuncionX_T.delete("0", "end")
    ValA_T.delete("0","end")
    ValB_T.delete("0","end")
    partes_T.delete("0","end")
    resultado_T.delete("0","end")

#-------------------------------------------------------------------------------------------
#creacion de ventana principal.
Ventana = Tk()
Ventana.title("Calculadora trapecio")
#Ventana.resizable(0,0)
#-------------------------------------------------------------------------------------------
#Creacion del frame.
FrameV=Frame()
FrameV.pack()
FrameV.config(bg="light grey")
#-------------------------------------------------------------------------------------------
#Etiquetas
FuncionX_L = Label(FrameV, text="Funcion en x")
FuncionX_L.grid(row=1, column=0, padx=10, pady=10)
FuncionX_L.config(bg="light grey") 

ValA_L = Label(FrameV, text="Valor A")
ValA_L.grid(row=2, column=0, padx=10, pady=10)
ValA_L.config(bg="light grey")

ValB_L = Label(FrameV, text="Valor B")
ValB_L.grid(row=3, column=0, padx=10, pady=10)
ValB_L.config(bg="light grey")

partes_L = Label(FrameV, text="Numero de particiones")
partes_L.grid(row=4, column=0, padx=10, pady=10)
partes_L.config(bg="light grey")

resultado_L = Label(FrameV, text="Resultado")
resultado_L.grid(row=5, column=0, padx=10, pady=10)
resultado_L.config(bg="light grey")
#-------------------------------------------------------------------------------------------
#Cajas de texto
FuncionX_T = Entry(FrameV)
FuncionX_T.grid(row=1, column=1, padx=10, pady=10)
FuncionX_T.config(justify="center")

ValA_T = Entry(FrameV)
ValA_T.grid(row=2, column=1, padx=10, pady=10)
ValA_T.config(justify="center")

ValB_T = Entry(FrameV)
ValB_T.grid(row=3, column=1, padx=10, pady=10)
ValB_T.config(justify="center")

partes_T = Entry(FrameV)
partes_T.grid(row=4, column=1, padx=10, pady=10)
partes_T.config(justify="center")

resultado_T = Entry(FrameV)
resultado_T.grid(row=5, column=1, padx=10, pady=10)
resultado_T.config(justify="center")
#-------------------------------------------------------------------------------------------
#Botones
calcular = Button(FrameV, text="Calcular", command=calcular)
calcular.grid(row=6, column=1, padx=10, pady=10)

Salir = Button(FrameV, text="Salir", command=Ventana.destroy)
Salir.grid(row=7, column=1, padx=10, pady=10)

Graficar = Button(FrameV, text="Graficar", command=grafica)
Graficar.grid(row=6, column=0, padx=10, pady=10)

Borrar = Button(FrameV, text="Borrar", command=clearcomm)
Borrar.grid(row=6, column=2, padx=10, pady=10)
#-------------------------------------------------------------------------------------------
Ventana.mainloop()