
### EJERCICIO DE PC ###

"""
Implemente un programa que dada una secuencia de N números enteros (positivos,
negativos y ceros), determine con la ayuda de un solo bucle, el promedio de los números
negativos y el promedio de los números positivos.
a) Simule el ingreso de los datos con la función input()
b) Simule el ingreso de datos con la función random.randint()
"""

from random import randint

n = int(input("Ingrese cantidad: "))

suma_positivos = 0
cant_positivos = 0
suma_negativos = 0
cant_negativos = 0
for i in range(n):
    # numero = int(input("Ingrese un numero: ")) # a
    numero = randint(-20, 20) # b
    if numero < 0:
        suma_negativos += numero
        cant_negativos += 1
    else:
        suma_positivos += numero
        cant_positivos += 1

if cant_positivos != 0:
    print("Promedio positivos: {}".format(suma_positivos/cant_positivos))
else:
    print("NO SE ENCONTRARON NUMEROS positivos")

if cant_negativos != 0:
    print("Promedio negativos: {}".format(suma_negativos/cant_negativos))
else:
    print("NO SE ENCONTRARON NUMEROS NEGATIVOS")
