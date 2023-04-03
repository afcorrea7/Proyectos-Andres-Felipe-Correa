
def MultiplicacionEscalar ():
    filas=int(input("Introduce numero de filas: "))
    columnas=int(input("Introduce numero de columnas: "))
    matriz=[]
    for i in range (filas):
        matriz.append([0]*columnas)

    for i in range (filas):
        for j in range (columnas):
            matriz[i][j]=float(input("Fila {}, Columna {}: ".format(i+1, j+1)))
    num=float(input("Ingrese el número que desea multiplicar con la matriz: "))
    for i in range (filas):
        for j in range (columnas):
            matriz[i][j]=matriz[i][j]*num

    print("\nResultado:\n")
    for fila in matriz :
        print("[", end=" ")
        for elemento in fila:
            print("{}".format(elemento), end=" ")
        print("]")


def RestaMatriz():
    print("Primera matriz")
    filas=int(input("Introduce numero de filas: "))
    columnas=int(input("Introduce numero de columnas: "))
    matriz1=[]
    for i in range (filas):
        matriz1.append([0]*columnas)

    for i in range (filas):
        for j in range (columnas):
            matriz1[i][j]=float(input("Fila {}, Columna {}: ".format(i+1, j+1)))


    print("Segunda matriz")
    filas=int(input("Introduce numero de filas: "))
    columnas=int(input("Introduce numero de columnas: "))
    matriz2=[]
    for z in range (filas):
        matriz2.append([0]*columnas)

    for x in range (filas):
        for y in range (columnas):
            matriz2[x][y]=float(input("Fila {}, Columna {}: ".format(x+1, y+1)))
    
    if (len(matriz1)==len(matriz2) and len(matriz1[0])==len(matriz2[0])):
        matrizResul=[]

        for t in range (len(matriz1)):
            matrizResul.append([])
            for m in range (len(matriz1[0])):
                matrizResul[t].append(matriz1[t][m]-matriz2[t][m])
        
        print("\nResultado:\n")
        for fila in matrizResul :
            print("[", end=" ")
            for elemento in fila:
                print("{}".format(elemento), end=" ")
            print("]")
    else:
        print("No se puede operar")
    

def Transpuesta():
    filas=int(input("Introduce numero de filas: "))
    columnas=int(input("Introduce numero de columnas: "))
    matriz=[]
    for i in range (filas):
        matriz.append([0]*columnas)

    for i in range (filas):
        for j in range (columnas):
            matriz[i][j]=float(input("Fila {}, Columna {}: ".format(i+1, j+1)))

    transp=[]

    for x in range (len(matriz[0])):
        transp.append([])
        for y in range (len(matriz)):
            transp[x].append(matriz[y][x])

    print("\nMatriz original:\n")
    for fila in matriz :
        print("[", end=" ")
        for elemento in fila:
            print("{}".format(elemento), end=" ")
        print("]")

    print("\nResultado:\n")
    for fila in transp :
        print("[", end=" ")
        for elemento in fila:
            print("{}".format(elemento), end=" ")
        print("]")


#MultiplicacionEscalar()  
#RestaMatriz()  
Transpuesta()