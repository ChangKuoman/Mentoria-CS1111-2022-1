
### EJERCICIO ###

# recursividad
# Escribir una función recursiva que realice la suma de una lista de números

def sumar_lista(lista):
    # casos base
    if (len(lista) == 1):
        return lista[0]
    elif (len(lista) == 0):
        return 0
    # llamada recursiva
    else:
        return lista[0] + sumar_lista(lista[1::])

print(sumar_lista([0, 1, 2, 3]))

print(sumar_lista([3]))

print(sumar_lista([]))
