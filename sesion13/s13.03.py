
### EJERCICIO ###

# recursividad
# 2. (Nivel 1) Elabore un programa recursivo para calcular el numero armonico, este algoritmo
# se dene por:
# Hn = 1 + 1/2 + 1/3 + ... + 1/N
# Esta funcion recibira como parametros los siguientes valores:
#  numero (N): Es el numero de la secuencia.
# Tome en consideracion la condicion de salida y la llamada recursiva.
# Algunos ejemplos de dialogo de este programa serian:
# Input : 2
# Output : 1.5
# Input : 10
# Output : 2.929
def armonico(n):
    # caso base
    if (n == 1):
        return 1
    else:
        return 1/n + armonico(n-1)

n = int(input("Input: "))
print(armonico(n))
