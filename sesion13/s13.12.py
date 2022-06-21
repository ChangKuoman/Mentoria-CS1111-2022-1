
### EJERCICIO DE PC ###

# recursividad
"""
2021-2 1.06
2. (5 points) Evalúa recursividad.
Implemente un algoritmo, usando una función recursiva, que resuelva la siguiente sumatoria:
K(n; p) = 1 * p + 2 * p + 3 * p + 4 * p + ... + n * p
* El programa debe solicitar al usuario que ingrese un número n, y un número d,
* Luego debe calcular el valor de H(n, p) usando una función recursiva,
* Debe imprimir el resultado de H(n, p)

Input n : 5
Input p : 2
Output : 30
"""

def H(n, p):
    if (n == 1):
        return p
    else:
        return n * p + H(n - 1, p)

print(H(5, 2))
