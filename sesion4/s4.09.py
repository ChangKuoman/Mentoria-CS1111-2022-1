
### EJERCICIO DE PC ###

"""
2021-2 3.04
3. (5 points) Evalúa estructuras de control selectivas y repetitivas.
Escriba un programa en Python que imprima todos los números del 1 al 100, excepto
los múltiplos de 3. TIP: Utilize continue.
"""

for i in range(1, 101):
    if i % 3 == 0:
        continue
    else:
        print(i)
