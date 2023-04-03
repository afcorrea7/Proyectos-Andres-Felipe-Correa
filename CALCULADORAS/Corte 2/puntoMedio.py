from sympy import *

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
    
bucle=1
while bucle==1:
    print("| --------------INTEGRACION NUMERICA PUNTO MEDIO-------------- |")

    #asignacion de valores a variables
    ecuacion = input("Ingrese una funcion en terminos de x: ")
    aVal = float(input("Ingrese un valor para a: ")) 
    bVal = float(input("Ingrese otro valor para b: "))
    partinum = int(input("Ingrese el número de particiones: ")) #El usuario debe darlo

    puntoMedio(ecuacion,aVal,bVal,partinum)

    bucle = int(input("Deseas repetir el metodo?\n 1.Si\n 0.No\n"))











