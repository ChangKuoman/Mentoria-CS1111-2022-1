
# enunciado: l5.JPG

n1 = int(input("Cant elementos l1: "))
lista1 = []
for i in range(n1):
    numero = int(input(f"Ingrese valor {i+1}: "))
    lista1.append(numero)

n2 = int(input("Cant elementos l1: "))
lista2 = []
for i in range(n2):
    numero = int(input(f"Ingrese valor {i+1}: "))
    lista2.append(numero)

print("Lista 1:", lista1)
print("Lista 2:", lista2)

interseccion = []
for numero in lista1:
    if numero in lista2 and numero not in interseccion:
        interseccion.append(numero)

diferencia = []
for numero in lista1:
    if numero not in lista2 and numero not in diferencia:
        diferencia.append(numero)

pares = []
for numero in lista1:
    if numero % 2 == 0 and numero not in pares:
        pares.append(numero)
for numero in lista2:
    if numero % 2 == 0 and numero not in pares:
        pares.append(numero)

print("interseccion", interseccion)
print("diferencia l1-l2", diferencia)
print("pares", pares)
