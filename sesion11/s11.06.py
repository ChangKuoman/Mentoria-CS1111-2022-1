
### EJERCICIO DE PC ###

"""
Utilizando diccionarios evaluar un texto y generar un diccionario con las letras
en minúscula como keys y como valor una lista con las posiciones donde aparece la letra en el texto.
"""

# hola que tal
# {'a': [3, 10], 'h':[0]}

cadena = str(input("Ingrese una cadena a evaluar: ")).lower()
posiciones_letras = {}

for posicion, letra in enumerate(cadena):
    # print(posicion, letra)
    if letra not in posiciones_letras:
        posiciones_letras[letra] = [posicion]
    else:
        posiciones_letras[letra].append(posicion)

print(posiciones_letras)
