#-----------------------------------------LIBRERIAS----------------------------------------------------------
from sympy import *
from tkinter import messagebox as MessageBox
from tkinter import * #libreria de GUI
from tkinter import ttk
from matplotlib import pyplot
from distutils.cmd import Command
from distutils.command.config import config
from numbers import Real
import math
from turtle import clear
from typing import BinaryIO #Libreria para usar modf y separar fraccionarios de enteros
from sqlite3 import DateFromTicks
from sympy.parsing.sympy_parser import parse_expr
import numpy as np
from re import A
from ast import Num
from re import I
from sys import int_info
from tokenize import Double
from decimal import *
import re
import scipy as sp  # Importamos scipy como el alias sp
import scipy.optimize as optimize
from numpy.random import uniform as unif
import random
from cgitb import text
from tkinter.tix import COLUMN #libreria de GUI
#-----------------------------------------------------------------------------------------------------------
#VARIABLES


#-----------------------------------------------------------------------------------------------------------
#Principal
def ventana1():
    global ventana1
    ventana1 = Tk()
    ventana1.title("Menu")
    #Ventana.geometry('200x250')
    ventana1.resizable(0,0) #bloqueo de tamaño.
    ventana1.iconbitmap('Icono\calculadora.ico') #icono.
    #-------------------------------------------------------------------------------------------
    #Creacion del frame.
    FrameV=Frame()
    FrameV.pack()
    FrameV.config(bg="light grey") #color de fondo.
    #-------------------------------------------------------------------------------------------
    #Labels (etiquetas).
    binarioL=Label(FrameV, text="Menu de calculadoras")
    binarioL.grid(row=0, column=2, padx=10, pady=10)
    binarioL.config(bg="light grey") #color de fondo.

    #-------------------------------------------------------------------------------------------
    #Botones.
    Calculadora1=Button(FrameV, text="Raices", command=raices)
    Calculadora1.grid(row=1, column=1, padx=10, pady=10)

    Calculadora2=Button(FrameV, text="Conversiones", command=conversiones)
    Calculadora2.grid(row=1, column=2, padx=10, pady=10)

    Calculadora3=Button(FrameV, text="Derivadas", command=ventana4)
    Calculadora3.grid(row=1, column=3, padx=10, pady=10)

    Calculadora4=Button(FrameV, text="Integraciones", command=integracion)
    Calculadora4.grid(row=2, column=1, padx=10, pady=10)

    Calculadora14=Button(FrameV, text="Matrices", command=ventana15)
    Calculadora14.grid(row=2, column=2, padx=10, pady=10)

    Calculadora15=Button(FrameV, text="Minimos cuadrados", command=ventana16)
    Calculadora15.grid(row=2, column=3, padx=10, pady=10)

    VolverB=Button(FrameV, text="Creditos", command=creditos)
    VolverB.grid(row=17, column=0, pady=10, padx=10)

    SalirB=Button(FrameV, text="Salir", command=ventana1.destroy)
    SalirB.grid(row=17, column=4, pady=10, padx=10)

    ventana1.mainloop()
#Biseccion
def ventana2():
    global ventana2
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

#-------------------------------------------------------------------------------------------
    def clearcomm():
        FuncionX.delete("0", "end")
        ValorX1.delete("0","end")
        ValorX2.delete("0","end")
        Error_T.delete("0","end")
        ResultadoT.delete("0","end")
        ResultadoR.delete("0","end")

    def tabla():
        top=Toplevel(ventana2)
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
    #ventana2 = Tk()
    ventana2 = Toplevel(raices) #crear una ventana siguiente de la ventana1
    ventana2.title("Calculadora Biseccion")
    ventana2.resizable(0,0) #bloqueo de tamaño.
    #-------------------------------------------------------------------------------------------
    #Creacion del frame.
    FrameV=Frame(ventana2)
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

    SalirB=Button(FrameV, text="Volver", command=volver_ventana1)
    SalirB.grid(row=8, column=2, pady=10, padx=10)
    #-------------------------------------------------------------------------------------------
    if(ventana2):
        raices.withdraw()

    ventana2.mainloop()
#Conversiones
def ventana3():
    global ventana3
    #Variables globables
    contador=7 #repeticiones de multiplicacion
    i=1 #Bucle switch case

    #Funciones para separar entero de decimal

    def evaluar():
      binarie = binarioT.get()
      dec = decimalT.get()
      octalis = OctadecimalT.get()
      hex = HexadecimalT.get() 
      if hex != '':
        try:
          hex = float(hex)
        except:
          hex = hex + ".0"
        hex = str(hex)

      clearcomm()
      if dec != None and dec != '':
        decimalT.insert(0,dec)
        binarioT.insert(0, Deci_Binario(float(dec)))
        OctadecimalT.insert(0, Deci_Octal(float(dec)))
        HexadecimalT.insert(0, Deci_Hexa(float(dec)))
      if binarie != None and binarie != '':
        binarioT.insert(0, binarie)
        decimalT.insert(0, B_Dec(float(binarie),2))
        OctadecimalT.insert(0, Deci_Octal(float(B_Dec(float(binarie),2))))
        HexadecimalT.insert(0, Deci_Hexa(float(B_Dec(float(binarie),2))))
      if octalis != None and octalis != '':
        OctadecimalT.insert(0, octalis)
        binarioT.insert(0, Deci_Binario(float(B_Dec(float(octalis),8))))
        HexadecimalT.insert(0, Deci_Hexa(float(B_Dec(float(octalis),8))))
        decimalT.insert(0, B_Dec(float(octalis),8))
      if hex != None and hex != '':
        HexadecimalT.insert(0, hex)
        decimalT.insert(0,Hex_Partes(hex))
        binarioT.insert(0,Deci_Binario(Hex_Partes(hex)))
        OctadecimalT.insert(0,Deci_Octal(Hex_Partes(hex)))

      ResultadosL.configure(text="Hola")

    def parteEntera(num):
      fraccion,entero = math.modf(num)
      return int(entero)

    def parteFraccion(num):
      fraccion,entero = math.modf(num)
      return round(fraccion,10)

    #Decimal Entero a Binario
    def Deci_Ent_Binario(num):
      entero = parteEntera(num)
      binariop1 = format(entero,'0b') #format retira el 0b del resultado, se ve mas estetico
      return binariop1

    #Decimal Fraccional a Binario
    def Deci_Frac_Bin(num):
      fraccion = parteFraccion(num)
      binariop2= ""
      cuenta = 0

      while cuenta != contador:
        multiplicacion = fraccion * 2
        binariop2 = binariop2 + str(parteEntera(multiplicacion))
        fraccion = parteFraccion(multiplicacion)
        cuenta += 1
      return binariop2

    #Decimal a Binario, Esta es la funcion que se llama en el case 1
    def Deci_Binario(num):
      binarioFinal = str(Deci_Ent_Binario(num)+'.'+str(Deci_Frac_Bin(num)))
      return binarioFinal

    #Decimal Entero a Octal
    def Deci_Ent_Octal(num):
      entero = parteEntera(num)
      octalp1= format(entero,'0o')
      return octalp1

    #Decimal Fraccional a Octal
    def Deci_Frac_Octal(num):
      fraccion = parteFraccion(num)
      octalp2 = ""
      cuenta = 0

      while cuenta != contador:
        multiplicacion = fraccion * 8
        octalp2 = octalp2 + str(parteEntera(multiplicacion))
        fraccion = parteFraccion(multiplicacion)
        cuenta += 1
      return octalp2

    #Decimal a Octal, Esta es la funcion que se llama en el case 2
    def Deci_Octal(num):
      octalFinal = str(Deci_Ent_Octal(num)+'.'+str(Deci_Frac_Octal(num)))
      return octalFinal

    #Decimal Entero a Hexadecimal
    def Deci_Ent_Hexadecimal(num):
      entero = parteEntera(num)
      hexap1 = format(entero,'0x')
      return hexap1

    #Decimal Fraccional a Hexadecimal
    def Deci_Frac_Hexadecimal(num):
      fraccion = parteFraccion(num)
      hexap2 = ""
      cuenta=0

      while cuenta != contador:
        multiplicacion = fraccion * 16
        if parteEntera(multiplicacion) ==10:
          hexap2=hexap2+str("a")
        elif parteEntera(multiplicacion) ==11:
          hexap2=hexap2+str("b")
        elif parteEntera(multiplicacion) ==12:
          hexap2=hexap2+str("c")
        elif parteEntera(multiplicacion) ==13:
          hexap2=hexap2+str("d")
        elif parteEntera(multiplicacion) ==14:
          hexap2=hexap2+str("e")
        elif parteEntera(multiplicacion) ==15:
          hexap2=hexap2+str("f")
        else:
          hexap2=hexap2+str(parteEntera(multiplicacion))

        fraccion = parteFraccion(multiplicacion)
        cuenta += 1
      return hexap2

    #Decimal a Hexadecimal, Esta es la funcion que se llama en el case 3
    def Deci_Hexa(num):
      hexaFinal= str(Deci_Ent_Hexadecimal(num))+'.'+str(Deci_Frac_Hexadecimal(num))
      return hexaFinal
    #Convirtiendo a decimal, podemos llamar las funciones anteriores.
      #La formula para octal y binario es la misma, solo cambia la base
    #Base 2 u 8 Entera a Decimal
    def B_Ent_Dec(num, base):
      entero=str(parteEntera(num))
      decimal = 0

      for pos, digito in enumerate(entero[::-1]):
        decimal += int(digito) * base ** pos
      return decimal

    #Base 2 u 8 Fraccionario a Decimal
    def B_Frac_Dec(numero,base):
      fraccion = parteFraccion(numero)
      cuenta=0
      while cuenta!=contador:
        fraccion = fraccion*10
        cuenta+=1
      fraccion = str(int(fraccion))

      decimal = 0
      pos = 1

      for pos,digito in enumerate(fraccion):
        decimal += float(digito)*(float(base**(-pos-1)))
      return decimal

    #Base 2 u 8 a Decimal, Esto es lo que va en el case
    def B_Dec(num,base):
      decimal =str(float(B_Ent_Dec(num,base)+B_Frac_Dec(num,base)))
      return decimal

    #Hexadecimal separacion de parte entera y fraccional
    def Hex_Partes(num):

      tempEntero = ""
      tempFraccionario= ""
      digitosEnt = 0
      digitosFrac=0
      punto = True

      for i in range(len(num)-1): #Cuenta cuantos enteros hay, cuando encuentre un . pasa a contar cuantos fraccionarios hay
        if num[i] == '.':
          punto = False
        if punto == True:
          tempEntero += num[i]
          #print("TempEntero: ",tempEntero)
          digitosEnt += 1
        elif punto == False:  
          tempFraccionario += num[i+1]
          digitosFrac += 1
        #print("tempEntero final: ", tempEntero)
        #print("tempFraccionario final: ",tempFraccionario)  

      resultadoDeci = float(Hex_DeciEntero(tempEntero))+float(Hex_DeciFrac(tempFraccionario))
      return resultadoDeci

    def Hex_DeciEntero(tempEntero):
      decihex = int(tempEntero,16)
      return decihex

    def Hex_DeciFrac(tempFraccionario):
      deciHexFrac = 0
      conta = -1
      for i in range(len(tempFraccionario)):
        if tempFraccionario[i] == "A" or tempFraccionario[i] == "a":
          deciHexFrac += 10 * 16 ** (conta)
        elif tempFraccionario[i] == "B" or tempFraccionario[i] == "b":
          deciHexFrac += 11 * 16 ** (conta)
        elif tempFraccionario[i] == "C" or tempFraccionario[i] == "c":
          deciHexFrac += 12 * 16 ** (conta)
        elif tempFraccionario[i] == "D" or tempFraccionario[i] == "d":
          deciHexFrac += 13 * 16 ** (conta)
        elif tempFraccionario[i] == "E" or tempFraccionario[i] == "e":
          deciHexFrac += 14 * 16 ** (conta)
        elif tempFraccionario[i] == "F" or tempFraccionario[i] == "f":
          deciHexFrac += 15 * 16 ** (conta)
        else:
          deciHexFrac += int(tempFraccionario[i]) * 16 ** (conta)
        conta=conta-1

      return deciHexFrac
    #-------------------------------------------------------------------------------------------
    #Interfaz
    #Zona para definir comandos.
    def clearcomm():
        decimalT.delete("0", "end")
        binarioT.delete("0","end")
        OctadecimalT.delete("0","end")
        HexadecimalT.delete("0","end")
    #-------------------------------------------------------------------------------------------
    #creacion de ventana principal.
    ventana3 = Toplevel(conversiones) #crear una ventana siguiente de la ventana1
    ventana3.title("Calculadora Conversora")
    ventana3.resizable(0,0) #bloqueo de tamaño.

    Deci_Bin=StringVar()
    #-------------------------------------------------------------------------------------------
    #Creacion del frame.
    FrameV2=Frame(ventana3)
    FrameV2.pack()
    FrameV2.config(bg="light grey") #color de fondo.
    #-------------------------------------------------------------------------------------------
    #Labels (etiquetas).
    binarioL=Label(FrameV2, text="Binario:")
    binarioL.grid(row=0, column=0, sticky="w", padx=10, pady=10)
    binarioL.config(bg="light grey") #color de fondo.

    decimalL=Label(FrameV2, text="Decimal:")
    decimalL.grid(row=1, column=0, sticky="w", padx=10, pady=10)
    decimalL.config(bg="light grey") #color de fondo.

    OctadecimalL=Label(FrameV2,text="Octadecimal:")
    OctadecimalL.grid(row=2, column=0, sticky="w", padx=10, pady=10)
    OctadecimalL.config(bg="light grey") #color de fondo.

    HexadecimalL=Label(FrameV2, text="Hexadecimal:")
    HexadecimalL.grid(row=3, column=0, sticky="w", padx=10, pady=10)
    HexadecimalL.config(bg="light grey") #color de fondo.

    ResultadosL=Label(FrameV2)
    ResultadosL.grid(row=4, column=1, sticky="w", padx=10, pady=10)
    ResultadosL.config(bg="white") #color de fondo.
    #-------------------------------------------------------------------------------------------
    #Cajas de texto.
    binarioT=Entry(FrameV2)
    binarioT.grid(row=0, column=1, padx=10, pady=10)
    binarioT.config(justify="center")

    decimalT=Entry(FrameV2)
    decimalT.grid(row=1, column=1, padx=10, pady=10)
    decimalT.config(justify="center")

    OctadecimalT=Entry(FrameV2)
    OctadecimalT.grid(row=2, column=1, padx=10, pady=10)
    OctadecimalT.config(justify="center")

    HexadecimalT=Entry(FrameV2)
    HexadecimalT.grid(row=3, column=1, padx=10, pady=10)
    HexadecimalT.config(justify="center")
    #-------------------------------------------------------------------------------------------
    #Botones.
    CalcularB=Button(FrameV2, text="Calcular", command=evaluar)
    CalcularB.grid(row=5, column=1, pady=10)

    BorrarB=Button(FrameV2, text="Borrar", command=clearcomm)
    BorrarB.grid(row=5, column=0, pady=10)

    SalirB=Button(FrameV2, text="Volver", command=volver_ventana2)
    SalirB.grid(row=5, column=2, pady=10, padx=10)
    #-------------------------------------------------------------------------------------------
    if(ventana3):
      conversiones.withdraw()

    ventana3.mainloop() #es el ciclo para que la ventana "exista".
