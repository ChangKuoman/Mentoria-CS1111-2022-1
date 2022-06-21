
### EJERCICIO ###

# recursividad
# 1. (Nivel 1) Desarrolle un algoritmo que implemente una funcion recursiva que permita
# contar cuantos digitos tiene un numero.
# Algunos ejemplos de dialogo de este programa serian:
# Input : 123456
# Output : 6
# Input : 111
# Output : 3
def contar(n):
    # caso base
    if (n < 10):
        return 1
    # llamada recursiva
    else:
        return 1 + contar(n//10)

n = int(input("Input: "))
print(contar(n))
