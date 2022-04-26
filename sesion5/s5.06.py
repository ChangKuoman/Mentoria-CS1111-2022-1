
### EJERCICIO DE PC ###

"""
2021-2 3.04
4. (5 points) Evalúa bucles anidados.
Dado un input N, escriba un programa en Python donde cada linea tiene una estrella
más que la linea anterior y al llegar a N estrellas las siguientes lineas tendrán una estrella
menos que la linea anterior hasta llegar a 1 estrella. Por ejemplo:

N = 5:
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

N = 3:
*
* *
* * *
* *
*

N = 1:
*
"""

n = int(input("N: "))
i = 1
while (i < n):
    for j in range(i):
        print("*", end=" ")
    i += 1
    print()

while (i >= 1):
    for j in range(i):
        print("*", end=" ")
    i -= 1
    print()
