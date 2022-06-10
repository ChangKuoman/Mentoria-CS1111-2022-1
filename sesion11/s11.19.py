
### EJERCICIO ###

"""
14. Matriz
Dada la siguiente matriz de números:
4 5 6 3
1 4 6 7
8 2 3 6
3 5 4 9
3 4 5 3
Implemente un algoritmo que realice lo siguiente:
• Escribir la matriz en el programa principal
• Solicite al usuario un número de columna, y el programa debe imprimir el promedio
de los números de esa columna
• Solicite al usuario un número de fila y columna, y el programa debe:
Imprimir el producto de todos los números que estan alrededor de esa posición
de fila y columna.
Immprimir el mayor número que esta alrededor de esa posición de fila y columna
Recordar que la fila y columna comienzan desde cero.
Algunos ejemplos de diálogo de este programa serían:

Ingrese columna : 3
El promedio de la columna 3 es: 5.6
Ingrese fila : 4
Ingrese columna : 1
El producto alrededor de (4 ,1) es: 900
El mayor numero alrededor de (4 ,1) es: 5
"""

matriz = [
    [4, 5, 6, 3],
    [1, 4, 6, 7],
    [8, 2, 3, 6],
    [3, 5, 4, 9],
    [3, 4, 5, 3]
]

columna = int(input("Ingrese columna: "))
suma = 0
cantidad = 0
for i in range(len(matriz)):
    suma += matriz[i][columna]
    cantidad += 1
print("promedio:", suma/cantidad)

fila = int(input("Ingrese fila: "))
columna = int(input("Ingrese columna: "))
producto = 1
primero = True
for i in range(-1, 2, 1):
    for j in range(-1, 2, 1):
        if i == 0 and j == 0:
            continue
        if fila + i < 0 or fila + i >= len(matriz) or columna + j < 0 or columna + j >= len(matriz[0]):
            continue
        producto *= matriz[fila+i][columna+j]
        if primero == True:
            mayor = matriz[fila+i][columna+j]
            primero = False
        else:
            if matriz[fila+i][columna+j] > mayor:
                mayor = matriz[fila+i][columna+j]

print(producto)
print(mayor)
