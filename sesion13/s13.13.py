
### EJERCICIO DE PC ###

# recursividad
"""
2021-2 2.02
2. (5 points) Evalúa recursividad.
Desarrolle un programa que permita formar una lista con 20 números enteros, cuyos
valores estén entre 1 y 9. Luego el programa realice los siguiente:
• Imprima la lista generada, a continaución
• Lea como dato un número ”n” cuyo valores estan entre 1 y 9 y por medio de una
función recursiva halle la cantidad de ocurrencias de ”n” en la lista antes creada.
• Para resolver esta pregunta no puede utilizar la funcion count.
• Para asignar el puntaje a esta pregunta es absolutamente necesario que realice
una función recursiva

[8, 2, 9, 8, 1, 7, 7, 1, 6, 3, 2, 5, 7, 5, 5, 2, 9, 2, 7, 1]
Numero : 7
El numero 7 aparece 4 veces

[2, 7, 3, 5, 6, 4, 3, 9, 1, 1, 1, 8, 9, 3, 5, 9, 8, 2, 5, 7]
Numero : 1
El numero 1 aparece 3 veces

[1, 8, 5, 3, 9, 9, 3, 3, 7, 9, 4, 5, 7, 8, 9, 2, 1, 4, 5, 2]
Numero : 8
El numero 8 aparece 2 veces

[8, 7, 9, 5, 3, 1, 6, 5, 6, 1, 6, 3, 5, 6, 7, 6, 1, 3, 3, 3]
Numero : 4
El numero 4 aparece 0 veces
"""
import random
lista = [random.randint(1, 9) for i in range(20)]
numero = random.randint(1, 9)

def contar_lista(lista, numero):
    if (len(lista) == 1 and lista[0] == numero):
        return 1
    elif (len(lista) == 1 and lista[0] != numero):
        return 0
    elif (lista[0] == numero):
        return 1 + contar_lista(lista[1::], numero)
    else:
        return 0 + contar_lista(lista[1::], numero)

print(lista)
print(numero)
print(contar_lista(lista, numero))
