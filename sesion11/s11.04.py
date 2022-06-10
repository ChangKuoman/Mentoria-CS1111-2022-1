
### EJERCICIO ###

# Escribir un programa que pida una cadena de números y cuente la cantidad de dígitos por número y
# los agregue a un diccionario.

# 1234555
# {1: 1, 5: 3, ...}

cadena = str(input("Ingrese una cadena de numeros: "))

numeros = {}

for digito in cadena:
    if digito not in numeros.keys():
        numeros[digito] = 1
    else:
        numeros[digito] += 1

print(numeros)
