
### EJERCICIO ###

# recursividad
# 3. (Nivel 1) Elabore un programa recursivo para implementar una funcion factorial. Dado
# un numero N imprimir el resultado.
# Esta funcion recibira como parametros los siguientes valores:
#  numero (N): Es el numero inicial.
# Algunos ejemplos de dialogo de este programa serian:
# Input : 5
# Output : 120
def factorial(n):
    # caso base
    if (n == 1):
        return 1
    elif (n == 0):
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Input: "))
print(factorial(n))
