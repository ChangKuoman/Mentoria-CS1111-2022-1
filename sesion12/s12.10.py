
### EJERCICIO ###

# recursividad
# Escribir una función recursiva que multiplique a x b

def multiplicar(a, b):
    # caso base
    if b == 1:
        return a
    elif b == 0:
        return 0
    else:
        return a + multiplicar(a, b - 1)

print(multiplicar(5,  10))

print(multiplicar(10,  5))

print(multiplicar(5,  0))

print(multiplicar(0,  5))
