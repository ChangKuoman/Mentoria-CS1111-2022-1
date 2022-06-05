import random

# enunciado: l2.JPG

frase = str(input("Ingrese frase: "))

lista1 = [len(palabra) for palabra in frase.split(" ")]

print(lista1)

n = int(input("Numero de elementos: "))

lista2 = [random.randint(100, 999) for i in range(n)]

print(lista2)

d = int(input("Cantidad de datos: "))

lista3 = [random.randint(20000, 30000) for j in range(d)]

print("Soles", lista3)

lista4 = [soles*0.25 for soles in lista3]

print("Dolares", lista4)
