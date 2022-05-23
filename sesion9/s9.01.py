
### INTRODUCCION ###

# paso de listas en funciones

lista = [1, 2, 3, 4, 5]
suma = 5

def agregar_elementos(lista, elemento, elemento2):
    lista.append(elemento)
    lista.append(elemento2)


# lista.copy()
# lista[::]
agregar_elementos(lista, 8, 6)


def agregar_numeros(suma, num1, num2):
    suma += num1 + num2
    return suma


suma = agregar_numeros(suma, 5, 8)


print(lista)
print(suma)
