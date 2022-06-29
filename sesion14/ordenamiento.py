
# ordenamiento

asistentes = {
1: [43 , 39 , 23 , 52 , 21 , 48 , 31 , 26 , 55 , 32] ,
2: [51 , 29 , 47 , 40 , 32 ,25 , 31 , 29 , 51 , 36] ,
3: [30 , 43 , 52 , 23 , 37 , 51 , 29 , 50 , 26 , 35] ,
4: [36 , 44 , 49 , 22 , 44 , 49 , 55 , 48 , 52 , 51] ,
5: [32 , 29 , 43 , 32 , 32 , 36 , 22 , 48 , 38 , 29]
}

def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

for value in asistentes.values():
    bubble_sort(value)

print(asistentes)
