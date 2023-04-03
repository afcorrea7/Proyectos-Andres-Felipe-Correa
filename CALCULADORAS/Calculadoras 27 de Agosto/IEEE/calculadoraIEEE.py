#Andres Felipe Correa - Breyner Samuel Grajales - Juanita Noya - Oscar Lopez - Valentina Cuellar / metodos numericos 
from ast import Num
import math
from re import I
from sys import int_info
from tokenize import Double
from decimal import Decimal
from decimal import *
from tkinter import * #libreria de GUI.

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
  

#Menu
"""while bucle==1:
  
  print("\nEscoge la conversión que deseas realizar")
  numOpcion= int(input ("1) Decimal a IEEE 754 | 2) IEEE 754 a Decimal: "))

  print ("\n-------------------------------------------------\n")
  match numOpcion:
    case 1: 
      valor= float(input("Ingrese el numero a convertir: "))
      print ("Número decimal escogido: ",valor)
      Deci_IEEE(valor)
    case 2: 
      print("¿Qué precisión deseas convertir?")
      numOpcion1= int(input ("1) 32 bits | 2) 64 bits: "))
      print ("\n-------------------------------------------------\n")
      match numOpcion1:
        case 1:
          sigIEEE= int(input("Ingrese el signo (1 bit): "))
          expIEEE= str(input("Ingrese el exponente (8 bits): "))
          manIEEE= str(input("Ingrese la mantisa (23 bits): "))
          IEEE_Deci(sigIEEE,expIEEE,manIEEE,126,127)
          
        case 2: 
          sigIEEE= int(input("Ingrese el signo (1 bit): "))
          expIEEE= str(input("Ingrese el exponente (11 bits): "))
          manIEEE= str(input("Ingrese la mantisa (52 bits): "))
          IEEE_Deci(sigIEEE,expIEEE,manIEEE,1022,1023)

  bucle = int(input("¿Desea hacer otra conversión?\n 1. Si 0. No\n"))
"""

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
Ventana = Tk()
Ventana.title("Calculadora IEEE")
Ventana.resizable(0,0) #bloqueo de tamaño.
Ventana.iconbitmap('Interfaz\calculadora.ico') #icono.
#-------------------------------------------------------------------------------------------
#Creacion del frame.
FrameV=Frame()
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

SalirB=Button(FrameV, text="Salir", command=Ventana.destroy)
SalirB.grid(row=9, column=2, pady=10, padx=10)
#-------------------------------------------------------------------------------------------
Ventana.mainloop() #es el ciclo para que la ventana "exista"