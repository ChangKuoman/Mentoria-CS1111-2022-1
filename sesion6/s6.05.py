
### INTRODUCCION ###

# strings
cadena = str(input("cadena: "))

for palabra in cadena.split():
    print(palabra)

cadena = "##HOLA#HOLA###"

cadena = cadena.strip("#")

print(cadena)
