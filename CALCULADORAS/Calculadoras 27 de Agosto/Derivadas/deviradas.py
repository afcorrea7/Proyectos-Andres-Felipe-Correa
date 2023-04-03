from sqlite3 import DateFromTicks
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from tkinter import *
from matplotlib import pyplot
import numpy as np
#La forma de llamar a las incognitas
x, z = symbols ('x z') 

def derivada(): 
    try:
     fun_escrita = funcion.get()
     f = parse_expr(fun_escrita)
     dato_escrito =dato.get()
     z= parse_expr(dato_escrito)
     derivada= diff (f,x)
     respuesta=lambdify(x,derivada)
     respuesta= respuesta(float(z))
     etiqueta.configure(text=respuesta)
     etiqueta3.configure(text=derivada)
    
    except:
         etiqueta.configure(text="Introduce la funcion correctamente")
 

def derivada2(): 
 try:
  fun_escrita = funcion.get()
  f = parse_expr(fun_escrita)
  dato_escrito =dato.get()
  z= parse_expr(dato_escrito)
  derivada2= diff (f,x,x)
  respuesta2=lambdify(x,derivada2)
  respuesta2= respuesta2(float(z))
  etiqueta2.configure(text=respuesta2)
  etiqueta4.configure(text=derivada2)
 except:
         etiqueta2.configure(text="Introduce la funcion correctamente")

#Interfaz grafica 
#Ventana
ventana =Tk()
ventana.geometry ('600x600')
ventana.title("Cálculadora de Derivadas")
#Titulo
anuncio = Label(ventana, text="Introduce una función de x:", font=("Arial", 15), fg="blue")
anuncio.pack()

#Campo de texto
funcion = Entry(ventana, font=("Arial", 15))
funcion.pack()
#Titulo
anuncio2 = Label(ventana, text="Introduce el valor x:", font=("Arial", 15), fg="blue")
anuncio2.pack()
#Campo de texto
dato = Entry(ventana, font=("Arial", 15))
dato.pack()
#Boton Derivar
boton1 = Button(ventana, text="Derivar Función", font=("Arial", 15), command=derivada)
boton1.pack()
#Boton derivada de la derivada
boton4 = Button(ventana, text="Derivar Función 2", font=("Arial", 15), command=derivada2)
boton4.pack()


#Etiquetas y Titulos:
anuncioDeri = Label(ventana, text="Primera derivada:", font=("Arial", 15), fg="blue")
anuncioDeri.pack()

etiqueta3 = Label(ventana, text="[ ]", font=("Arial", 15), fg="red")
etiqueta3.pack()

anuncioResul = Label(ventana, text="Primer resultado:", font=("Arial", 15), fg="blue")
anuncioResul.pack()

etiqueta = Label(ventana, text="[ ]", font=("Arial", 15), fg="red")
etiqueta.pack()

anuncioDeri2 = Label(ventana, text="Segunda derivada:", font=("Arial", 15), fg="blue")
anuncioDeri2.pack()

etiqueta4 = Label(ventana, text="[ ]", font=("Arial", 15), fg="red")
etiqueta4.pack()

anuncioResul2 = Label(ventana, text="Segundo resultado:", font=("Arial", 15), fg="blue")
anuncioResul2.pack()

etiqueta2 = Label(ventana, text="[ ]", font=("Arial", 15), fg="red")
etiqueta2.pack()


def _quit(): #Función salir
    ventana.quit()     # detiene mainloop
    ventana.destroy()  # elimina la ventana de la memoria

def _graph():
    #----------------------------------------------------------------------------------------------------------------------------------
    w=0
    ini=0
    lim=30

    func=parse_expr(funcion.get())
    func_deri = diff(func,x) #Derivada
    func_derideri = diff(func,x,x) #Derivada de la derivada
    valX=[]
    valY=[]
    for i in range (ini*10,(lim*10)+1,1):
        val=i/10
        w=-1*(-1*(val)+15)
        valX.append(w)
        result=lambdify(x,func_deri)
        result=result(w)
        valY.append(result)

    print("--------------------------",func_deri)
    pyplot.subplot(3,1,1) #filas, columnas, # de grafica
    pyplot.title("Derivada")
    pyplot.plot(valX, valY) #plot derivada
    # Establecer el color de los ejes.
    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")
    # Limitar los valores de los ejes.
    pyplot.xlim(-15, 15)
    pyplot.ylim(-15, 15)
    #----------------------------------------------------------------------------------------------------------------------------------

    w=0
    ini=0
    lim=30

    valX2=[]
    valY2=[]
    for i in range (ini*10,(lim*10)+1,1):
        val=i/10
        w=-1*(-1*(val)+15)
        valX2.append(w)
        result=lambdify(x,func_derideri)
        result=result(w)
        valY2.append(result)

    print("--------------------------",func_derideri)
    pyplot.subplot(3,1,2) #filas, columnas, # de grafica
    pyplot.title("Derivada de la derivada")
    pyplot.plot(valX2, valY2) #plot derivada de la derivada

    # Establecer el color de los ejes.
    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")
    # Limitar los valores de los ejes.
    pyplot.xlim(-15, 15)
    pyplot.ylim(-15, 15)
    #----------------------------------------------------------------------------------------------------------------------------------
    
    #Grafica Funcion normal:
    w=0
    ini=0
    lim=30

    valX3=[] 
    valY3=[]
    for i in range (ini*10,(lim*10)+1,1):
        val=i/10
        w=-1*(-1*(val)+15)
        valX3.append(w)
        result=lambdify(x,funcion.get())
        result=result(w)
        valY3.append(result)

    print("--------------------------",funcion.get())
    pyplot.subplot(3,1,3) #filas, columnas, # de grafica
    pyplot.title("Función")
    pyplot.plot(valX3, valY3) #plot funcion normal

    # Establecer el color de los ejes.
    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")
    # Limitar los valores de los ejes.
    pyplot.xlim(-15, 15)
    pyplot.ylim(-15, 15)
    #----------------------------------------------------------------------------------------------------------------------------------

    pyplot.subplots_adjust(hspace=0.5, wspace=0.2) #ajusta espacio entre graficas (top, bottom, hspace, wspace)

    pyplot.show() #Grafica todo -----

#Boton Salir
button3 = Button(master=ventana, text="Salir", font=("Arial", 15), command=_quit)
button3.pack()

buttonGraph = Button(master=ventana, text="Graficar",font=("Arias",15),command=_graph)
buttonGraph.pack()


ventana.mainloop()
