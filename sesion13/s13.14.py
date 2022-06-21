
### EJERCICIO DE PC ###

# recursividad
"""
2021-2 2.05
2. (5 points) Evalúa recursividad.
Realizar un programa en Python que contenga una función recursiva(OBLIGATORIO)
que reciba desde teclado una cadena separado por comas y retorne la sumatoria de sus
elementos PARES

Num : 1,2,3,4,5,6
Respuesta : 2+4+6 =12

Num : 1,1,3,3
Respuesta : 0
"""

cadena = str(input("Num: "))
lista = [int(i) for i in cadena.split(',')]

def suma_pares(lista):
    if (len(lista) == 1 and lista[0] % 2 == 0):
        return lista[0]
    elif (len(lista) == 1 and lista[0] % 2 != 0):
        return 0
    elif (lista[0] % 2 == 0):
        return lista[0] + suma_pares(lista[1::])
    else:
        return 0 + suma_pares(lista[1::])

print(suma_pares(lista))
