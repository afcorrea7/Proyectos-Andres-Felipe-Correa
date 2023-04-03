from sympy import *

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

bucle=1
while bucle==1:
    print("| --------------INTEGRACION NUMERICA A LA IZQUIERDA -------------- |")

    #asignacion de valores a variables
    ecuacion = input("Ingrese una funcion en terminos de x: ")
    aVal = float(input("Ingrese un valor para a: ")) 
    bVal = float(input("Ingrese otro valor para b: "))
    partinum = int(input("Ingrese el número de particiones: ")) #El usuario debe darlo

    derecha(ecuacion,aVal,bVal,partinum)

    bucle = int(input("Deseas repetir el metodo?\n 1.Si\n 0.No\n"))
