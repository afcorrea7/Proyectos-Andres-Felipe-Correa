#from this import d
import sympy
from sympy import *
from tkinter import * #libreria de GUI
from tkinter import ttk
from matplotlib import pyplot
from sympy import *
#Variables
lista1=[0,0,0,0,0,0]
lista2=[]
# <3 x**3+2*x**2+2*x+4

bucle = 1
x = symbols('x')

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

def evaluar():

  FunX = FuncionX.get()
  ValX1 = ValorX1.get()
  ValX2 = ValorX2.get()
  ErrT = Error_T.get()

  print("-----------------------------------")
  print(" ")
  print("Valores => ",ErrT,ValX1,ValX2,FunX)
  print(" ")
  print("-----------------------------------")

  Biseccion(FunX, int(ValX1), int(ValX2), float(ErrT))
  

  #clearcomm()

def Biseccion(ecuacion,aVal,bVal,errorT):
    ite = 0
    errorR = errorT*2 #Inicia como el doble de errorT para que la segunda condicion en el while empiece siendo falsa
    r1 = 0 #raiz actual 
    r2 = 0 #raiz anterior  | se intercambian cada bucle

    expr = parse_expr(ecuacion)
    print(expr)

    while errorR>errorT and ite<50: #Se detiene cuando se cumplan una de las 2
        print("posicion ",ite)
        fa = expr.subs(x, aVal)
        print("fa.subs: ",fa)
        fb = expr.subs(x, bVal)
        print("fb.subs: ",fb)

        if((fa*fb)<0): #paso 1
            r2=r1
            r1 = (aVal+bVal)/2 #paso 2
            print("r1 es: ",r1)

            fri = expr.subs(x ,r1) #paso 3

            print("f(ri) es ",fri) #checking

            if(fri*fb)<0: #paso 4 y 5
                aVal=r1  
            
            else:
                bVal=r1  
            
            errorR= abs(r2-r1) #abs() = valor absoluto | paso 6
                                                #raiz anterior menos raiz actual
            print("Error relativo calculado: ",errorR)

            #Guarda todo en una posicion de Lista 1
            lista1 = [ite,round(fa,4),round(fb,4),round(r1,4),round(fri,4),round(errorR,6)]
            lista2.append(lista1)

            if(errorR<errorT): #paso 7

                ResultadoT.insert(0,errorR)
                ResultadoR.insert(0,r1)
                print("El error relativo ",errorR," es menor al error de tolerancia ",errorT) #paso 8
                print("La raiz es: ", r1)


            else:
                print("Se repite el ciclo")
            ite +=1                    
            
        else:

            ResultadoR.insert("No hay raiz")
            print(0, "No hay raiz")
            ite =50




"""while bucle==1:
    print("| --------------METODO DE BISECCION -------------- |")

    #asignacion de valores a variables
    ecuacion = input("Ingrese una funcion en terminos de x: ")
    aVal = float(input("Ingrese un valor para x (fa): ")) 
    bVal = float(input("Ingrese otro valor para x (fb): "))
    errorT = float(input("Ingrese el error de tolerancia: ")) #El usuario debe darlo

    #fa = eval(ecuacion,{'x':aVal}) #eval evalua la expresion.
    #fb = eval(ecuacion,{'x':bVal}) 
        

    Biseccion(ecuacion,aVal,bVal,errorT)

    bucle = int(input("Deseas repetir el metodo?\n 1.Si\n 0.No\n"))"""
            



#-------------------------------------------------------------------------------------------
#Zona para definir comandos.
def clearcomm():
    FuncionX.delete("0", "end")
    ValorX1.delete("0","end")
    ValorX2.delete("0","end")
    Error_T.delete("0","end")
    ResultadoT.delete("0","end")
    ResultadoR.delete("0","end")

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
Ventana.title("Calculadora Biseccion")
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

ValorX1_L=Label(FrameV, text="Punto X:")
ValorX1_L.grid(row=3, column=0, padx=10, pady=10)
ValorX1_L.config(bg="light grey") #color de fondo.

ValorX2_L=Label(FrameV, text="Otro valor para X:")
ValorX2_L.grid(row=4, column=0, padx=10, pady=10)
ValorX2_L.config(bg="light grey") #color de fondo.

ErrorT_L=Label(FrameV, text="Error de tolerancia:")
ErrorT_L.grid(row=5, column=0, padx=10, pady=10)
ErrorT_L.config(bg="light grey") #color de fondo.

Resultado_L=Label(FrameV, text="Error Relativo:")
Resultado_L.grid(row=6, column=0, padx=10, pady=10)
Resultado_L.config(bg="light grey") #color de fondo.

ResultadoR_L=Label(FrameV, text="Raiz:")
ResultadoR_L.grid(row=7, column=0, padx=10, pady=10)
ResultadoR_L.config(bg="light grey")
#-------------------------------------------------------------------------------------------
#Cajas de texto.
FuncionX=Entry(FrameV)
FuncionX.grid(row=2, column=1, padx=10, pady=10)
FuncionX.config(justify="center")

ValorX1=Entry(FrameV)
ValorX1.grid(row=3, column=1, padx=10, pady=10)
ValorX1.config(justify="center")

ValorX2=Entry(FrameV)
ValorX2.grid(row=4, column=1, padx=10, pady=10)
ValorX2.config(justify="center")

Error_T=Entry(FrameV)
Error_T.grid(row=5, column=1, padx=10, pady=10)
Error_T.config(justify="center")

ResultadoT=Entry(FrameV)
ResultadoT.grid(row=6, column=1, padx=10, pady=10)
ResultadoT.config(justify="center")

ResultadoR=Entry(FrameV)
ResultadoR.grid(row=7, column=1, padx=10, pady=10)
ResultadoR.config(justify="center")
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