#Derivadas
def ventana4():
    global ventana4

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


    #-----------------------------------------------------------------------------------------------------
    #Interfaz grafica 
    #Ventana
    ventana4 = Toplevel(ventana1)
    ventana4.geometry ('600x600')
    ventana4.title("Cálculadora de Derivadas")
    #Titulo
    anuncio = Label(ventana4, text="Introduce una función de x:", font=("Arial", 15), fg="blue")
    anuncio.pack()

    #Campo de texto
    funcion = Entry(ventana4, font=("Arial", 15))
    funcion.pack()
    #Titulo
    anuncio2 = Label(ventana4, text="Introduce el valor x:", font=("Arial", 15), fg="blue")
    anuncio2.pack()
    #Campo de texto
    dato = Entry(ventana4, font=("Arial", 15))
    dato.pack()
    #Boton Derivar
    boton1 = Button(ventana4, text="Derivar Función", font=("Arial", 15), command=derivada)
    boton1.pack()
    #Boton derivada de la derivada
    boton4 = Button(ventana4, text="Derivar Función 2", font=("Arial", 15), command=derivada2)
    boton4.pack()


    #Etiquetas y Titulos:
    anuncioDeri = Label(ventana4, text="Primera derivada:", font=("Arial", 15), fg="blue")
    anuncioDeri.pack()

    etiqueta3 = Label(ventana4, text="[ ]", font=("Arial", 15), fg="red")
    etiqueta3.pack()

    anuncioResul = Label(ventana4, text="Primer resultado:", font=("Arial", 15), fg="blue")
    anuncioResul.pack()

    etiqueta = Label(ventana4, text="[ ]", font=("Arial", 15), fg="red")
    etiqueta.pack()

    anuncioDeri2 = Label(ventana4, text="Segunda derivada:", font=("Arial", 15), fg="blue")
    anuncioDeri2.pack()

    etiqueta4 = Label(ventana4, text="[ ]", font=("Arial", 15), fg="red")
    etiqueta4.pack()

    anuncioResul2 = Label(ventana4, text="Segundo resultado:", font=("Arial", 15), fg="blue")
    anuncioResul2.pack()

    etiqueta2 = Label(ventana4, text="[ ]", font=("Arial", 15), fg="red")
    etiqueta2.pack()


    def _quit(): #Función salir
        ventana4.quit()     # detiene mainloop
        ventana4.destroy()  # elimina la ventana de la memoria

    def _graph():
        #-----------------------------------------------------------------------
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
    button3 = Button(master=ventana4, text="Volver", font=("Arial", 15), command=volver_ventana3)
    button3.pack()

    buttonGraph = Button(master=ventana4, text="Graficar",font=("Arias",15),command=_graph)
    buttonGraph.pack()

    if(ventana4):
            ventana1.withdraw()
    ventana4.mainloop()
#Falsa posicion
def ventana5():
    global ventana5

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
        top=Toplevel(ventana5)
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
    ventana5 = Toplevel(raices)
    ventana5.title("Falsa posicion")
    ventana5.resizable(0,0) #bloqueo de tamaño.
    #Ventana.iconbitmap('calculadora.ico') #icono.
    #-------------------------------------------------------------------------------------------
    #Creacion del frame.
    FrameV=Frame(ventana5)
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

    SalirB=Button(FrameV, text="Volver", command=volver_ventana4)
    SalirB.grid(row=8, column=2, pady=10, padx=10)
    #-------------------------------------------------------------------------------------------
    if(ventana5):
        raices.withdraw()
    ventana5.mainloop() #es el ciclo para que la ventana "exista"
