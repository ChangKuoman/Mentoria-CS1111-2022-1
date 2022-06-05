
# enunciado: lc1.JPG

def funcion1(lista):
    lista2 = [elemento**2 for elemento in lista if (elemento % 6 != 0) and (elemento % 2 == 0)]
    return lista2

print(funcion1([1, 2, 3, 4, 5, 6, 7, 8]))

def funcion2(fila, columna, valor):
    matriz = [[valor for i in range(columna)] for j in range(fila)]
    return matriz

print(funcion2(3, 2, 1))

def funcion3(lista):
    pares = [elemento for elemento in lista if elemento % 2 == 0]
    impares = [elemento for elemento in lista if elemento % 2 != 0]
    return pares, impares

print(funcion3([1, 2, 3, 4, 5, 6, 7, 8]))

def funcion4(matriz):
    lista = [matriz[i][j] for i in range(len(matriz)) for j in range(len(matriz[0]))]
    return lista

print(funcion4([[1, 2], [3, 4], [5, 6]]))
