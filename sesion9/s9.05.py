
### EJERCICIO ###

# listas
"""
Dada una lista de n ́umeros construya una funci ́on que extraiga una secuencia
de n ́umeros dada dos posiciones. Presente el resultado como la suma de esos n ́umeros
extra ́ıdos. Los n ́umeros ingresados se incorporan como una lista en una sola l ́ınea.
Algunos ejemplos de di ́alogo de este programa ser ́ıan:
Input : 3 4 5 6 7 9 1 2 3 4
pos1 : 3
pos2 : 5
Output : 18
Input : 3 4 1 2 7 9 1 2 3 4
pos1 : 5
pos2 : 8
Output : 19
"""

cadena = str(input("Input: "))
lista = []
for numero in cadena.split(" "):
    lista.append(int(numero))

pos1 = int(input("pos1: "))
pos2 = int(input("pos2: "))

# para usar indices
pos1 -= 1

# sublista = lista[pos1:pos2:1]
suma = 0
for i in range(pos1, pos2, 1):
    suma += lista[i]

print("Output:", suma)
