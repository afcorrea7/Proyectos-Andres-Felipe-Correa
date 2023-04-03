from numpy.random import uniform as unif
from sympy import *

def montecarlo(fx, a, b, num):
    suma=0
    resultado=0
    funcionDev=parse_expr(fx) #pasa de string a una ecuación 
    x=symbols('x')

    for i in range (0,num,1):
        varX=unif(a,b) 
        suma+=funcionDev.subs(x,varX)
        
        #print(funcion)

    resultado=((b-a)*suma)/num
    print("Integral",resultado)


bucle=1
while bucle==1:
    print("| --------------INTEGRACION NUMERICA MONTECARLO-------------- |")

    #asignacion de valores a variables
    ecuacion = input("Ingrese una funcion en terminos de x: ")
    aVal = float(input("Ingrese un valor para a: ")) 
    bVal = float(input("Ingrese otro valor para b: "))
    num = int(input("Ingrese la cantidad de números aleatorios: ")) #El usuario debe darlo

    montecarlo(ecuacion,aVal,bVal,num)

    bucle = int(input("Deseas repetir el metodo?\n 1.Si\n 0.No\n"))