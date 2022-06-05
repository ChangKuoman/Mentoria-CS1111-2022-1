
# que la ultima letra de cada palabra sea en mayuscula
# hola como estas
# holA comO estaS

cadena = str(input("Ingrese cadena: "))

cadena_nueva = ""
for palabra in cadena.split():
    for i in range(len(palabra)):
        if i == len(palabra)-1:
            cadena_nueva += palabra[i].upper()
        else:
            cadena_nueva += palabra[i].lower()
    cadena_nueva += " "

print(cadena_nueva)
