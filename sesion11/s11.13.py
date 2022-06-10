
### EJERCICIO ###

# UTILIZANDO LIST COMPREHENSION
# Escribir un programa que genere una lista con n números al azar del 1 al 9 e imprimirla.
# Luego generar otras 2 listas de pares e impares de los números de la lista original.

import random
n = int(input("Ingrese n: "))
lista = [random.randint(1, 9) for i in range(n)]
print(lista)
pares = [numero for numero in lista if numero % 2 == 0]
impares = [numero for numero in lista if numero % 2 != 0]
print(pares)
print(impares)