#IEEE
def ventana6():
    global ventana6

    #Variables globables
    contador=52 #repeticiones de multiplicacion
    numOption=0

    bucle=1

    def butt():
      deci = decimalT.get()

      sig32 = Signo32.get()
      expon32 = Exponente32.get()
      manti32 = Mantisa32.get()

      sig64 = Signo64.get()
      expon64 = Exponente64.get()
      manti64 = Mantisa64.get()

      if deci != '' and deci != None:
        Deci_IEEE(float(deci))
      elif expon32 != '' and deci != None:
        IEEE_Deci(int(sig32),expon32,manti32,126,127)
      elif expon64 != '' and deci != None:
        IEEE_Deci(int(sig64),expon64,manti64,1022,1023)

    #Funciones para separar entero de decimal
    def parteEntera(num):
      fraccion,entero = math.modf(num)
      return int(entero)

    def parteFraccion(num):
      fraccion,entero = math.modf(num)
      return round(fraccion,10)

    #Decimal Entero a Binario
    def Deci_Ent_Binario(num):
      entero = parteEntera(num)
      binariop1 = format(entero,'0b') #format retira el 0b del resultado, se ve mas estetico
      return binariop1

    def soloEnteroIEEE(num): #Para decimal a ieee
      entero = list(num)  
      entero = entero.index[:entero.index('.')] #quita todo despues del punto, solo deja entero asi
      entero = str(entero)
      return entero

    #Decimal Fraccional a Binario
    def Deci_Frac_Bin(num):
      fraccion = parteFraccion(num)
      binariop2= ""
      cuenta = 0

      while cuenta != contador:
        multiplicacion = fraccion * 2
        binariop2 = binariop2 + str(parteEntera(multiplicacion))
        fraccion = parteFraccion(multiplicacion)
        cuenta += 1
      return binariop2

    #Decimal a Binario, Esta es la funcion que se llama en el case
    def Deci_Binario(num):
      binarioFinal = str(Deci_Ent_Binario(num)+'.'+str(Deci_Frac_Bin(num)))
      return binarioFinal

    #Base 2 u 8 Entera a Decimal
    def B_Ent_Dec(num, base):
      entero=str(parteEntera(num))
      decimal = 0

      for pos, digito in enumerate(entero[::-1]):
        decimal += int(digito) * base ** pos
      return decimal

    #Base 2 u 8 Fraccionario a Decimal
    def B_Frac_Dec(numero,base):
    #  fraccion = parteFraccion(numero)
    #  cuenta=0
    #  while cuenta!=contador:
    #    fraccion = fraccion*10
    #    cuenta+=1
      caracteres = str(numero)
      caracteres = list(caracteres)
      for i in range(2): #ejecuta la linea dos veces
        del caracteres[0]
      
      #print("Fraccion en B_Frac_Dec: ", caracteres)

      decimal = 0
      pos = 1

      for pos,digito in enumerate(caracteres):
        decimal += float(digito)*(float(base**(-pos-1)))
      return decimal

    #Base 2 u 8 a Decimal
    def B_Dec(num,base):
      decimal =str(Decimal(B_Ent_Dec(num,base)+B_Frac_Dec(num,base)))
      return decimal

    #Decimal a IEEE

    #Signo de IEEE 754
    def signo (numero):
        if numero >= 0:
            signo = 0
        else:
            signo = 1
        return signo

    #Mantisa de IEEE 754
    def mantisa(numero, bits):
        binaSTR = ""
        respuesta = ""
        mantisa = ""
        if numero <0: #Si es negativo se pasa a positivo
            numero = numero * -1    
        binario = Decimal(Deci_Binario(numero))
        binaSTR = str(binario) #establecemos la variable inicial como una cadena de caracteres
        #print("Inicio: ",binario)
        while (parteEntera(binario)) != 1 :
            
            binario = (binario / 10) #se utiliza para correr las comas 
            #print(binario)
        respuesta = Decimal(binario)   
        if bits == 23:
          mantisa = str(respuesta)[2:24] #excluimos los primeros dos caracteres de la cadena y hasta completar los bits
        if bits == 52:
          mantisa = str(respuesta)[2:53] #excluimos los primeros dos caracteres de la cadena y hasta completar los bits
        ceros = ""
      
        for i in range (0, (bits-len(mantisa)), 1):
            ceros = ceros + "0"

        mantisaFinal = str(mantisa) + ceros
        return mantisaFinal

    def exponente (num,const):
        if num <0: #Si es negativo se pasa a positivo
          num = num * -1
        binario = Decimal(Deci_Binario(num))
        vecesExpo = parteEntera(binario)
        digitos = str(vecesExpo)
        vecescomas = 0
        for i in range(len(digitos)-1):
            vecescomas +=1        
        expo = const + vecescomas
        resul = Deci_Ent_Binario(expo)
        lista = list(resul) #convierte el resultado a una lista para tener cada digito

        if const == 127: #32 bits
          while len(lista)<8: #si el binario no tiene 8 digitos:
            lista.insert(0, '0') #añade cero a la izquierda hasta que se completen los bits necesarios
        elif const == 1023: #64 bits
          while len(lista)<11: #si el binario no tiene 11 digitos:
            lista.insert(0, '0') #añade cero a la izquierda hasta que se completen los bits necesarios
        
        resulFinal = ''.join(lista) #lo convierte a string nuevamente
        return resulFinal

    def Deci_IEEE(num):
      Signo32.insert(0,signo(num))
      Exponente32.insert(0, exponente(num,127))
      Mantisa32.insert(0, mantisa(num,23))

      Signo64.insert(0,signo(num))
      Exponente64.insert(0, exponente(num,1023))
      Mantisa64.insert(0, mantisa(num,52))
      
      print("IEEE 32 bits: ",signo(num),"",exponente(num,127)," ",mantisa(num,23)) ##const, bits
      print("IEEE 64 bits", signo(num)," ", exponente(num, 1023), " ",mantisa(num,52)) ##const, bits

    #IEEE a decimal
    def IEEE_Deci (signo, exponente, mantisa, const1,const2):
      IEEEDecimal=0
      listaExp=list(exponente)
      listaMan=list(mantisa)
      unosExp=0
      unosMan=0
    
      if (signo==1):
        signoDec="-"
      else:
        signoDec=""

      for i in range (len(listaMan)):
        unosMan+=int(listaMan[i]) #Cuenta valores de mantisa

      for i in range (len(listaExp)):
        unosExp+=int(listaExp[i])  #Cuenta valores de exponente
      
      if (unosExp==0 and unosMan==0):
        IEEEDecimal=0

        
        decimalT.insert(0, (signoDec + str(IEEEDecimal)))

      if (unosExp==0 and unosMan!=0):
        manSTR="0."+str(mantisa)
        numMan=float(manSTR)
        numManDec=B_Dec(numMan,2)
        IEEEDecimal=float(numManDec)*2**(-const1)
        print("Decimal:",signoDec,IEEEDecimal)
        decimalT.insert(0, (signoDec + str(IEEEDecimal)))

      if (unosExp>0 and unosMan>0):
        manSTR="1."+str(mantisa)
        numMan=Decimal(manSTR)
        numManDec=B_Dec(numMan,2)
        expo=B_Ent_Dec(int(exponente),2)
        eVar=expo-const2
        IEEEDecimal=float(numManDec)*2**(eVar) 
        print("Decimal:",signoDec,IEEEDecimal)
        decimalT.insert(0, (signoDec + str(IEEEDecimal)))

      if((unosExp==8 or unosExp==11 )and unosMan==0):
        print("Decimal:",signoDec,"∞")
        decimalT.insert(0, "∞")

      if((unosExp==8 or unosExp==11) and unosMan!=0):
        print("Decimal:","NaN")
        decimalT.insert(0, "NaN")
      

    #-------------------------------------------------------------------------------------------
    #Zona para definir comandos.
    def clearcomm():
        decimalT.delete("0", "end")
        Signo32.delete("0","end")
        Exponente32.delete("0","end")
        Mantisa32.delete("0","end")
        Signo64.delete("0","end")
        Exponente64.delete("0","end")
        Mantisa64.delete("0","end")
    #-------------------------------------------------------------------------------------------
    #creacion de ventana principal.
    ventana6 = Toplevel(conversiones)
    ventana6.title("Calculadora IEEE")
    ventana6.resizable(0,0) #bloqueo de tamaño.
    #-------------------------------------------------------------------------------------------
    #Creacion del frame.
    FrameV=Frame(ventana6)
    FrameV.pack()
    FrameV.config(bg="light grey") #color de fondo.
    #-------------------------------------------------------------------------------------------
    #Labels (Etiquetas).
    DecimalL=Label(FrameV, text="Decimal:")
    DecimalL.grid(row=0, column=0, padx=10, pady=10)
    DecimalL.config(bg="light grey") #color de fondo.

    #32 bits.
    IeeL32=Label(FrameV, text="IEE 32 bits")
    IeeL32.grid(row=1, column=1)
    IeeL32.config(bg="light grey") #color de fondo.

    Signo32_L=Label(FrameV, text="Signo:")
    Signo32_L.grid(row=2, column=0, pady=5, padx=5)
    Signo32_L.config(bg="light grey") #color de fondo.

    Exponente32_L=Label(FrameV, text="Exponente:")
    Exponente32_L.grid(row=3, column=0, pady=5, padx=5)
    Exponente32_L.config(bg="light grey") #color de fondo.

    Mantisa32_L=Label(FrameV, text="Mantisa:")
    Mantisa32_L.grid(row=4, column=0, pady=5, padx=5)
    Mantisa32_L.config(bg="light grey") #color de fondo.

    #64 bits.
    IeeL64=Label(FrameV, text="IEE 64 bits")
    IeeL64.grid(row=5, column=1)
    IeeL64.config(bg="light grey") #color de fondo.

    Signo64_L=Label(FrameV, text="Signo:")
    Signo64_L.grid(row=6, column=0, pady=5, padx=5)
    Signo64_L.config(bg="light grey") #color de fondo.

    Exponente64_L=Label(FrameV, text="Exponente:")
    Exponente64_L.grid(row=7, column=0, pady=5, padx=5)
    Exponente64_L.config(bg="light grey") #color de fondo.

    Mantisa64_L=Label(FrameV, text="Mantisa:")
    Mantisa64_L.grid(row=8, column=0, pady=5, padx=5)
    Mantisa64_L.config(bg="light grey") #color de fondo.
    #-------------------------------------------------------------------------------------------
    #Cajas de texto.
    decimalT=Entry(FrameV)
    decimalT.grid(row=0, column=1, padx=10, pady=10)
    decimalT.config(justify="center")

    #32 bits.
    Signo32=Entry(FrameV)
    Signo32.grid(row=2, column=1, padx=10, pady=10)
    Signo32.config(justify="center")

    Exponente32=Entry(FrameV)
    Exponente32.grid(row=3, column=1, padx=10, pady=10)
    Exponente32.config(justify="center")

    Mantisa32=Entry(FrameV)
    Mantisa32.grid(row=4, column=1, padx=10, pady=10)
    Mantisa32.config(justify="center")

    #64 bits.
    Signo64=Entry(FrameV)
    Signo64.grid(row=6, column=1, padx=10, pady=10)
    Signo64.config(justify="center")

    Exponente64=Entry(FrameV)
    Exponente64.grid(row=7, column=1, padx=10, pady=10)
    Exponente64.config(justify="center")

    Mantisa64=Entry(FrameV)
    Mantisa64.grid(row=8, column=1, padx=10, pady=10)
    Mantisa64.config(justify="center")
    #-------------------------------------------------------------------------------------------
    #Botones.
    CalcularB=Button(FrameV, text="Calcular", command=butt)
    CalcularB.grid(row=9, column=1, pady=10)

    BorrarB=Button(FrameV, text="Borrar", command=clearcomm)
    BorrarB.grid(row=9, column=0, pady=10)

    SalirB=Button(FrameV, text="Volver", command=volver_ventana5)
    SalirB.grid(row=9, column=2, pady=10, padx=10)
    #-------------------------------------------------------------------------------------------
    if(ventana6):
      conversiones.withdraw()
    ventana6.mainloop() #es el ciclo para que la ventana "exista"
