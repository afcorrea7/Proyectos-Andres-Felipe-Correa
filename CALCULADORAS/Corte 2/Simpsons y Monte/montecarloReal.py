from numpy.random import uniform as unif
from sympy import *
from tkinter import *
from matplotlib import pyplot

def montecarlo(fx, a, b, num,m):
    suma=0
    resultado=0
    funcionDev=parse_expr(fx) #pasa de string a una ecuación 
    x=symbols('x')
    for i in range (0,num,1):
        varX=unif(0,1) 
        varY=unif(0,1)
        xi=varX*(b-a)+a
        yi=varY*m
        fxi=funcionDev.subs(x,xi)
        
        if(yi<=fxi):
            suma+=1
        
        #print(funcion)

    resultado=(suma*(b-a)*m)/num
    return resultado
    print("Integral",resultado)



"""while bucle==1:
    print("| --------------INTEGRACION NUMERICA MONTECARLO-------------- |")

    #asignacion de valores a variables
    ecuacion = input("Ingrese una funcion en terminos de x: ")
    aVal = float(input("Ingrese un valor para a: ")) 
    bVal = float(input("Ingrese otro valor para b: "))
    num = int(input("Ingrese la cantidad de números aleatorios: ")) #El usuario debe darlo

    montecarlo(ecuacion,aVal,bVal,num)

    bucle = int(input("Deseas repetir el metodo?\n 1.Si\n 0.No\n"))"""
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

def calcall():
    ec = ecX.get()
    vala = aVal.get()
    valb = bVal.get()
    pt = ptNo.get()
    m = mNo.get()
    vala = float(vala)
    valb = float(valb)
    pt = int(pt)
    m = int(m)

    anLI.configure(text=montecarlo(ec,vala,valb,pt,m))

def clearcomm():
    ecX.delete("0", "end")
    aVal.delete("0","end")
    bVal.delete("0","end")
    ptNo.delete("0","end")
    mNo.delete("0","end")
    anLI.configure(text="")
   

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

lb4 = Label(mFrame, text="Número de aleatorios: ")
lb4.grid(row=3, column=0, padx=10, pady=10)
lb4.config(bg="light grey")

lb5 = Label(mFrame, text="Cota superior: ")
lb5.grid(row=4, column=0, padx=10, pady=10)
lb5.config(bg="light grey")

lb5 = Label(mFrame, text="Integral: ")
lb5.grid(row=5, column=0, padx=10, pady=10)
lb5.config(bg="light grey")
#Input----------------------------------------------------------------------------------------------------
ecX = Entry(mFrame)
ecX.grid(row=0,column=1,padx=10,pady=10)

aVal = Entry(mFrame)
aVal.grid(row=1,column=1,padx=10,pady=10)

bVal = Entry(mFrame)
bVal.grid(row=2,column=1,padx=10,pady=10)

ptNo = Entry(mFrame)
ptNo.grid(row=3,column=1,padx=10,pady=10)

mNo = Entry(mFrame)
mNo.grid(row=4,column=1,padx=10,pady=10)
#Answer---------------------------------------------------------------------------------------------------
anLI = Label(mFrame)
anLI.grid(row=5, column=1, padx=10, pady=10)
anLI.config(bg="light grey") 

#Button----------------------------------------------------------------------------------------------------
fn = Button(mFrame, text="calcular", command=calcall)
fn.grid(row=7, column=0, padx=10,pady=10)

Graficar = Button(mFrame, text="Graficar", command=grafica)
Graficar.grid(row=7, column=2, padx=10, pady=10)

Borrar = Button(mFrame, text="Borrar", command=clearcomm)
Borrar.grid(row=7, column=1, padx=10, pady=10)
Main.mainloop()