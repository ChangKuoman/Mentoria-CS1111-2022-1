
### EJERCICIO ###

# Teniendo en cuenta la siguiente matriz, imprimir la suma de la columna 2020 y la fila 'abr'.

meses = [
    ['mes', 2019, 2020, 2021],
    ['ene', 50,    16,   49],
    ['feb', 13,    47,   61],
    ['mar', 15,    82,   46],
    ['abr', 20,    17,   95]
]

suma_2020 = 0
for i in range(1, len(meses)):
    suma_2020 += meses[i][2]
print(suma_2020)

suma_abr = 0
for i in range(1, len(meses[4])):
    suma_abr += meses[4][i]
print(suma_abr)