#Newton
def ventana7():
  global ventana7


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
               
    #-------------------------------------------------------------------------------------------
  #Zona para definir comandos.
  def clearcomm():
      FuncionX.delete("0", "end")
      PuntoX.delete("0","end")
      ErrorT.delete("0","end")
      ResultadoT.delete("0","end")
      
  def tabla():
      top=Toplevel(ventana7)
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
  ventana7 = Toplevel(raices)
  ventana7.title("Calculadora Newton")
  ventana7.resizable(0,0) #bloqueo de tamaño.
  #ventana7.iconbitmap('Interfaz\calculadora.ico') #icono.
  #-------------------------------------------------------------------------------------------
  #Creacion del frame.
  FrameV=Frame(ventana7)
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

  SalirB=Button(FrameV, text="Volver", command=volver_ventana6)
  SalirB.grid(row=6, column=2, pady=10, padx=10)
  #-------------------------------------------------------------------------------------------
  if(ventana7):
          raices.withdraw()
  ventana7.mainloop() #es el ciclo para que la ventana "exista"
#Polinomio
def ventana8():
  global ventana8
  
  resul = 0
  arra= []
  nums = []

  def grafica():
    x=symbols('x')
    z=0
    funcion=parse_expr(Tcuadratico.get())
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

  def cambio(arr):
      
    print(arr)
    arr2 = [""]
    print("--------")
    val = len(arr)
    for i in range(0,val-1, 1):
        arr2.append("")
    for i in range(0, val, 1):

        arr2[i] = arr[(val-1)-i]
        print(arr[(val-1)-i])
        #print("--------")
    return arr2
    #print (arr2)

  def Vnum():
    #ejemplos = ["4x**4+3x**3+5x**2-2x+2"]
    nums.append(Tcuadratico.get())
    for e in nums:
      print(e, "\n ", coefs(e))
      arra.append(coefs(e))
    print(cambio(arra[0]))
    ResultadoT.insert(0, cambio(arra[0]))

  def coefs(entrada):
    regexp = r"(-?\d*)(x?)(?:(?:\^|\*\*)(\d))?"
    c = {}
    for coef, x, exp in re.findall(regexp, entrada):
      # print(coef, x, exp)
      if not coef and not x:
        continue
      if x and not coef:
        coef = '1'
      if x and coef == "-":
        coef = "-1"
      if x and not exp:
        exp = '1'
      if coef and not x:
        exp = '0'
      exp = ord(exp) & 0x000F
      c[exp] = float(coef)
    grado = max(c)
    coeficientes = [0.0] * (grado+1)
    for g, v in c.items():
      coeficientes[g] = v

      print("los coe son: ",coeficientes[g])

      raices = sp.roots(coeficientes)
      print("las raices son:")
      for i in raices:
              print(i)
      print("raices como arreglo:")

    return raices
      
 #-------------------------------------------------------------------------------------------
  #Zona para definir comandos.
  def clearcomm():
      Tcuadratico.delete("0", "end")
      ResultadoT.delete("0","end")
  #-------------------------------------------------------------------------------------------
  #creacion de ventana principal.
  ventana8 = Toplevel(raices)
  ventana8.title("Calculadora Polinomios")
  ventana8.resizable(0,0) #bloqueo de tamaño.
  #Ventana.iconbitmap('Interfaz\calculadora.ico') #icono.
  #-------------------------------------------------------------------------------------------
  #Creacion del frame.
  FrameV=Frame(ventana8)
  FrameV.pack()
  FrameV.config(bg="light grey") #color de fondo.
  #-------------------------------------------------------------------------------------------
  Aviso_L=Label(FrameV, text="Ejemplo de como escribir el polinomio: a*x**2+b*x+c")
  Aviso_L.grid(row=1, column=1, padx=10, pady=10)
  Aviso_L.config(bg="light grey") #color de fondo.

  Tcuadratico_L=Label(FrameV, text="Polinomio:")
  Tcuadratico_L.grid(row=2, column=0, padx=5, pady=5)
  Tcuadratico_L.config(bg="light grey") #color de fondo.

  Resultado_L=Label(FrameV, text="Resultado:")
  Resultado_L.grid(row=3, column=0, padx=5, pady=5)
  Resultado_L.config(bg="light grey") #color de fondo.
  #-------------------------------------------------------------------------------------------
  #Cajas de texto.
  Tcuadratico=Entry(FrameV)
  Tcuadratico.grid(row=2, column=1, padx=5, pady=5)
  Tcuadratico.config(justify="center")

  ResultadoT=Entry(FrameV)
  ResultadoT.grid(row=3, column=1, sticky=S+N+E+W)

  ResultadoT.config(justify="center")
  #ResultadoT.config(state=DISABLED)
  #-------------------------------------------------------------------------------------------
  #Botones.
  BorrarB=Button(FrameV, text="Borrar", command=clearcomm)
  BorrarB.grid(row=4, column=0, pady=10)

  CalcularB=Button(FrameV, text="Calcular", command=Vnum)
  CalcularB.grid(row=4, column=1, pady=10, padx=10)

  GraficaB=Button(FrameV, text="Graficar", command= grafica)
  GraficaB.grid(row = 5, column= 1, padx=10, pady=10)

  SalirB=Button(FrameV, text="Volver", command=volver_ventana7)
  SalirB.grid(row=4, column=2, pady=10, padx=10)
  #-------------------------------------------------------------------------------------------
  if(ventana8):
        raices.withdraw()
  ventana8.mainloop() #es el ciclo para que la ventana "exista"
#Secantes
def ventana9():
  global ventana9

  xS = symbols('x')
  #def f(x):
  lista1=[0,0,0,0]
  lista2=[]

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
      top=Toplevel(ventana9)
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
  ventana9 = Toplevel(raices)
  ventana9.title("Calculadora Secante")
  ventana9.resizable(0,0) #bloqueo de tamaño.
  #Ventana.iconbitmap('calculadora.ico') #icono.
  #-------------------------------------------------------------------------------------------
  #Creacion del frame.
  FrameV=Frame(ventana9)
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
  BorrarB.grid(row=8, column=2, pady=10)

  CalcularB=Button(FrameV, text="Calcular", command=evaluar)
  CalcularB.grid(row=8, column=1, pady=10, padx=10)

  GraficaB=Button(FrameV, text="Graficar", command= grafica)
  GraficaB.grid(row = 8, column= 0, padx=10, pady=10)

  TablaB=Button(FrameV, text="Ver Iteraciones", command=tabla)
  TablaB.grid(row=9, column=0, pady=10, padx=20)

  SalirB=Button(FrameV, text="Volver", command=volver_ventana8)
  SalirB.grid(row=9, column=2, pady=10, padx=10)
  #-------------------------------------------------------------------------------------------
  if(ventana9):
          raices.withdraw()
  ventana9.mainloop() #es el ciclo para que la ventana "exista"
#MonteCarlo
def ventana10():
  global ventana10

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
      
  #maincanv-------------------------------------------------------------------------------------------------
  ventana10 = Toplevel(integracion)
  ventana10.title("Calculadora Monte Carlo")
  ventana10.resizable(0,0)
  #FrmCr----------------------------------------------------------------------------------------------------
  mFrame = Frame(ventana10)
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

  SalirB=Button(mFrame, text="Volver", command=volver_ventana9)
  SalirB.grid(row=8, column=1, pady=10, padx=10)

  if(ventana10):
        integracion.withdraw()
  ventana10.mainloop()
#Simpson
def ventana11():
  global ventana11  

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
  ventana11 = Toplevel(integracion)
  ventana11.title("Calculadora")
  ventana11.resizable(0,0)
  #FrmCr----------------------------------------------------------------------------------------------------
  mFrame = Frame(ventana11)
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

  Salir = Button(mFrame, text="Volver", command=volver_ventana10)
  Salir.grid(row=8, column=1, padx=10, pady=10)
  #----------------------------------------------------------------------------------------------------------
  if(ventana11):
          integracion.withdraw()
  ventana11.mainloop()
