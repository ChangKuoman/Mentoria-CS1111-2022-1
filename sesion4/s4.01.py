
### EJERCICIO DE PC ###

"""
PC1 2021-2 1.02
1. (5 points) Evalúa estructuras de control selectivas.
Se desea obtener el día de la semana en base a un número entero. Escribir un pro-
grama en Python que reciba un entero como input e imprima que día de la semana
es.

• Input:1 Output: Lunes
• Input:7 Output: Domingo
• Input:8 Output: Invalido
"""

dia = int(input("Input: "))

if dia == 1:
    print("Lunes")
elif dia == 2:
    print("MArtes")
elif dia == 3:
    print("Miercoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sabado")
elif dia == 7:
    print("Domindo")
else:
    print("Invalido")
