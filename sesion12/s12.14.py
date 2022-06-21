
### EJERCICIO DE PC ###

"""
PC3 2022-1 Lab 1.06
1.  (5 points)  Listas.Desarrolle un programa que permita leer varios n ́umeros y almacenarlos en una lista.No se sabe cuantos n ́umeros son, pero el ingreso termina cuando el usuario ingresa elnumero 0.  El cero no formar ́a parte de lista.  El programa debe luego imprimir la listaleida y luego imprimir la lista desde la posici ́on de medio hacia los costados.  Considereque el tama ̃no de la lista puede ser par o impar.Algunos ejemplos de di ́alogo de este programa ser ́ıan:

Numero : 1
Numero : 2
Numero : 3
Numero : 4
Numero : 5
Numero : 6
Numero : 7
Numero : 8
Numero : 9
Numero : 0
Lista  leida: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Ahora  se  imprimen  los  elementos  desde  la  posicion  del  medio
5   4   6   3   7   2   8   1   9

Numero : 1
Numero : 2
Numero : 3
Numero : 4
Numero : 5
Numero : 6
Numero : 0
Lista  leida: [1, 2, 3, 4, 5, 6]
Ahora  se  imprimen  los  elementos  desde  la  posicion  del  medio
3   4   2   5   1   6
"""
lista = []

while True:
    numero = int(input("Numero: "))
    if numero == 0:
        break
    lista.append(numero)

print("Lista leida:", lista)

print("Ahora se imprimen los elementos desde la posicion del medio")
if (len(lista) % 2 == 0):
    for i in range(len(lista)//2):
        print(lista[len(lista)//2 - 1 - i], end =" ")
        print(lista[len(lista)//2 + i], end = " ")
else:
    print(lista[len(lista)//2], end =" ")
    for i in range(len(lista)//2):
        print(lista[len(lista)//2 - 1 - i], end =" ")
        print(lista[len(lista)//2 + 1 + i], end = " ")
