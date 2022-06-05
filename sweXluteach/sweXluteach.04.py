
# enunciado: strings_2.JPG

cadena = str(input("Ingrese 2 palabras separadas por un espacio: "))

palabra1, palabra2 = cadena.split()

nueva_cadena = ""
nueva_cadena += palabra2[0]
nueva_cadena += palabra1[1::]
nueva_cadena += " "
nueva_cadena += palabra1[0]
nueva_cadena += palabra2[1::]

print(nueva_cadena)
