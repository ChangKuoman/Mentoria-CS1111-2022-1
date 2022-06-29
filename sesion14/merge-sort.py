
# merge sort

def merge(left, right, lista):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lista[k] = left[i]
            k = k+1
            i = i+1

        else:
            lista[k] = right[j]
            k = k+1
            j = j+1

    while i < len(left):
        lista[k] = left[i]
        i = i+1
        k = k+1

    while j < len(right):
        lista[k] = right[j]
        j = j+1
        k = k+1

def merge_sort(lista):
    n = len(lista)
    if n > 1:
        mitad = n//2
        left = lista[:mitad]
        right = lista[mitad:]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, lista)


lista = [5, 8, 6, 5, 4, 2]
merge_sort(lista)
print(*lista)
