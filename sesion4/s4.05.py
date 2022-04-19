
### EJERCICIO ###

# Crear un programa que pida al usuario dos números, uno <inicial> y otro
# <final>. Imprimir aquellos números que se encuentren entre ambos y al mismo
# tiempo sean divisibles entre 2 y 3

inicial = int(input("Ingrese numero 1: "))
final = int(input("Ingrese numero 2: "))

for i in range(inicial+1, final):
    if i%2 == 0 and i%3 == 0:
        print(i, end=" ")
