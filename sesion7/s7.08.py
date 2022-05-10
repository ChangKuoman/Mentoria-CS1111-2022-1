
### EJERCICIO ###

# Escribir un programa en el cual se ingrese una palabra e imprimir la palabra segun lo
# indicado (no considere números):
# las vocales en mayúsculas y las consonantes en minúsculas
# las vocales en minúsculas y las consonantes de mayúsculas
# toda la palabra en mayúsculas
# toda la palabra en minúsculas

palabra = str(input("Ingrese palabra: "))

cadena1 = ""
cadena2 = ""
for letra in palabra:
    if letra.lower() in "aeiou":
        # vocales
        cadena1 += letra.upper()
        cadena2 += letra.lower()
    else:
        # consonantes
        cadena1 += letra.lower()
        cadena2 += letra.upper()

print(cadena1)
print(cadena2)
print(palabra.upper())
print(palabra.lower())
