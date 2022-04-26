
### EJERCICIO DE PC ###

"""
2021-0 1.02
Escribe un programa que lea un n ́umero entero N como entrada y retorne
como salida una ’X’ dibujada en un cuadrado de N × N.
Input :
5
Output :
  0 1 2 3 4
0 *       *
1   *   *
2     *
3   *   *
4 *       *
"""

n = int(input("N: "))

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
