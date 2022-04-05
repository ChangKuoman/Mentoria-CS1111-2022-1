
### EJERCICIO DE PC ###

"""
2021-2 3.04
1. (5 points) Evalúa estructuras de control selectivas.
Se dice que un número es "crypto" si cumple alguna de las siguientes especicaciones:
• es negativo.
• es positivo y es múltiplo de 3.
• es positivo y es mayor a 77 y su último dígito es 5.
Escriba un programa un python que imprima si un número es "crypto" o no.

n = -5
Es Crypto

n = 15
Es Crypto

n = 85
Es Crypto

n = 11
No Es Crypto

n = 76
No Es Crypto
"""

n = int(input("Ingrese un número: "))

if n < 0:
    print("Es Crypto.")
elif n > 0 and n % 3 == 0:
    print("Es Crypto.")
elif n > 77 and n % 10 == 5:
    print("Es Crypto.")
else:
    print("No Es Crypto.")
