#from ast import Num
from matplotlib import pyplot
from sympy import *
import re
from tkinter import * #libreria de GUI
import scipy as sp  # Importamos scipy como el alias sp

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
    print(e, "\n ", Metodo.separador(e))
    arra.append( Metodo.separador(e))
  print(Metodo.separador(e))
  ResultadoT.insert(0, Metodo.separador(e))

class polinomios:
  
	def separador(slef, num):
		# resive el el parametro como un string de numeros
		txt = num
		# se hace un split para pasar la cadena separada por comas a in arrelgo de con elementos tipo int
		cadena = [float(i) for i in txt.split(',')]
		print("el arreglo del polinomio es:")
		print(cadena)
		# al arreglo se le aplica la funcion roots para hayar las raices
		raices = sp.roots(cadena)
		print("las raices son:")
		for i in raices:
			print(i)
		print("raices como arreglo:")
		# se retornan las raices en forma de arreglo
		return raices

    


#num = input('Los terminos de los polinomios deben de estar separados por comas.\nejem: si es x^2+5x-8 se escribe 1,5,-8 \nescribir terminos del polinomios:\n')
Metodo = polinomios()
#print(Metodo.separador(num))

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

    
    #asdsadasdasdasdasdsad

  return coeficientes

  coefici = coefs(nums)
  """for g, v in c.items():
    coeficientes[g] = v

    print("los coe son: ",coeficientes[g])

    raices = sp.roots(coeficientes)
    print("las raices son:")
    for i in raices:
            print(i)
    print("raices como arreglo:")

  return raices"""



#-------------------------------------------------------------------------------------------
#Zona para definir comandos.
def clearcomm():
    Tcuadratico.delete("0", "end")
    ResultadoT.delete("0","end")
#-------------------------------------------------------------------------------------------
#creacion de ventana principal.
Ventana = Tk()
Ventana.title("Calculadora Polinomios")
Ventana.resizable(0,0) #bloqueo de tamaño.
#Ventana.iconbitmap('Interfaz\calculadora.ico') #icono.
#-------------------------------------------------------------------------------------------
#Creacion del frame.
FrameV=Frame()
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

SalirB=Button(FrameV, text="Salir", command=Ventana.destroy)
SalirB.grid(row=4, column=2, pady=10, padx=10)
#-------------------------------------------------------------------------------------------
Ventana.mainloop() #es el ciclo para que la ventana "exista"