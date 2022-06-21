
### EJERCICIO ###

# recursividad
# Escribir una función recursiva que invierta una palabra

def invertir(palabra):
    if len(palabra) == 1:
        return palabra
    else:
        return palabra[-1] + invertir(palabra[0:len(palabra)-1:1])

print(invertir("hola"))
