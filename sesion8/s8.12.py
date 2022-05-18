
### EJERCICIO DE PC ###

"""
2021-2 1.02
4. (5 points) Escribe una funci´on que reciba dos listas del mismo tamaño y retorne la suma
de los productos. Por ejemplo: [2,7,1] y [4,5,6] debería retornar 49.
NOTA: No se puede usar la funci´on sum ni cualquiera de sus variantes.

Input : [2 ,7 ,1] , [4 ,5 ,6] Output : 49

[2, 7, 1]
[4, 5, 6]
8 + 35 + 6 = 49

Input : [1 ,2 ,3] , [4 ,5 ,6] Output : 32

[1, 2, 3]
[4, 5, 6]
4 + 10 + 18 = 32
"""

def sumando_listas(lista1, lista2):
    suma_total = 0
    for i in range(len(lista1)):
        suma_total += lista1[i] * lista2[i]
    return suma_total

l1 = [2, 7, 1]
l2 = [4, 5, 6]

print(sumando_listas(l1, l2))
print(sumando_listas([1, 2, 3],[4, 5, 6]))

l3 = [4, 5]
l4 = [2, 5]
if len(l3) == len(l4):
    print(sumando_listas(l3, l4))
else:
    print("Las listas no tienen el mismo tamaño")
