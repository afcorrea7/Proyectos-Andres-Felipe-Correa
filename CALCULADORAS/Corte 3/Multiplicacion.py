from difflib import restore
from sympy import *
import numpy as np

filas = 0
colum = 0
matriz1 = []
matriz2 = []
matrizFin=[]

bucle=1

def MultiplicacionMatriz():
    #Matriz 1
    print("Matriz 1: \n")
    filas = int(input("Ingrese numero de filas: "))
    columnas = int(input("Ingrese numero de columnas: "))

    for i in range(filas): #se crea una matriz vacia
        matriz1.append([0]*columnas)
    for l in range (filas): #a medida que se crea la matriz se pide los valores que van a meterse
        for j in range (columnas):
            matriz1[l][j]=float(input("Fila {}, Columna {}: ".format(l+1, j+1)))

    #print la matriz recien creada
    for f in matriz1:
        print("[", end=" ")
        for elem in f:
            print("{}".format(elem), end=" ")
        print("]")

    #------------------------------------------------------------------------------------------------------------

    #Matriz 2
    print("Matriz 2: \n")     

    filas = int(input("Ingrese numero de filas: "))
    columnas = int(input("Ingrese numero de columnas: "))

    for m in range(filas): #se crea una matriz vacia
        matriz2.append([0]*columnas)
    for n in range (filas): #a medida que se crea la matriz se pide los valores que van a meterse
        for o in range (columnas):
            matriz2[n][o]=float(input("Fila {}, Columna {}: ".format(n+1, o+1)))

    #print la matriz recien creada
    for f in matriz2:
        print("[", end=" ")
        for elem in f:
            print("{}".format(elem), end=" ")
        print("]")

    #MULTIPLICACION-----------------------------------------------------------------------------------------------
    if(len(matriz1[0])==len(matriz2)): #Solo multiplicar cuando el num de columnas de matriz1 sea el mismo que el num de filas de matriz2
        #creamos matriz vacia
        for i in range(len(matriz1)): #que tenga el numero de filas de matriz1
            matrizFin.append([])
            for l in range(len(matriz2[0])): #y el numero de columnas de matriz2
                matrizFin[i].append(0)

        #Recorre los indices de las matrices 1 y 2 para llenar matrizFin
        for n in range(len(matriz1)):
            for m in range(len(matriz2[0])): 
                for o in range(len(matriz1[0])):
                    matrizFin[n][m] += matriz1[n][o]*matriz2[o][m]

        return matrizFin
    else:
        print("las columnas de la matriz 1 no encajan con las filas de la matriz 2.")
        return None



while bucle==1:
    print("| -------------- MULTIPLICACION DE MATRICES -------------- |")

    resultado = MultiplicacionMatriz()
    print("Resultado de la multiplicación: ")
    for f in resultado:
        print("[", end=" ")
        for elem in f:
            print("{}".format(elem), end=" ")
        print("]")


    bucle = int(input("Deseas repetir el metodo?\n 1.Si\n 0.No\n"))
