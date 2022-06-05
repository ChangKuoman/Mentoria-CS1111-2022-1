
# enunciado: l2.JPG

elementos = str(input("Ingresar lista: "))
lista = []
for nota in elementos.split(","):
    lista.append(int(nota))

maxima = max(lista)

maxima_2 = lista[0]
for nota in lista:
    if nota > maxima_2:
        maxima_2 = nota

nueva_lista = [maxima]
for nota in lista:
    if nota != maxima:
        nueva_lista.append(nota)

print(nueva_lista)
