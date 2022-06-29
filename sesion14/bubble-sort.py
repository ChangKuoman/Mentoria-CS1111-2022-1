
# bubble sort

lista = [5, 8, 6, 5, 4, 2]
# 1      5, 6, 5, 4, 2, 8  !!!!

# lista = sorted(lista)
# lista.sort()

def burbuja(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

burbuja(lista)
print(*lista)
