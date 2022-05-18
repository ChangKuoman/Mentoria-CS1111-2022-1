
### EJERCICIO DE PC ###

"""
Desarrollar e implentar un programa que permita formar dos listas de números enteros con datos aleatorios del 0 al 50. El tamaño de cada lista será ingresado como dato. Cada lista representa a un conjunto por lo tanto no contendrá elementos
repetidos. Con estas listas realice lo siguiente:
• Imprima cada lista
• Por medio de la una función Interseccion, halle la lista intersección, es decir aquella que contiene los elementos comunes a ambas listas. La función debe recibir como parámetros las dos listas y formar la lista intersección de modo tal que no contenga elementos repetidos.
"""

from random import randint

def llenar_lista(lista, n):
    while n > 0:
        num = randint(0, 50)
        if num not in lista:
            lista.append(num)
            n -= 1

def interseccion(lista1, lista2):
    lista_interseccion = []
    for elemento in lista1:
        if elemento in lista2:
            lista_interseccion.append(elemento)
    return lista_interseccion

lista1 = []
lista2 = []

long1 = int(input("Long1: "))
long2 = int(input("Long2: "))

llenar_lista(lista1, long1)
llenar_lista(lista2, long2)

print(lista1)
print(lista2)

lista3 = interseccion(lista1, lista2)

print(lista3)
