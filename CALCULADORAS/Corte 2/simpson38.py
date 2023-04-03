from sympy import *
import numpy as np
import random
from random import uniform

""""
num=300
print(num%3==0) como saber si un numero es multiplo de 3
"""
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
    print("Integral:", area) 



def CalcuError(ecua, aVal, bVal): #Calcula el error
    expr = parse_expr(ecua)
    deriv = diff(expr, x, 4) #funcion, qué variable, hasta qué derivada

    h = (bVal-aVal)/3

    aleatorio = random.uniform(aVal,bVal)
    derivAleatorio = deriv.subs(x, aleatorio) #evalua f(x) donde f(x) es la cuarta derivada y x es random

    errorSimp = (-3*(h**5)/80)*derivAleatorio

    return errorSimp



while bucle==1:
    print("| -------------- INTEGRACION NUMERICA POR SIMPSON 3/8 -------------- |")

    #asignacion de valores a variables
    ecuacion = input("Ingrese una funcion en terminos de x: ")
    aVal = float(input("Ingrese un valor para a: ")) 
    bVal = float(input("Ingrese otro valor para b: "))
    partinum = int(input("Ingrese el número de particiones: ")) #El usuario debe darlo

    nuevopartinum = Multiplo3(partinum) #Asegura que el numero de particiones ingresadas sea multiplo de 3

    Simpson38(ecuacion,aVal,bVal,nuevopartinum)

    print("El error de este metodo esta vez es de: ",CalcuError(ecuacion,aVal,bVal))

    bucle = int(input("Deseas repetir el metodo?\n 1.Si\n 0.No\n"))