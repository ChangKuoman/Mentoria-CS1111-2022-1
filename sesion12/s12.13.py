
### EJERCICIO ###

# recursividad
# Crear una función recursiva que calcule la suma de los cuadrados de 1 a n.

def suma_cuadrados(n):
    if n == 1:
        return 1
    else:
        return n**2 + suma_cuadrados(n-1)

print(suma_cuadrados(5))

print(suma_cuadrados(1))
