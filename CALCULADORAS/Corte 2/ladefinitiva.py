
from sympy import *
import random
from random import uniform

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
    
def CalcuError(ecua, aVal, bVal): #Calcula el error
    x= symbols ('x')
    expr = parse_expr(ecua)
    deriv = diff(expr, x, 4) #funcion, qué variable, hasta qué derivada

    h = (bVal-aVal)/3

    aleatorio = random.uniform(aVal,bVal)
    derivAleatorio = deriv.subs(x, aleatorio) #evalua f(x) donde f(x) es la cuarta derivada y x es random

    errorSimp = ((h**5)/90)*derivAleatorio

    return errorSimp

bucle=1
while bucle==1:
    print("| -------------- INTEGRACION NUMERICA POR SIMPSON 3/8 -------------- |")

    #asignacion de valores a variables
    ecuacion = input("Ingrese una funcion en terminos de x: ")
    aVal = float(input("Ingrese un valor para a: ")) 
    bVal = float(input("Ingrese otro valor para b: "))
    partinum = int(input("Ingrese el número de particiones: ")) #El usuario debe darlo

    nuevopartinum = Multiplo2(partinum) #Asegura que el numero de particiones ingresadas sea multiplo de 3

    simp(ecuacion,aVal,bVal,nuevopartinum)

    print("El error de este metodo esta vez es de: ",CalcuError(ecuacion,aVal,bVal))

    bucle = int(input("Deseas repetir el metodo?\n 1.Si\n 0.No\n"))