
### EJERCICIO DE PC ###

# ingresar una palabra y verficar si tiene las 5 vocales minimo 1 vez
# imprime el orden de aparicion de las vocales

palabra = str(input("Input: "))

letraa = False
letrae = False
letrai = False
letrao = False
letrau = False

cadena_vocales = ""
for letra in palabra:
    if letra.lower() == 'a':
        letraa = True
        cadena_vocales += letra
    elif letra.lower() == 'e':
        letrae = True
        cadena_vocales += letra
    elif letra.lower() == 'i':
        letrai = True
        cadena_vocales += letra
    elif letra.lower() == 'o':
        letrao = True
        cadena_vocales += letra
    elif letra.lower() == 'u':
        letrau = True
        cadena_vocales += letra

if letraa and letrae and letrai and letrao and letrau:
    print("La palabra tiene las 5 vocales!")
else:
    print("La palabra no tiene las 5 vocales!")

print(cadena_vocales)
