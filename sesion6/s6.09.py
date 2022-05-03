
### INTRODUCCION ###

# listas
lista = [1, 3, 4, 5, 6, True, "cadena", [1, 2], 45.21]
#       0  1  2  3  4   5       6
print(lista[8])

for elemento in lista:
    print(elemento)

lista.append(90)
print(lista)
lista.pop(0)
print(lista)

lista = [1, "1", 1.2, True] # corchetes
