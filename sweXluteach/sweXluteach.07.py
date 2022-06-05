
# enunciado: funciones_2.JPG

def posicion_alfabeto(letra):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    posicion = alfabeto.find(letra) + 1
    posicion_ascii = ord(letra) - 64
    return posicion_ascii

def hallar_suma(cadena):
    suma = 0
    for letra in cadena.upper():
        suma += posicion_alfabeto(letra)
    return suma

cadena = str(input("Ingrese cadena: "))
print(hallar_suma(cadena))
