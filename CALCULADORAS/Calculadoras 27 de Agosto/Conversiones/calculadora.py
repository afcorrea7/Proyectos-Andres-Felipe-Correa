#Andres Felipe Correa - Breyner Samuel Grajales - Juanita Noya - Oscar Lopez - Valentina Cuellar
from cgitb import text
from distutils.cmd import Command
from distutils.command.config import config
from numbers import Real
from tkinter import * #libreria de GUI.
import math
from turtle import clear
from typing import BinaryIO #Libreria para usar modf y separar fraccionarios de enteros

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


"""
    while i==1:
    
    print ("¿Que tipo de numero desear convertir?")
    numOpcion= int (input ("1.Decimal\n2.Octal\n3.Binario\n4.Hexadecimal\n"))
    valor= input("Ingrese el número que desea convertir: ")


    match numOpcion:
        case 1: 
          print("\n---------------------------------------------------\n")
          print("Número decimal escogido: "+valor+"\n")
          num = float(valor)

          print ('En binario es: ',Deci_Binario(num),"\nEn octal es: ",Deci_Octal(num),"\nEn hexadecimal es: ",Deci_Hexa(num),)
    
        case 2: 
          print("\n---------------------------------------------------\n")
          print("Número octal escogido: "+valor+"\n")
          num = float(valor)
          print ("En binario es:",Deci_Binario(float(B_Dec(num,8))),"\nEn decimal es: ",B_Dec(num,8),"\nEn hexadecimal es: ",Deci_Hexa(float(B_Dec(num,8))))

        case 3: 
          print("\n---------------------------------------------------\n")
          print("Número binario escogido: "+valor+"\n")
          num = float(valor)
          print ("En decimal es:",B_Dec(num,2), "\nEn octal es: ",Deci_Octal(float(B_Dec(num,2))),"\nEn hexadecimal es: ",Deci_Hexa(float(B_Dec(num,2))))

        case 4: 
          print("\n---------------------------------------------------\n")
          print("Número hexadecimal escogido: "+valor+"\n")
          #Hex_Partes(valor)
          print("En decimal es:",Hex_Partes(valor), "\nEn octal es: ",Deci_Octal(Hex_Partes(valor)),"\nEn binario es: ",Deci_Binario(Hex_Partes(valor)))          

    opcion=int(input("\n1.Convertir otro número 2.Salir\n"))
    i=opcion

    """

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
Ventana = Tk()
Ventana.title("Calculadora Conversora")
#Ventana.geometry("550x550") #tamaño.
Ventana.resizable(0,0) #bloqueo de tamaño.
#Ventana.iconbitmap('calculadora.ico') #icono.

Deci_Bin=StringVar()
#-------------------------------------------------------------------------------------------
#Creacion del frame.
FrameV=Frame()
FrameV.pack()
FrameV.config(bg="light grey") #color de fondo.
#-------------------------------------------------------------------------------------------
#Labels (etiquetas).
binarioL=Label(FrameV, text="Binario:")
binarioL.grid(row=0, column=0, sticky="w", padx=10, pady=10)
binarioL.config(bg="light grey") #color de fondo.

decimalL=Label(FrameV, text="Decimal:")
decimalL.grid(row=1, column=0, sticky="w", padx=10, pady=10)
decimalL.config(bg="light grey") #color de fondo.

OctadecimalL=Label(FrameV,text="Octadecimal:")
OctadecimalL.grid(row=2, column=0, sticky="w", padx=10, pady=10)
OctadecimalL.config(bg="light grey") #color de fondo.

HexadecimalL=Label(FrameV, text="Hexadecimal:")
HexadecimalL.grid(row=3, column=0, sticky="w", padx=10, pady=10)
HexadecimalL.config(bg="light grey") #color de fondo.

ResultadosL=Label(FrameV)
ResultadosL.grid(row=4, column=1, sticky="w", padx=10, pady=10)
ResultadosL.config(bg="white") #color de fondo.
#-------------------------------------------------------------------------------------------
#Cajas de texto.
binarioT=Entry(FrameV)
binarioT.grid(row=0, column=1, padx=10, pady=10)
binarioT.config(justify="center")

decimalT=Entry(FrameV)
decimalT.grid(row=1, column=1, padx=10, pady=10)
decimalT.config(justify="center")

OctadecimalT=Entry(FrameV)
OctadecimalT.grid(row=2, column=1, padx=10, pady=10)
OctadecimalT.config(justify="center")

HexadecimalT=Entry(FrameV)
HexadecimalT.grid(row=3, column=1, padx=10, pady=10)
HexadecimalT.config(justify="center")
#-------------------------------------------------------------------------------------------
#Botones.
CalcularB=Button(FrameV, text="Calcular", command=evaluar)
CalcularB.grid(row=5, column=1, pady=10)


BorrarB=Button(FrameV, text="Borrar", command=clearcomm)
BorrarB.grid(row=5, column=0, pady=10)

SalirB=Button(FrameV, text="Salir", command=Ventana.destroy)
SalirB.grid(row=5, column=2, pady=10, padx=10)
#-------------------------------------------------------------------------------------------
Ventana.mainloop() #es el ciclo para que la ventana "exista".