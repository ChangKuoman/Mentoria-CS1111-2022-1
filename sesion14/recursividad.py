
# recursividad

"""
8. Suma de N elementos de serie - recursividad
Diseñe una funcion recursiva sumaSerie(n) que calcule la suma de los primeros n elementos
de una serie (empezando por 1), donde el elemento i de la serie viene determinado
por la siguiente formula:
Ei = i3 + 5
Por lo tanto si n = 3, el resultado de la funcion seria:
suma = (1^3 + 5) + (2^3 + 5) + (3^3 + 5) = 51
O en el caso en que n = 4, el resultado de la funcion seria:
suma = (1^3 + 5) + (2^3 + 5) + (3^3 + 5) + (4^3 + 5) = 120
"""

def sumaSerie(n):
    # caso base
    if n == 1:
        return 1**3 + 5
    # llamada recursiva
    else:
        return n**3 + 5 + sumaSerie(n - 1)

print(sumaSerie(3))
print(sumaSerie(4))

"""
9. Crear lista de serie - recursividad
Utilizando la misma formula del ejercicio anterior
Ei = i^3 + 5
Elabore una funcion que le permita construir de forma recursiva una lista con los
elementos de la serie desde 1 hasta N. Algunos ejemplos de dialogo de este programa
serian (funcion sugerida):
Ejemplo lista de 1 a 5
lista = []
listaSerie (lista , 1, 5)
print ( lista ) # [6, 13, 32, 69, 130]
Ejemplo lista de 2 a 10
lista = []
listaSerie (lista , 2, 10)
print ( lista ) # [13 , 32, 69, 130 , 221 , 348 , 517 , 734 , 1005]
"""

def listaSerie(lista, inicio, fin):
    # caso base
    if inicio == fin:
        lista.append(sumaSerie(inicio))
        return
    # llamada recursiva
    else:
        lista.append(sumaSerie(inicio))
        return listaSerie(lista, inicio + 1, fin)

lista = []
listaSerie(lista, 1, 5)
print(lista)
