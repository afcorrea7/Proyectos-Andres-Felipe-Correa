from sympy import *

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



while bucle==1:
    print("| --------------INTEGRACION POR TRAPECIOS -------------- |")

    #asignacion de valores a variables
    ecuacion = input("Ingrese una funcion en terminos de x: ")
    aVal = float(input("Ingrese un valor para a: ")) 
    bVal = float(input("Ingrese otro valor para b: "))
    partinum = int(input("Ingrese el número de particiones: ")) #El usuario debe darlo
    
    Trapecios(ecuacion,aVal,bVal,partinum)

    bucle = int(input("Deseas repetir el metodo?\n 1.Si\n 0.No\n"))