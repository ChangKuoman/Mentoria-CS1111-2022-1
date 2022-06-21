
### EJERCICIO ###

# recursividad

# Sea H(n) = n * (n-1) + H(n-1), redondear a 3 decimales y cuando n = 1, retorna 0

def H(n):
    # caso base
    if (n == 1):
        return 0
    # llamada recursiva
    else:
        return n * (n - 1) + H(n - 1)

print(round(H(15), 3))
