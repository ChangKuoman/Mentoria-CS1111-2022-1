
### EJERCICIO ###

# Escribir un programa que genere dos matrices de 5x5 con número al azar entre 1 y 9,
# luego cree una nueva matriz con la multiplicación de las dos matrices. Imprimir
# las 3 matrices.

import random

def generar_matriz(matriz, lado):
    for i in range(lado):
        matriz.append([])
        for j in range(lado):
            azar = random.randint(1, 9)
            matriz[i].append(azar)

def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()
    print()

def multiplicar(matriz_1, matriz_2, matriz_3):
    for i in range(len(matriz_1)):
        for j in range(len(matriz_1[i])):
            matriz_3[i][j] = matriz_1[i][j] * matriz_2[i][j]


matriz_1 = []
matriz_2 = []
matriz_3 = []

generar_matriz(matriz_1, 5)
generar_matriz(matriz_2, 5)
generar_matriz(matriz_3, 5)

multiplicar(matriz_1, matriz_2, matriz_3)

imprimir_matriz(matriz_1)
imprimir_matriz(matriz_2)
imprimir_matriz(matriz_3)
