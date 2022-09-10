import numpy as np
import math
def sumavectocomp(m,n):
    preal = m[0] + n[0]
    pimag = m[1] + n[1]
    return (preal, pimag)

#print(sumavectocomp([2,0],[3,1]))

def inversovectocomp(m):
    preal = (m[0] * -1)
    pimag = (m[1] * -1)
    return (preal, pimag)

#print(inversovectocomp([2,-8]))

def multescavectocomp(m,n):
    preal = (n[0] * m)
    pimag = (n[1] * m)
    return preal, pimag

#print(multescavectocomp(2,[-3,4]))

def adimatrices(m,n):
    if len(m) != len(n):
        return False
    if len(m[0]) != len(n[0]):
        return False
    x = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = (m[i][j] + n[i][j])
    return m

#print(adimatrices([[1,2,3],[4,5,6]],[[2,3,5],[11,7,5]]))

def inversamatrizcomp(m):
    matriz = np.array(m)
    filas, columnas = matriz.shape
    for i in range(filas):
        for j in range(columnas):
            m[i][j] = m[i][j] * -1
    return m
#print(inversamatrizcomp([[1,2,3],[4,5,6,]]))

def multescamatrizcomp(n,m):
    matriz = np.array(m)
    filas, columnas = matriz.shape
    for i in range(filas):
        for j in range(columnas):
            m[i][j] = n * m[i][j]
    return m

#print(multescamatrizcomp((2),[[1+2j,2+1j],[2+3j,1+2j]]))

def transmatriz(m):
    matriz = []
    for i in range(len(m[0])):
        matriz.append([])
        for j in range(len(m)):
            matriz[i].append(m[j][i])
    return matriz

#print(transmatriz([[1,2,3],[11,12,13]]))

def conjugadamatriz(m):
    for i in range(len(m[0])):
        return m

#print(conjugadamatriz([[1,2],[3,4]]))

def normavect(v):
    for i in range(len(v)):
        v[i] = v[i] ** 2
        x = 0
    for i in range(len(v)):
        y = v[i]
        x = x + y
    return str(math.sqrt(x))

#print(normavect([2,1]))

def adjuntamatriz(m):
    matriz = np.array(m)
    filas, columnas = matriz.shape
    for i in range(filas):
        for j in range(columnas):
            m[i][j] = np.conj(m[i][j])
    for i in range(filas):
        for j in range(columnas):
            m[i][j] = m[j][i]
    return m

#print(adjuntamatriz([[2+3j, 1+5j],[2+5j, 8+7j]]))

def producto_matrices(a, b):
    filas_a = len(a)
    filas_b = len(b)
    columnas_a = len(a[0])
    columnas_b = len(b[0])
    if columnas_a != filas_b:
        return None
        producto = []
        for i in range(filas_b):
            producto.append([])
            for j in range(columnas_b):
                producto[i].append(None)
        for c in range(columnas_b):
            for i in range(filas_a):
                suma = 0
                for j in range(columnas_a):
                    suma += a[i][j] * b[j][c]
                producto[i][c] = suma
        return producto

#print(producto_matrices([[3, 2, 1],[1, 1, 3],[0, 2, 1]],[[2,1],[1,0],[3,2]]))

def productointernodosvec(m,n):
    x = m[0] * n[0]
    y = m[1] * n[1]
    return x + y

#print(productointernodosvec([2,-1],[5,1]))

def distanciavec(m,n):
    x = (m[0] + n[0]) ** 2
    y = (m[1] + n[1]) ** 2
    a = x + y
    return str(math.sqrt(a))
#print(distanciavec([2,1],[1,2]))

def productotensor(m,n):
    a = np.array(m)
    b = np.array(n)
    x = np.tensordot(m, n)
    return x
print(productotensor([[2,2],[1,1]],[[1,1],[1,1]]))
