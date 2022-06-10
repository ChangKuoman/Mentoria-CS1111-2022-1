
### EJERCICIO ###

# UTILIZANDO LIST COMPREHENSION
# Crear un matriz de nxn números al azar del 10 al 99.

import random
n = int(input("Ingrese n: "))

matriz = [[random.randint(10, 99) for i in range(n)] for j in range(n)]
print(matriz)
