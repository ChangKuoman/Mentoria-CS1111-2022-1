
# enunciado: l3.JPG

nombres1 = str(input("Lista 1: "))
nombres2 = str(input("Lista 2: "))

lista1 = []
for nombre in nombres1.split(","):
    lista1.append(nombre)

lista2 = []
for nombre in nombres2.split(","):
    lista2.append(nombre)

union = []
for nombre in lista1:
    if nombre not in union:
        union.append(nombre)

for nombre in lista2:
    if nombre not in union:
        union.append(nombre)

union.sort()
union = sorted(union)

nombres = ",".join(union)
print("Union:", nombres)
