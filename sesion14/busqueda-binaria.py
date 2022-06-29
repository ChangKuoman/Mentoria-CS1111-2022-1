
# busqueda binaria
# !!! la lista tiene que estar ordenada

def binaria(lista, elem):

    if len(lista) == 1:
        return lista[0] == elem

    n = len(lista)
    mitad = n//2
    if lista[mitad] == elem:
        return True

    elif lista[mitad] < elemento:
        return binaria(lista[mitad:], elem)
    elif lista[mitad] > elemento:
        return binaria(lista[:mitad], elem)

def busqueda_iter(lista, elem):
    low = 0
    high = len(lista) -1
    resultado = False

    while low <= high:
        mid = low + (high-low)//2

        if lista[mid] == elem:
            resultado = True
            break

        if elem <=lista[mid]:
            high = mid - 1

        if elem > lista[mid]:
            low = mid + 1

    return resultado
