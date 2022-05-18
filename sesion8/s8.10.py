
### EJERCICIO ###

# Pedir al usuario ingresar números hasta que ingrese 0, y agregarlos a una lista si son pares y otra si son impares.

lista_pares = []
lista_impares = []

while True:
    n = int(input("Ingrese numero: "))
    if n == 0:
        break

    if n % 2 == 0:
        lista_pares.append(n)
    else:
        lista_impares.append(n)

print(lista_pares)
print(lista_impares)