#Simpson38
def ventana12():
  global ventana12

  x = symbols('x')
  bucle=1

  def Multiplo3(partinum):
      if(partinum%3==1):
          partinum+=2 #Si el residuo es 1 sumale 2 a partinum
          print("numero de particiones ajustado a: ",partinum)

      if(partinum%3==2):
          partinum+=1 #Si el residuo es 2 sumale 1 a partinum
          print("numero de particiones ajustado a: ",partinum)
      return partinum

  def Simpson38(ecua, aVal, bVal, partinum):
      area=0
      areasucesion=0
      jmas=0
      listaFX=[]
      #suma separa las particiones de la primera y la ultima
      suma=0
      suma2=0
      sumaloka=0

      expr = parse_expr(ecua) #resuelve la funcion

      #numero h
      h = (bVal-aVal)/partinum

      #area
      for n in range(0,partinum+1,1): #Empieza desde 0, con el +1 el rango no excluye a partinum 
          
          jmas = aVal+(h*n)
          areasucesion=(expr.subs(x,jmas))
          listaFX.append(areasucesion)
          
      
      for u in range(1,partinum,1):
          if(u%3==0):
              sumaloka+=2*(listaFX[u])  
          else:
              suma+=3*(listaFX[u]) 
      
      suma2=listaFX[0]+listaFX[partinum]
      
      area=((3/8)*h)*(suma2+suma+sumaloka)

      return area
      print("Integral:", area) 

  def CalcuError(ecua, aVal, bVal, parti): #Calcula el error
      expr = parse_expr(ecua)
      deriv = diff(expr, x, 4) #funcion, qué variable, hasta qué derivada

      h = (bVal-aVal)/parti
      print("h en error: ",h)

      aleatorio = random.uniform(aVal,bVal)
      derivAleatorio = deriv.subs(x, aleatorio) #evalua f(x) donde f(x) es la cuarta derivada y x es random

      errorSimp = (-3*(h**5)/80)*derivAleatorio

      return errorSimp

  def calcall():
      ec = ecX.get()
      vala = aVal.get()
      valb = bVal.get()
      pt = Multiplo3(int(ptNo.get()))
      
      vala = float(vala)
      valb = float(valb)
      pt = int(pt)

      anLp.configure(text=pt)
      anLI.configure(text=Simpson38(ec,vala,valb,pt))
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
  ventana12 = Toplevel(integracion)
  ventana12.title("Calculadora")
  ventana12.resizable(0,0)
  #FrmCr----------------------------------------------------------------------------------------------------
  mFrame = Frame(ventana12)
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

  Salir = Button(mFrame, text="Volver", command=volver_ventana11)
  Salir.grid(row=8, column=1, padx=10, pady=10)
  #----------------------------------------------------------------------------------------------------------
  if(ventana12):
          integracion.withdraw()
  ventana12.mainloop()
#Trapecio
def ventana13():
  global ventana13

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
  ventana13 = Toplevel(integracion)
  ventana13.title("Calculadora trapecio")
  #Ventana.resizable(0,0)
  #-------------------------------------------------------------------------------------------
  #Creacion del frame.
  FrameV=Frame(ventana13)
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

  Salir = Button(FrameV, text="Volver", command=volver_ventana12)
  Salir.grid(row=7, column=1, padx=10, pady=10)

  Graficar = Button(FrameV, text="Graficar", command=grafica)
  Graficar.grid(row=6, column=0, padx=10, pady=10)

  Borrar = Button(FrameV, text="Borrar", command=clearcomm)
  Borrar.grid(row=6, column=2, padx=10, pady=10)
  #-------------------------------------------------------------------------------------------
  if(ventana13):
          integracion.withdraw()
  ventana13.mainloop()
#Rectangulos
def ventana14():

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

  #maincanv-------------------------------------------------------------------------------------------------
  ventana14 = Toplevel(integracion)
  ventana14.title("Calculadora")
  ventana14.resizable(0,0)
  #FrmCr----------------------------------------------------------------------------------------------------
  mFrame = Frame(ventana14)
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

  fn1 = Button(mFrame, text="Volver", command=volver_ventana13)
  fn1.grid(row=7, column=2, padx=10,pady=10)

  if(ventana14):
    integracion.withdraw()
  ventana14.mainloop()
#Matrices
def ventana15():
  global ventana15

  inp = []
  txtv = []
  txta = []
  lb1 = []
  lb2 = []
  res = []
  res2 = []
  matrice = []
  matrice2 = []

  #Funciones de operaciones ---------------------------------------------------------------------------------
  def SaveMT():
    
    x = int(FilaM_T.get())
    y = int(ColumnM_T.get())
    x1 = int(FilaM_T2.get())
    y1 = int(ColumnM_T2.get())

    for i in range(x):
      matrice.append([])
      for j in range(y):
        try:
          matrice[i].append(float(inp[i][j].get()))
        except:
          pass

    for i in range(x1):
      matrice2.append([])
      for j in range(y1):
        try:
          matrice2[i].append(float(res[i][j].get()))
        except:
          pass            
    
    print(matrice)
    print(matrice2)

  def Suma():
    if len(matrice) == len(matrice2) and len(matrice[0]) == len(matrice2[0]):
      matrizResul = []
      for i in range(len(matrice)):
        matrizResul.append([])
        for j in range(len(matrice[0])):
          matrizResul[i].append(matrice[i][j] + matrice2[i] [j])

      print("\nResultado:\n")
      for fila in matrizResul :
        print("[", end=" ")
        for elemento in fila:
            print("{}".format(elemento), end=" ")
        print("]")
      print(len(matrizResul[0]))
      print(len(matrizResul))
      ansgen(int(len(matrizResul)), len(matrizResul[0]), matrizResul)
    else:
      print("No se puede operar")

  def Resta():
    if (len(matrice)==len(matrice2) and len(matrice[0])==len(matrice2[0])):
      matrizResul=[]

      for t in range (len(matrice)):
        matrizResul.append([])
        for m in range (len(matrice[0])):
          matrizResul[t].append(matrice[t][m]-matrice2[t][m])
      
      print("\nResultado:\n")
      for fila in matrizResul :
        print("[", end=" ")
        for elemento in fila:
          print("{}".format(elemento), end=" ")
        print("]")
      print(len(matrizResul[0]))
      print(len(matrizResul))
      ansgen(int(len(matrizResul)), len(matrizResul[0]), matrizResul)
        
    else:
      print("No se puede operar")

  def Multi():
    matrizResul=[]
    #crear matriz vacia matrizResul
    for i in range(len(matrice)): #que tenga el numero de filas de matriz1
      matrizResul.append([])
      for l in range(len(matrice2[0])): #y el numero de columnas de matriz2
        matrizResul[i].append(0)

    if(len(matrice[0])==len(matrice2)): #Solo multiplicar cuando el num de columnas de matriz1 sea el mismo que el num de filas de matriz2
      #Recorre los indices de las matrices 1 y 2 para llenar matrizFin 
      for n in range(len(matrice)):
        for m in range(len(matrice2[0])): 
          for o in range(len(matrice[0])):
            matrizResul[n][m] += matrice[n][o]*matrice2[o][m]

      print(len(matrizResul[0]))
      print(len(matrizResul))
      ansgen(int(len(matrizResul)), len(matrizResul[0]), matrizResul)
    else:
      print("las columnas de la matriz 1 no encajan con las filas de la matriz 2.")

  def Escalar():
    matrizResul=[]
    for i in range (len(matrice)): #crear matrizResul vacia con la misma longitud de matrice
      matrizResul.append([0]*len(matrice[0]))
    for i in range (len(matrice)):
      for j in range (len(matrice[0])):
        matrizResul[i][j]=matrice[i][j]*(matrice2[0][0])

    print("\nResultado:\n")
    for fila in matrizResul :
      print("[", end=" ")
      for elemento in fila:
        print("{}".format(elemento), end=" ")
      print("]")
    ansgen(int(len(matrizResul)), len(matrizResul[0]), matrizResul)

  def Inversa():
    matrizResul=[]
    matrizResul = np.linalg.inv(matrice)
    print("\nResultado:\n")
    for fila in matrizResul :
      print("[", end=" ")
      for elemento in fila:
        print("{}".format(elemento), end=" ")
      print("]")
    print(len(matrizResul[0]))
    print(len(matrizResul))
    ansgen(int(len(matrizResul)), len(matrizResul[0]), matrizResul)


  def Transpuesta():
    transp=[]

    for x in range (len(matrice[0])):
      transp.append([])
      for y in range (len(matrice)):
        transp[x].append(matrice[y][x])

    print("\nMatriz original:\n")
    for fila in matrice :
      print("[", end=" ")
      for elemento in fila:
        print("{}".format(elemento), end=" ")
      print("]")

    print("\nResultado:\n")
    for fila in transp :
      print("[", end=" ")
      for elemento in fila:
        print("{}".format(elemento), end=" ")
      print("]")

  def Gauss():
    m = len(matrice2[0])
    x = np.zeros(m)
    if(len(matrice2)==1 and len(matrice2[0])==len(matrice)): #El vector debe tener el mismo num de columnas que el num de filas de m1
      for k in range(0, m):
          for r in range(k+1, m):
            factor=(matrice[r][k]/matrice[k][k])
            matrice2[0][r]=matrice2[0][r]-(factor*matrice2[0][k])
            for c in range(0,m):
              matrice[r][c]=matrice[r][c]-(factor*matrice[k][c])
      x[m-1]=(matrice2[0][m-1])/(matrice[m-1][m-1])

      for r in range(m-2, -1, -1):
        suma = 0
        for c in range(0,m):
          suma=suma+matrice[r][c]*x[c]
        x[r]=(matrice2[0][r]-suma)/matrice[r][r] 
            
        print(x)

        #for fila in x:
            #matrizResul.append(x[fila])
        matrizResul = Label(FrameAbajo2, text=str(x), bg="light gray") #No encontré como llamarlo con ansgen porque sacaba error x has no len()
        matrizResul.grid(row=3, column=4, padx=10, pady=10)
        #ansgen(int(len(matrizResul)), len(matrizResul), matrizResul) 
    else:
        print("No se puede realizar GJ,numero de columnas en M1 erroneo o M2 debe ser un vector (solo una fila)")

  #Ventana Operaciones---------------------------------------------------------------------------------------
  def fgen():
    #Matrix 1----------------------------------------------------------------------
    x = int(FilaM_T.get())
    y = int(ColumnM_T.get())
    val = 0
    for i in range(x+1):        
      for j in range(y+1):
          if (i == 0 or j == 0) and not(i == 0 and j == 0):
              if i == 0:
                lb1.append(Label(FrameAbajo, text="col " + str(j), bg="gray"))
                lb1[val].grid(row=i+1, column=j+1, padx=10, pady=10)
                val+=1
              if j == 0:
                lb1.append(Label(FrameAbajo, text="fila " + str(i), bg="gray"))
                lb1[val].grid(row=i+1, column=j+1, padx=10, pady=10)
                val+=1
          elif i == 0 and j == 0:
              lb1.append(Label(FrameAbajo, text=" ... ", bg="gray"))
              lb1[val].grid(row=i+1, column=j+1, padx=10, pady=10)
              val+=1
    
    for i in range(x):
      txtv.append([])
      inp.append([])
      for j in range(y):
        txtv[i].append(StringVar)
        inp[i].append(Entry(FrameAbajo, textvariable=txtv[i][j]))
        inp[i][j].grid(row=i+2, column=j+2, padx=10, pady=10)
    

    #Matrix 2----------------------------------------------------------------------
    x1 = int(FilaM_T2.get())
    y1 = int(ColumnM_T2.get())
    val = 0
    for i in range(x1+1):        
        for j in range(y1+1):
            if (i == 0 or j == 0) and not(i == 0 and j == 0):
                if i == 0:
                  lb2.append(Label(FrameAbajo, text="col " + str(j),  bg="gray"))
                  lb2[val].grid(row=i+1, column=y+j+4, padx=10, pady=10)
                  val+=1
                if j == 0:
                  lb2.append(Label(FrameAbajo, text="fila " + str(i), bg="gray"))
                  lb2[val].grid(row=i+1, column=y+j+4, padx=10, pady=10)
                  val+=1
            elif i == 0 and j == 0:
                lb2.append(Label(FrameAbajo, text=" ... ", bg="gray"))
                lb2[val].grid(row=i+1, column=y+j+4, padx=10, pady=10)
                val+=1
    for i in range(x1):
        txta.append([])
        res.append([])

        for j in range(y1):
          txta[i].append(StringVar)
          res[i].append(Entry(FrameAbajo, textvariable=txta[i][j]))
          res[i][j].grid(row=i+2, column=y+j+5, padx=10, pady=10)

  def ansgen(x, y, v):
    res2 
    for i in range(x):
        res2.append([])
        for j in range(y):
          res2[i].append(Label(FrameAbajo2, text=str(v[i][j]), bg="light gray"))
          res2[i][j].grid(row=i+1, column=j+1, padx=10, pady=10)


  #-------------------------------------------------------------------------------------------
  #Zona para definir comandos.
  def clearcomm():
      FilaM_T.delete("0", "end")
      ColumnM_T.delete("0","end")
      FilaM_T2.delete("0", "end")
      ColumnM_T2.delete("0","end")
      for i in range(len(res2)):
          for j in range(len(res2[0])):
              res2[i][j].config(text="")
  #-------------------------------------------------------------------------------------------
  #creacion de ventana principal.  
  ventana15 = Toplevel(ventana1)
  ventana15.title("Matrix")
  ventana15.config(bg="light grey")

  #Ventana.resizable(0,0)
  #-------------------------------------------------------------------------------------------
  #Creacion del frame.
  FrameV=Frame(ventana15)
  FrameV.pack()
  FrameV.config(bg="light grey")

  FrameAbajo = Frame(ventana15)
  FrameAbajo.pack()
  FrameAbajo.config(bg="gray")

  FrameAbajo2 = Frame(ventana15)
  FrameAbajo2.pack()
  FrameAbajo2.config(bg="light gray")
  #-------------------------------------------------------------------------------------------
  #Etiquetas
  FilaM = Label(FrameV, text="Numero de filas matrix")
  FilaM.grid(row=1, column=0, padx=10, pady=10)
  FilaM.config(bg="light grey")

  ColumnM = Label(FrameV, text="Numero de columnas matrix")
  ColumnM.grid(row=2, column=0, padx=10, pady=10)
  ColumnM.config(bg="light grey")

  FilaM2 = Label(FrameV, text="Numero de filas matrix 2")
  FilaM2.grid(row=3, column=0, padx=10, pady=10)
  FilaM2.config(bg="light grey")

  ColumnM2 = Label(FrameV, text="Numero de columnas matrix 2")
  ColumnM2.grid(row=4, column=0, padx=10, pady=10)
  ColumnM2.config(bg="light grey")
  #-------------------------------------------------------------------------------------------
  #Cajas de texto
  FilaM_T = Entry(FrameV)
  FilaM_T.grid(row=1, column=1, padx=10, pady=10)
  FilaM_T.config(justify="center")

  ColumnM_T = Entry(FrameV)
  ColumnM_T.grid(row=2, column=1, padx=10, pady=10)
  ColumnM_T.config(justify="center")

  FilaM_T2 = Entry(FrameV)
  FilaM_T2.grid(row=3, column=1, padx=10, pady=10)
  FilaM_T2.config(justify="center")

  ColumnM_T2 = Entry(FrameV)
  ColumnM_T2.grid(row=4, column=1, padx=10, pady=10)
  ColumnM_T2.config(justify="center")
  #-------------------------------------------------------------------------------------------
  #Botones
  calcular = Button(FrameV, text="Crear", command=fgen)
  calcular.grid(row=7, column=1, padx=10, pady=10)

  Salir = Button(FrameV, text="Volver", command=volver_ventana14)
  Salir.grid(row=7, column=2, padx=10, pady=10)

  Borrar = Button(FrameV, text="Borrar", command=clearcomm)
  Borrar.grid(row=7, column=0, padx=10, pady=10)
  #-------------------------------------------------------------------------------------------
  #Botones Operaciones

  bt1 = Button(FrameV, text="Sumar", command=Suma)
  bt1.grid(row=1, column=4, padx=10, pady=10)

  bt2 = Button(FrameV, text="Restar", command=Resta)
  bt2.grid(row=1, column=5, padx=10, pady=10)

  bt3 = Button(FrameV, text="Multiplicar", command=Multi)
  bt3.grid(row=2, column=4, padx=10, pady=10)

  bt4 = Button(FrameV, text="Por Escalar M1", command=Escalar)
  bt4.grid(row=2, column=5, padx=10, pady=10)

  bt5 = Button(FrameV, text="Inversa M1", command=Inversa)
  bt5.grid(row=3, column=4, padx=10, pady=10)

  bt6 = Button(FrameV, text="Transpuesta M1", command=Transpuesta)
  bt6.grid(row=3, column=5, padx=10, pady=10)

  bt7 = Button(FrameV, text="Gauss-Jordan", command=Gauss)
  bt7.grid(row=4, column=4, padx=10, pady=10)

  bt = Button(FrameV, text="Guardar", command=SaveMT)
  bt.grid(row=5, column=4, padx=10, pady=10)
  #-------------------------------------------------------------------------------------------
  if(ventana15):
          ventana1.withdraw()
  ventana15.mainloop()
