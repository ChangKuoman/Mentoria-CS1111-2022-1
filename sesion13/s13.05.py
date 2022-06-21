
### EJERCICIO ###

# recursividad
# 4. (Nivel 1) Elabore un programa que solicite al usuario el ingreso de un numero entero N
# y un decremento X. Dena una funcion recursiva denominada imprimeserie, que recibe
# ambos valores e imprime la resta de N - X, de forma sucesiva hasta llegar a 0 o un valor
# muy cercano con lo cual se imprime el mensaje: \Fin".
# Esta funcion recibira como parametros los siguientes valores:
#  numero (N): Es el numero inicial.
#  decremento (X): Es un numero entero que sera restado a N.
# Algunos ejemplos de dialogo de este programa serian:
# Ingrese numero : 40
# Ingrese decremento : 5
# 40 35 30 25 20 15 10 5 Fin
# Ingrese numero : 20
# Ingrese decremento : 3
# 20 17 14 11 8 5 2 Fin

def imprimeserie(n, x):
    # caso base
    if (n <= 0):
        return "Fin"
    # llamada recursiva
    else:
        return str(n) + " " + imprimeserie(n - x, x)

print(imprimeserie(40, 5))
