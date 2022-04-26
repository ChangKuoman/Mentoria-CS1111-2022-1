
### EJERCICIO DE PC ###

"""
2021-1 2.06
4. (5 points) Desarolle un programa en Python que muestre el siguiente patrón mostrado
a continuación. Considere que N >= 1.

n:3
1
01
101

n: 5
0 1
1 0 1
2 1 0 1
3 0 1 0 1
4 1 0 1 0 1
  0 1 2 3 4
"""

n = int(input("N: "))

for i in range(n):
    for j in range(i+1):
        if (i + j) % 2 == 0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
