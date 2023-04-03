
from scipy import linalg



#Suma 
a= [[1, 8, 7],
    [3, 5, 6],
    [4, 7, 1]]

b= [[6,  3, 7],
    [23, 43, 12],
    [55,  43, 7]]

def sumar (m1, m2):

    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):

        m3 = []
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m1[0])):
                m3[i].append(m1[i][j] + m2[i] [j])
        return m3
    else:
        return None

c= sumar(a,b)

if c == None:
    print("No se puede sumar")
else:
    for fila in c:
        print("[", end=" ")
        for elemento in fila:
            print(elemento, end=" ")
        print("]")


#Inversa
print("Inversa de A:")
print(linalg.inv(a))
