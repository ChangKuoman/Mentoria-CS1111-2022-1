
### EJERCICIO ###

# UTILIZANDO LIST COMPREHENSION
# Crear una lista de n números (float) al azar del 10 al 20 redondeado a 2 decimales. Use la función uniform
# de la librería random

import random
n = int(input("Ingrese n: "))

lista = [round(random.uniform(10, 20), 2) for i in range(n)]
print(lista)
