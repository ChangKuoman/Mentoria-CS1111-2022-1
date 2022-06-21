
### EJERCICIO ###

# recursividad
# 5. (Nivel 1) Escribir una funcion recursiva que nos permita elevar a la N potencia
# cualquier numero. El usuario ingresa primero el numero y luego el exponente.
# Ejemplos:
# Ingrese un numero : 4
# Ingrese el exponente : 2
# El resultado es: 16
# Ingrese un numero : 3
# Ingrese el exponente : 4
# El resultado es: 81

def elevar(base, exponente):
    if (exponente == 0):
        return 1
    elif (exponente == 1):
        return base
    else:
        return base * elevar(base, exponente - 1)

print(elevar(4, 2))
print(elevar(3, 4))
