
### EJERCICIO DE PC ###

"""
Realice un programa que permita generar ”n” números al azar cuyos valores pueden estar desde el 100 al 999,
y el programa forme diccionario en donde el número sea la clave y el valor asociado sea el número deletreado
en quechua.
Note que al ser un diccionario no puede tener claves repetidas.
En la siguiente tabla se muestran la equivalencia de cada dígito en quechua.
numeros = {
    0: "Chusaq",
    1: "Huk",
    2: "Iskay",
    3: "Kinsa",
    4: "Tawa",
    5: "Pisqa",
    6: "Soqta",
    7: "Qanchis",
    8: "Pusaq",
    9: "Esqon"
}
"""

numeros = {
    0: "Chusaq",
    1: "Huk",
    2: "Iskay",
    3: "Kinsa",
    4: "Tawa",
    5: "Pisqa",
    6: "Soqta",
    7: "Qanchis",
    8: "Pusaq",
    9: "Esqon"
}

dict = {}

import random
cantidad = int(input("Cuantos numeros generar: "))
for i in range(cantidad):
    azar = random.randint(100, 999)
    quechua = ""
    for digito in str(azar):
        quechua += numeros[int(digito)] + " "
    dict[azar] = quechua

for key, value in dict.items():
    print(key, value)
