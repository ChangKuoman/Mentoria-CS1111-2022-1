
### EJERCICIO ###

# crear una funcion que invierta una palabra
def invertir_palabra(palabra):

    palabra_invertida = ""
    for letra in palabra:
        palabra_invertida = letra + palabra_invertida

    return palabra_invertida
print(invertir_palabra("hola"))

# palabra = "hola"
# palabra_invertida = ""
# for letra in palabra:
#     palabra_invertida = letra + palabra_invertida