#Minimos Cuadrados
def ventana16():
  global ventana16
  global counter
  global r

  counter = 0
  r = 0
  grado_T = []
  arrentries =  []
  arrentries2 = []
  CC_T = []

  def ajustarc(puntosX, puntosY, nPuntos):
    
    listXi=[] #lista de las sumatorias de puntosX con exponente del 1 al 9 | para no usar 9 variables, cada posicion de la lista es una sumatoria
    Yi=0 #es una variable y no una lista porque es un solo numero
    listXiYi=[] #lista de las sumatorias de la multiplicacion de puntosX elevados a la n con Yi

    def sumatoria(listas, expo):
        listasExp = [x**expo for x in listas]
        sumPuntos = sum(listasExp)
        return sumPuntos

    for x in range (0,12):
        listXi.append(sumatoria(puntosX, x+1)) #con esta lista se llena la matriz

    Yi = sumatoria(puntosY, 1) #Yi es la suma de todos los puntos en Y

    #hacer XiYi
    for n in range(0,6): 
        suma=0 #se reinicia suma | suma es sumatoria de Xi*Yi, Xi**2*Yi,...,Xi**n*Yi
        for m in range(0,nPuntos):
            suma+= (puntosX[m]**(n+1))*puntosY[m] #n+1 para que no se eleve a la cero | suma+= 
            #print("Suma en ",n,": ",suma)
        listXiYi.append(suma)
        #print("listXiYi: ",listXiYi[n])
        

    def multiplicacion(lista1,lista2):
        lista_multi = [a*b for a,b in zip(lista1, lista2)]
        return lista_multi

    def gaussJordan(matrizIgual,matriz1):
        m = len(matrizIgual)
        x = np.zeros(m)

        for k in range(0, m):
            for r in range(k+1, m):
                factor=(matriz1[r,k]/matriz1[k,k])
                matrizIgual[r]=matrizIgual[r]-(factor*matrizIgual[k])
                for c in range(0,m):
                    matriz1[r,c]=matriz1[r,c]-(factor*matriz1[k,c])

        x[m-1]=matrizIgual[m-1]/matriz1[m-1, m-1]

        for r in range(m-2, -1, -1):
            suma = 0
            for c in range(0,m):
                suma=suma+matriz1[r,c]*x[c]
            x[r]=(matrizIgual[r]-suma)/matriz1[r, r]  
        return x



    def casoLineal(): #Primer caso, grado 1
        matriz1=np.array([[nPuntos, listXi[0]], 
            [listXi[0], listXi[1]]
            ],dtype=np.float64) #2x2 | dtype es para que la matriz sea float

        matrizIgual=np.array([Yi,listXiYi[0]],dtype=np.float64) #es una lista a modo de vector, una sola fila

        final=gaussJordan(matrizIgual,matriz1)

        #respuesta=round(final[0],3)+"+"+round(final[1],3)+"x"
        #print(respuesta)
        respuestaG = Concat(final, 1)
        CoeCor(respuestaG, 0)

    def casoCuad():
        matriz1=np.array([[nPuntos, listXi[0], listXi[1]], 
            [listXi[0], listXi[1], listXi[2]], 
            [listXi[1], listXi[2], listXi[3]]
            ],dtype=np.float64) #3x3 | dtype es para que la matriz sea float
        
        matrizIgual=np.array([Yi,listXiYi[0], listXiYi[1]],dtype=np.float64) #es una lista a modo de vector, una sola fila

        final=gaussJordan(matrizIgual,matriz1)

        respuestaG = Concat(final, 2)
        CoeCor(respuestaG, 1)

    def casoCub():
        matriz1=np.array([[nPuntos, listXi[0], listXi[1], listXi[2]], 
            [listXi[0], listXi[1], listXi[2], listXi[3]], 
            [listXi[1], listXi[2], listXi[3], listXi[4]],
            [listXi[2], listXi[3], listXi[4], listXi[5]]
            ],dtype=np.float64) #4x4 | dtype es para que la matriz sea float

        matrizIgual=np.array([Yi,listXiYi[0], listXiYi[1], listXiYi[2]],dtype=np.float64) #es una lista a modo de vector, una sola fila

        final=gaussJordan(matrizIgual,matriz1)

        respuestaG = Concat(final, 3)
        CoeCor(respuestaG, 2)

    def caso4():
        matriz1=np.array([[nPuntos, listXi[0], listXi[1], listXi[2], listXi[3]], 
            [listXi[0], listXi[1], listXi[2], listXi[3], listXi[4]], 
            [listXi[1], listXi[2], listXi[3], listXi[4], listXi[5]],
            [listXi[2], listXi[3], listXi[4], listXi[5], listXi[6]],
            [listXi[3], listXi[4], listXi[5], listXi[6], listXi[7]]
            ],dtype=np.float64) #5x5 | dtype es para que la matriz sea float

        matrizIgual=np.array([Yi,listXiYi[0], listXiYi[1], listXiYi[2], listXiYi[3]],dtype=np.float64) #es una lista a modo de vector, una sola fila

        final=gaussJordan(matrizIgual,matriz1)

        respuestaG = Concat(final, 4)
        CoeCor(respuestaG, 3)

    def caso5():
        matriz1=np.array([[nPuntos, listXi[0], listXi[1], listXi[2], listXi[3], listXi[4]], 
            [listXi[0], listXi[1], listXi[2], listXi[3], listXi[4], listXi[5]], 
            [listXi[1], listXi[2], listXi[3], listXi[4], listXi[5], listXi[6]],
            [listXi[2], listXi[3], listXi[4], listXi[5], listXi[6], listXi[7]],
            [listXi[3], listXi[4], listXi[5], listXi[6], listXi[7], listXi[8]],
            [listXi[4], listXi[5], listXi[6], listXi[7], listXi[8], listXi[9]]
            ],dtype=np.float64) #6x6 | dtype es para que la matriz sea float

        matrizIgual=np.array([Yi,listXiYi[0], listXiYi[1], listXiYi[2], listXiYi[3], listXiYi[4]],dtype=np.float64) #es una lista a modo de vector, una sola fila

        final=gaussJordan(matrizIgual,matriz1)

        respuestaG = Concat(final, 5)
        CoeCor(respuestaG, 4)

    def caso6():
        matriz1=np.array([[nPuntos, listXi[0], listXi[1], listXi[2], listXi[3], listXi[4], listXi[5]], 
            [listXi[0], listXi[1], listXi[2], listXi[3], listXi[4], listXi[5], listXi[6]],
            [listXi[1], listXi[2], listXi[3], listXi[4], listXi[5], listXi[6], listXi[7]],
            [listXi[2], listXi[3], listXi[4], listXi[5], listXi[6], listXi[7], listXi[8]],
            [listXi[3], listXi[4], listXi[5], listXi[6], listXi[7], listXi[8], listXi[9]],
            [listXi[4], listXi[5], listXi[6], listXi[7], listXi[8], listXi[9], listXi[10]],
            [listXi[5], listXi[6], listXi[7], listXi[8], listXi[9], listXi[10], listXi[11]]
            ],dtype=np.float64) #7x7 | dtype es para que la matriz sea float

        matrizIgual=np.array([Yi,listXiYi[0], listXiYi[1], listXiYi[2], listXiYi[3], listXiYi[4], listXiYi[5]],dtype=np.float64) #es una lista a modo de vector, una sola fila

        final=gaussJordan(matrizIgual,matriz1)

        respuestaG = Concat(final, 6)
        CoeCor(respuestaG, 5)


    def Concat(final, grado): #print
        global r
        respuesta=''
        for x in range(0,grado+1):
            varFin = round(final[x],3)
            print("varFin: ",varFin)
            if(final[x]>=0 and x!=0): #si es positivo
                print("Entra if >=0")
                respuesta+="+"+str(varFin)+"*x**"+str(x)
            if(x==0): #si es el primer valor
                print("Entra if =0")
                respuesta+=str(varFin)
            if(final[x]<0 and x!=0): #si es negativo
                print("Entra if <0")
                respuesta+=str(varFin)+"*x**"+str(x)
        try:
            grado_T[r].insert(0, str(respuesta))
        except:
            grado_T[r].insert(0, ":(")
        r+=1

        return respuesta
            
    def CoeCor(respuestaG, grado):
        #asi se llamaran las incognitas para que sympy las entienda
        x = symbols ('x') 

        sumCC=0
        sumCC2=0
        promY = sum(puntosY)/nPuntos
        funcRes = parse_expr(respuestaG)

        for i in range(0, nPuntos):
            fxi = funcRes.subs(x, puntosX[i])
            print("AAAAAAAAAAAA", fxi)
            #fxi = fxi(puntosX[i])
            sumCC += (puntosY[i]-fxi)**2

        for j in range(0, nPuntos):
            sumCC2 += (puntosY[j]-promY)**2

        coeficiente = sqrt((sumCC2-sumCC)/sumCC2)
        print("Coeficiente Correlacion: ", round(coeficiente,6))
        CC_T[grado].insert(0, round(coeficiente,6))


    #--------------------EJECUCION---------------------------------------------
    casoLineal()
    casoCuad()
    casoCub()
    caso4()
    caso5()
    caso6()
    #print(sumatoria(puntosX,2))

  #==============================================================================================================================================================================
  #||||||||||||||||||||||||||||||||||||||||||||||O T R O|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
  #==============================================================================================================================================================================
  def manage():
    global counter
    x = int(numeroPuntos_T.get())

    if counter == 0: 
      for i in range(x):
        arrentries.append(Entry(FrameV))
        arrentries2.append(Entry(FrameV))
        arrentries[i].grid(row=3, column=i, padx=2, pady=5)
        arrentries2[i].grid(row=4, column=i, padx=2, pady=5)
    else:
      puntosx = []
      puntosy = []
      for i in range(x):
        puntosx.append(int(arrentries[i].get()))
        puntosy.append(int(arrentries2[i].get()))
      ajustarc(puntosx, puntosy, x)
    counter += 1


  #-------------------------------------------------------------------------------------------
  def clearcomm():
    grado_T[0].delete("0","end")
    grado_T[1].delete("0","end")
    grado_T[2].delete("0","end")
    grado_T[3].delete("0","end")
    grado_T[4].delete("0","end")
    grado_T[5].delete("0","end")

    
  #-------------------------------------------------------------------------------------------
  #creacion de ventana principal.
  ventana16 = Toplevel(ventana1)
  ventana16.title("Ajuste por minimos cuadrados")
  ventana16.config(bg="grey65")
  ventana16.geometry("800x500")
  ventana16.resizable(0,0) #bloqueo de tamaño.
  #-------------------------------------------------------------------------------------------
  #Creacion del frame.
  FrameV=Frame(ventana16)
  FrameV.pack()
  FrameV.config(bg="light grey") #color de fondo.

  FrameV3=Frame(ventana16)
  FrameV3.pack()
  FrameV3.config(bg="grey65") #color de fondo.

  FrameV2=Frame(ventana16)
  FrameV2.pack()
  FrameV2.config(bg="grey65") #color de fondo.

  #-------------------------------------------------------------------------------------------
  #Labels (etiquetas, todo lo que tenga "_L").
  numeroPuntos_L=Label(FrameV, text="Numero de puntos")
  numeroPuntos_L.grid(row=2, column=0, padx=10, pady=10)
  numeroPuntos_L.config(bg="light grey") #color de fondo.

  #Etiquetas grados
  ejemplo_L=Label(FrameV3, text="Ajustes por grados f(x) = a₀+a₁x+a₂x²+a₃x³+...+aₙxⁿ0")
  ejemplo_L.grid(row=12, column=0, padx=10, pady=10)
  ejemplo_L.config(bg="grey65") #color de fondo.

  grado1_L=Label(FrameV2, text="Grado 1:")
  grado1_L.grid(row=3, column=0, padx=10, pady=10)
  grado1_L.config(bg="grey65") #color de fondo.

  grado2_L=Label(FrameV2, text="Grado 2:")
  grado2_L.grid(row=4, column=0, padx=10, pady=10)
  grado2_L.config(bg="grey65") #color de fondo.

  grado3_L=Label(FrameV2, text="Grado 3:")
  grado3_L.grid(row=5, column=0, padx=10, pady=10)
  grado3_L.config(bg="grey65") #color de fondo.

  grado4_L=Label(FrameV2, text="Grado 4:")
  grado4_L.grid(row=6, column=0, padx=10, pady=10)
  grado4_L.config(bg="grey65") #color de fondo.

  grado5_L=Label(FrameV2, text="Grado 5:")
  grado5_L.grid(row=7, column=0, padx=10, pady=10)
  grado5_L.config(bg="grey65") #color de fondo.

  grado6_L=Label(FrameV2, text="Grado 6:")
  grado6_L.grid(row=8, column=0, padx=10, pady=10)
  grado6_L.config(bg="grey65") #color de fondo.

  #Etiquetas Coeficientes Correlacion
  cc1_L=Label(FrameV2, text="C.C :")
  cc1_L.grid(row=3, column=2, padx=10, pady=10)
  cc1_L.config(bg="grey65") #color de fondo.

  cc2_L=Label(FrameV2, text="C.C :")
  cc2_L.grid(row=4, column=2, padx=10, pady=10)
  cc2_L.config(bg="grey65") #color de fondo.

  cc3_L=Label(FrameV2, text="C.C :")
  cc3_L.grid(row=5, column=2, padx=10, pady=10)
  cc3_L.config(bg="grey65") #color de fondo.

  cc4_L=Label(FrameV2, text="C.C :")
  cc4_L.grid(row=6, column=2, padx=10, pady=10)
  cc4_L.config(bg="grey65") #color de fondo.

  cc5_L=Label(FrameV2, text="C.C :")
  cc5_L.grid(row=7, column=2, padx=10, pady=10)
  cc5_L.config(bg="grey65") #color de fondo.

  cc6_L=Label(FrameV2, text="C.C :")
  cc6_L.grid(row=8, column=2, padx=10, pady=10)
  cc6_L.config(bg="grey65") #color de fondo.

  #-------------------------------------------------------------------------------------------
  #Cajas de texto. ----------
  numeroPuntos_T=Entry(FrameV)
  numeroPuntos_T.grid(row=2, column=1, padx=10, pady=10)
  numeroPuntos_T.config(justify="center")
  #Outputs grados
  grado_T.append(Entry(FrameV2, width=70))
  grado_T[0].grid(row=3, column=1, padx=10, pady=10)
  grado_T[0].config(justify="center")

  grado_T.append(Entry(FrameV2, width=70))
  grado_T[1].grid(row=4, column=1, padx=10, pady=10)
  grado_T[1].config(justify="center")

  grado_T.append(Entry(FrameV2, width=70))
  grado_T[2].grid(row=5, column=1, padx=10, pady=10)
  grado_T[2].config(justify="center")

  grado_T.append(Entry(FrameV2, width=70))
  grado_T[3].grid(row=6, column=1, padx=10, pady=10)
  grado_T[3].config(justify="center")

  grado_T.append(Entry(FrameV2, width=70))
  grado_T[4].grid(row=7, column=1, padx=10, pady=10)
  grado_T[4].config(justify="center")

  grado_T.append(Entry(FrameV2, width=70))
  grado_T[5].grid(row=8, column=1, padx=10, pady=10)
  grado_T[5].config(justify="center")

  #Outputs Coeficiente Correlacion | tienen que estar alineados con sus grados
  CC_T.append(Entry(FrameV2, width=15))
  CC_T[0].grid(row=3, column=3, padx=10, pady=10)

  CC_T.append(Entry(FrameV2, width=15))
  CC_T[1].grid(row=4, column=3, padx=10, pady=10)

  CC_T.append(Entry(FrameV2, width=15))
  CC_T[2].grid(row=5, column=3, padx=10, pady=10)

  CC_T.append(Entry(FrameV2, width=15))
  CC_T[3].grid(row=6, column=3, padx=10, pady=10)

  CC_T.append(Entry(FrameV2, width=15))
  CC_T[4].grid(row=7, column=3, padx=10, pady=10)

  CC_T.append(Entry(FrameV2, width=15))
  CC_T[5].grid(row=8, column=3, padx=10, pady=10)

  #-------------------------------------------------------------------------------------------
  #Botones.
  BorrarB=Button(FrameV, text="Borrar", command=clearcomm)
  BorrarB.grid(row=11, column=0, pady=10)

  CalcularB=Button(FrameV, text="Calcular", command=manage)
  CalcularB.grid(row=11, column=1, pady=10, padx=10)

  SalirB=Button(FrameV, text="Volver", command=volver_ventana15)
  SalirB.grid(row=11, column=2, pady=10, padx=10)
  #-------------------------------------------------------------------------------------------
  if(ventana16):
          ventana1.withdraw()
  ventana16.mainloop() #es el ciclo para que la ventana "exista"

