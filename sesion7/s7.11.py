
### EJERCICIO DE PC ###

"""
Diseñe e implemente un programa que permita leer una cadena de ADN y el programa genere e imprima la
cadena complementaria, respetando la correspondencia entre las bases: (A - T, C - G).

Cadena de ADN : acgttgcaaaccggtt
Cadena de ADN : ACGTTGCAAACCGGTT
Cadena complementaria : TGCAACGTTTGGCCAA

A -> T
T -> A
C -> G
G -> C
"""

cadena = str(input("Cadena ADN: "))

print("Cadena de ADN:", cadena.upper())

complementaria = ""
for i in cadena.lower():
    if i == 'a':
        complementaria += 'T'
    elif i == 't':
        complementaria += 'A'
    elif i == 'c':
        complementaria += 'G'
    elif i == 'g':
        complementaria += 'C'

print("Cadena complementaria:", complementaria)
