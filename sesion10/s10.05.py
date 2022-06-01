
### EJERCICIO DE PC ###

"""
2021-2 2.02
1. (5 points) Evalúa matrices
Desarrolle e implemente un programa que solicite el tamaño de una matriz cuadrada, y
realice lo siguiente:
• El tamaño de la matriz es mayor a 2.
• Generar dos matrices cuadradas con valores aleatorios enteros entre 1 y 5
• Imprimir ambas matrices
• Generar e imprimir una tercera matriz, también cuadrada que tenga el número 1
en las posiciones en que los valores de las dos primeras matrices coincidan tanto en
valor como en posición y 0 si no coinciden.

Orden de la matriz cuadrada : 4
Matriz 1:
4 2 3 1
4 1 2 3
5 2 3 3
1 5 4 2
Matriz 2:
1 2 3 2
2 4 3 5
3 1 3 4
3 1 5 3
Matriz de Coincidencias :
0 1 1 0
0 0 0 0
0 0 1 0
0 0 0 0

Orden de la matriz cuadrada : 6
Matriz 1:
4 2 3 1 4 1
2 3 5 2 3 3
1 5 4 2 1 2
3 2 2 4 3 5
3 1 3 4 3 1
5 3 3 4 5 3
Matriz 2:
4 2 2 3 5 4
2 5 5 3 4 5
1 1 4 2 2 1
2 4 3 1 2 2
1 1 5 3 2 1
2 5 4 3 5 1
Matriz de Coincidencias :
1 1 0 0 0 0
1 0 1 0 0 0
1 0 1 1 0 0
0 0 0 0 0 0
0 1 0 0 0 1
0 0 0 0 1 0

Orden de la matriz cuadrada : 3
Matriz 1:
4 2 3
1 4 1
2 3 5
Matriz 2:
2 3 3
1 5 4
2 1 2
Matriz de Coincidencias :
0 0 1
1 0 0
1 0 0
"""

import random

lado = int(input("Ingrese lado de la matriz: "))
while (lado <= 2):
    lado = int(input("Ingrese lado de la matriz: "))

def generar_matriz_2(lado):
    matriz = []
    for i in range(lado):
        matriz.append([])
        for j in range(lado):
            azar = random.randint(1, 5)
            matriz[i].append(azar)
    return matriz

def coincidencias(matriz1, matriz2, matriz3, lado):
    for fila in range(lado):
        for columna in range(lado):
            if (matriz1[fila][columna] == matriz2[fila][columna]):
                matriz3[fila][columna] = 1
            else:
                matriz3[fila][columna] = 0

def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()
    print()

matriz1 = generar_matriz_2(lado)
matriz2 = generar_matriz_2(lado)
matriz3 = generar_matriz_2(lado)

coincidencias(matriz1, matriz2, matriz3, lado)

imprimir_matriz(matriz1)
imprimir_matriz(matriz2)
imprimir_matriz(matriz3)
