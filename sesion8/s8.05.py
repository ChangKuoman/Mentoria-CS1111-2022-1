
### INTRODUCCION ###

# listas
lista = []

for i in range(5):
    n = int(input("Ingrese un numero: "))
    if n % 2 == 0:
        lista.append(n)

print(lista)

n = int(input("Ingrese otro numero: "))

lista.insert(0, n)

print(lista)
