
### EJERCICIO ###

# Teniendo en cuenta la siguiente matriz, imprimir la suma del total de medallas.

tokyo2020 = [
    ['País', 'Oro', 'Plata', 'Bronce'],  # 0
    ['EEUU', 39, 41, 33],  # 1
    ['China', 38, 32, 18],  # 2
    ['Japón', 27, 14, 17]  # 3
]

total_medallas = 0
for i in range(1, len(tokyo2020)): # filas
    for j in range(1, len(tokyo2020[i])): # columnas
        total_medallas += tokyo2020[i][j]

print(total_medallas)
