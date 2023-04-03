from sympy import *
import numpy as np
import scipy as sp

x = symbols('x')
bucle=1

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

while bucle==1:
    print("| --------------INTEGRACION NUMERICA A LA IZQUIERDA -------------- |")

    #asignacion de valores a variables
    ecuacion = input("Ingrese una funcion en terminos de x: ")
    aVal = float(input("Ingrese un valor para a: ")) 
    bVal = float(input("Ingrese otro valor para b: "))
    partinum = int(input("Ingrese el número de particiones: ")) #El usuario debe darlo

    Izquierdos(ecuacion,aVal,bVal,partinum)

    bucle = int(input("Deseas repetir el metodo?\n 1.Si\n 0.No\n"))