
# enunciado: strings_3.JPG

cadena = str(input("Ingrese una cadena: "))

cadena_resultado = ""
for i in range(len(cadena)):
    if i % 2 == 0:
        cadena_resultado += cadena[i].upper()
    else:
        cadena_resultado += cadena[i].lower()

print(cadena_resultado)
# cadena[0::2].upper()
