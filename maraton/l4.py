
# enunciado: l4.JPG

def imprimir_lados(lista):
    for i in range(len(lista)//2):
        print(lista[i], end=" ")
        print(lista[len(lista)-1-i], end=" ")

    if len(lista) % 2 != 0:
        print(lista[len(lista)//2], end=" ")

    print()

imprimir_lados([8, 1, 2, 1, 4])

imprimir_lados([1, 2, 3, 4, 5, 6])
