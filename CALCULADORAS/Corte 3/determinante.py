import numpy as np

print('Ingrese el orden de la matriz a calcular')
filasA, columnasA = int(input()), int(input())

#Creando la matriz
matriizA = []
for i in range(filasA):
    matrizA.append([0]* columnasA)


    #Rellenando la matriz
print('Ingrese la matriz A')
for fila in range(filasA):
    for columna in range(columnasA):
        matrizA[fila][columna] = float(
            input(f'Ingrese la posicion numero {fila}, {columna}: ')
        )

#Determinante de la matriz

determinante = np.linalg.det(matriizA)
print(determinante)