
### EJERCICIO ###

# Pedir a usuario que ingrese una frase y analice cada palabra, si comienza por una vocal el programa
# imprime la palabra.

frase = str(input("Ingrese una frase: "))

for palabra in frase.split(' '):
    if palabra[0].lower() in "aeiouAEIOU":
        print(palabra, end=" ")