#-------------------------------CATEGORIAS----------------------------------------------------------------
def conversiones():
  global conversiones

  conversiones = Toplevel(ventana1)
  conversiones.title("Menu de conversiones")
  conversiones.geometry('300x220')
  conversiones.resizable(0,0) #bloqueo de tamaño.
  conversiones.config(bg= "light grey")
  #conversiones.iconbitmap('Icono\calculadora.ico') #icono.
  #-------------------------------------------------------------------------------------------
  #Creacion del frame.
  FrameV=Frame(conversiones)
  FrameV.pack()
  FrameV.config(bg="light grey") #color de fondo.
  #-------------------------------------------------------------------------------------------
  #Labels (etiquetas).
  binarioL=Label(FrameV, text="Menu de calculadoras")
  binarioL.grid(row=0, column=1, padx=10, pady=10)
  binarioL.config(bg="light grey") #color de fondo.

  #-------------------------------------------------------------------------------------------
  #Botones.
  Calculadora1=Button(FrameV, text="Conversiones decimales", command=ventana3)
  Calculadora1.grid(row=1, column=1, padx=10, pady=10)

  Calculadora2=Button(FrameV, text="Conversiones IEEE", command=ventana6)
  Calculadora2.grid(row=2, column=1, padx=10, pady=10)

  SalirB=Button(FrameV, text="Volver", command=volver_ventana16)
  SalirB.grid(row=3, column=1, pady=10, padx=10)
  #-------------------------------------------------------------------------------------------
  if(conversiones):
    ventana1.withdraw()
  conversiones.mainloop()

