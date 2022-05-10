
### EJERCICIO ###

# Escribir un programa que solicite al usuario una palabra y use una función para verificar
# si contiene las letras de “p”, “a” y “n”, la función debe retornar un booleano.

def contiene_pan(cadena):
    # manera 1
    letrap = False
    letraa = False
    letran = False
    for letra in cadena:
        if letra == 'p':
            letrap = True
        if letra == 'a':
            letraa = True
        if letra == 'n':
            letran = True

    if (letrap == True and letraa == True and letran == True):
        return True
    else:
        return False
    # manera 2
    return ('p' in cadena) and ('a' in cadena) and ('n' in cadena)


# print(contiene_pan("pan"))
# print(contiene_pan("hjkl"))
# print(contiene_pan("aty"))
# print(contiene_pan("anh"))
