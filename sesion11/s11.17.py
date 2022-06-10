
### EJERCICIO DE PC ###

"""
2021-2 1.02
2. (5 points) Evalúa listas por comprensión.
Utilizando listas por comprensión. Resuelve los siguientes enunciados:
• Escribe una función que reciba un string y retorne el mismo string sin vocales.
Nota: Utilizar ””.join([])
• Escribe una función que recibe un string y retorne todas las palabras menores con
5 caracteres o menos en una lista. Nota: Utilizar split()
• Escribe una función que recibe el largo N y ancho M y genere una matriz de números
random. Nota: Utilizar lista por comprensión anidada.

Caso 1. Input : " sebastian " Output : " sbstn "
Caso 2. Input : " Las nubes son grises " Output : ["Las"," nubes ", "son"]
Caso 3. Input :"N: 3, M: 3" Output :
[
    [ 4, 2, 2]
    [ 5, 5, 2]
    [ 7, 8, 10]
]
"""

import random

def funcion1(cadena):
    lista = [letra for letra in cadena if letra not in "aeiouAEIOU"]
    return "".join(lista)

def funcion2(frase):
    lista = [palabra for palabra in frase.split() if len(palabra) <= 5]
    return lista

def funcion3(N, M):
    matriz = [[random.randint(1, 9) for i in range(M)] for j in range(N)]
    return matriz

print(funcion1("sebastian"))
print(funcion2("Las nubes son grises"))
print(funcion3(3, 3))
