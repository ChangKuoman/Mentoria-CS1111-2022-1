
# enunciado: l1.JPG

def SplitList(lista, sep):
    nueva_lista = []
    sublista = []
    for elemento in lista:
        if elemento == sep:
            nueva_lista.append(sublista)
            sublista = []
        else:
            sublista.append(elemento)
    nueva_lista.append(sublista)
    return nueva_lista

print(SplitList([5, 2, 0, 1, 3, 6, 0, 4, 6], 0))
