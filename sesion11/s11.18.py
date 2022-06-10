
### EJERCICIO DE PC ###

"""
2021-2 1.03
2. (5 points) Evalúa listas por comprensión.
Desarrolle un programa que utilizando unicamente listas por comprensión realice 3 tareas
diferentes:
• Forme una lista con todos los números múltiplos de 7 comprendidos entre el 7 y el
100
• Forme una lista con todos los números de de dos dígitos que sean a la vez múltiplos de 2 y de 3
• Forme una matriz de 6 filas por 3 columnas en donde cada elemento sea el caracter #
• Para asignar el puntaje a esta pregunta es absolutamente necesario que
utilice (listas por comprensión)!!!

1. lista con todos los numeros multiplos de 7 comprendidos
entre el 7 y el 100
[7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]
2. lista con todos los numeros de de dos digitos que sean a
la vez multiplos de 2 y de 3
[12 , 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]
3. matriz de 6 filas por 3 columnas en donde cada elemento
sea la caracter #
[
    [’#’, ’#’, ’#’],
    [’#’, ’#’, ’#’],
    [’#’, ’#’, ’#’],
    [’#’, ’#’, ’#’],
    [’#’, ’#’, ’#’],
    [’#’, ’#’, ’#’]
]
"""

lista1 = [numero for numero in range(7, 100) if numero % 7 == 0]
print(lista1)

lista2 = [numero for numero in range(10, 100) if numero % 2 == 0 and numero % 3 == 0]
print(lista2)

matriz = [['#' for i in range(3)] for j in range(6)]
print(matriz)
