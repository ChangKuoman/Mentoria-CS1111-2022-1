
### INTRODUCCION ###

# listas
lista = [9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9]

lista = list(set(lista))

n = int(input("Ingrese un numero a remover (1-9): "))
lista.remove(n)

print(lista)
