
### EJERCICIO DE PC ###

"""
Desarrolle un programa que pida al usuario ingresar una opción (a, b, c) y
tambien le pida ingresar 5 numeros, y realize los siguientes calculos:
• Si escogió la opción a entonces debe imprimir el promedio de los numeros
• Si escogió la opción b entonces debe imprimir la cantidad de numeros pares
• Si escogió la opción c entonces debe imprimir la cantidad numero que son de múltiplos de 4
"""

def hallar_promedio():
    suma = 0
    for i in range(5):
        num = int(input("Ingrese numero: "))
        suma += num
    return suma/5

def hallar_pares():
    cantidad = 0
    for i in range(5):
        num = int(input("Ingrese numero: "))
        if es_par(num) == True:
            cantidad += 1
    return cantidad

def hallar_multiplos4():
    cantidad = 0
    for i in range(5):
        num = int(input("Ingrese numero: "))
        if num % 4 == 0:
            cantidad += 1
    return cantidad

opcion = str(input("Ingrese opcion (a, b, c): "))

if opcion == 'a':
    print(hallar_promedio())
elif opcion == 'b':
    print(hallar_pares())
elif opcion == 'c':
    print(hallar_multiplos4())
else:
    print("No se ingreso una opcion correcta")