def raices():
  global raices

  raices = Toplevel(ventana1)
  raices.title("Menu de raices")
  raices.geometry('300x320')
  raices.resizable(0,0) #bloqueo de tamaño.
  raices.config(bg= "light grey")
  #raices.iconbitmap('Icono\calculadora.ico') #icono.
  #-------------------------------------------------------------------------------------------
  #Creacion del frame.
  FrameV=Frame(raices)
  FrameV.pack()
  FrameV.config(bg="light grey") #color de fondo.
  #-------------------------------------------------------------------------------------------
  #Labels (etiquetas).
  binarioL=Label(FrameV, text="Menu de calculadoras")
  binarioL.grid(row=0, column=1, padx=10, pady=10)
  binarioL.config(bg="light grey") #color de fondo.

  #-------------------------------------------------------------------------------------------
  #Botones.
  Calculadora1=Button(FrameV, text="Biseccion", command=ventana2)
  Calculadora1.grid(row=1, column=1, padx=10, pady=10)

  Calculadora2=Button(FrameV, text="Newton", command=ventana7)
  Calculadora2.grid(row=2, column=1, padx=10, pady=10)

  Calculadora2=Button(FrameV, text="Falsa posicion", command=ventana5)
  Calculadora2.grid(row=3, column=1, padx=10, pady=10)

  Calculadora2=Button(FrameV, text="Secantes", command=ventana9)
  Calculadora2.grid(row=4, column=1, padx=10, pady=10)

  Calculadora2=Button(FrameV, text="Polinomios", command=ventana8)
  Calculadora2.grid(row=5, column=1, padx=10, pady=10)

  SalirB=Button(FrameV, text="Volver", command=volver_ventana17)
  SalirB.grid(row=6, column=1, pady=10, padx=10)
  #-------------------------------------------------------------------------------------------
  if(raices):
    ventana1.withdraw()
  raices.mainloop()

def integracion():
  global integracion

  integracion = Toplevel(ventana1)
  integracion.title("Menu de raices")
  integracion.geometry('300x320')
  integracion.resizable(0,0) #bloqueo de tamaño.
  integracion.config(bg= "light grey")
  #-------------------------------------------------------------------------------------------
  #Creacion del frame.
  FrameV=Frame(integracion)
  FrameV.pack()
  FrameV.config(bg="light grey") #color de fondo.
  #-------------------------------------------------------------------------------------------
  #Labels (etiquetas).
  binarioL=Label(FrameV, text="Menu de calculadoras")
  binarioL.grid(row=0, column=1, padx=10, pady=10)
  binarioL.config(bg="light grey") #color de fondo.

  #-------------------------------------------------------------------------------------------
  #Botones.
  Calculadora1=Button(FrameV, text="Rectangulos", command=ventana14)
  Calculadora1.grid(row=1, column=1, padx=10, pady=10)

  Calculadora2=Button(FrameV, text="Simpson 1/3", command=ventana11)
  Calculadora2.grid(row=2, column=1, padx=10, pady=10)

  Calculadora2=Button(FrameV, text="Simpson 3/8", command=ventana12)
  Calculadora2.grid(row=3, column=1, padx=10, pady=10)

  Calculadora2=Button(FrameV, text="Montecarlo", command=ventana10)
  Calculadora2.grid(row=4, column=1, padx=10, pady=10)

  Calculadora2=Button(FrameV, text="Trapecios", command=ventana13)
  Calculadora2.grid(row=5, column=1, padx=10, pady=10)

  SalirB=Button(FrameV, text="Volver", command=volver_ventana18)
  SalirB.grid(row=6, column=1, pady=10, padx=10)
  #-------------------------------------------------------------------------------------------
  if(integracion):
    ventana1.withdraw()
  integracion.mainloop()

def creditos():
  MessageBox.showinfo("Creditos","Este programa fue desarrollado por Oscar Lopez, Breyner Grajales, Valentina Cuellar, Juanita Noya, Andres Correa")
  
#-----------------------------------------------------------------------------------------------------------
def volver_ventana1():
    raices.iconify()
    raices.deiconify()
    ventana2.destroy()

def volver_ventana2():
    conversiones.iconify()
    conversiones.deiconify()
    ventana3.destroy()

def volver_ventana3():
    ventana1.iconify()
    ventana1.deiconify()
    ventana4.destroy()

def volver_ventana4():
    raices.iconify()
    raices.deiconify()
    ventana5.destroy()

def volver_ventana5():
    conversiones.iconify()
    conversiones.deiconify()
    ventana6.destroy()

def volver_ventana6():
    raices.iconify()
    raices.deiconify()
    ventana7.destroy()

def volver_ventana7():
    raices.iconify()
    raices.deiconify()
    ventana8.destroy()

def volver_ventana8():
    raices.iconify()
    raices.deiconify()
    ventana9.destroy()

def volver_ventana9():
    integracion.iconify()
    integracion.deiconify()
    ventana10.destroy()

def volver_ventana10():
    integracion.iconify()
    integracion.deiconify()
    ventana11.destroy()

def volver_ventana11():
    integracion.iconify()
    integracion.deiconify()
    ventana12.destroy()

def volver_ventana12():
    integracion.iconify()
    integracion.deiconify()
    ventana13.destroy()

def volver_ventana13():
  integracion.iconify()
  integracion.deiconify()
  ventana14.destroy()

def volver_ventana14():
    ventana1.iconify()
    ventana1.deiconify()
    ventana15.destroy()

def volver_ventana15():
    ventana1.iconify()
    ventana1.deiconify()
    ventana16.destroy()

def volver_ventana16():
    ventana1.iconify()
    ventana1.deiconify()
    conversiones.destroy()

def volver_ventana17():
    ventana1.iconify()
    ventana1.deiconify()
    raices.destroy()

def volver_ventana18():
    ventana1.iconify()
    ventana1.deiconify()
    integracion.destroy()

ventana1()

