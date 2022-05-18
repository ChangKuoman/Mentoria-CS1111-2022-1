
### EJERCICIO ###

# Escribir un programa que solicite al usuario una frase e ingrese las vocales a una una lista y las consonantes a otra, sin repetirse.

cadena = str(input("Ingrese cadena: "))

lista_vocales = []
lista_consonantes = []

for letra in cadena.lower():
    if letra in "aeiou":
        if letra not in lista_vocales:
            lista_vocales.append(letra)
    elif letra == ' ':
        continue
    elif letra not in lista_consonantes:
        lista_consonantes.append(letra)

print(lista_vocales)
print(lista_consonantes)
