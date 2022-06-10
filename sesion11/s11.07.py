
### EJERCICIO DE PC ###

"""
Escribir un programa en Python que cree un diccionario de traducci ́on INGLES-ESPAÑOL.
• Ingresar datos desde teclado [clave:valor]y almacenarlos en un diccionario (obligatorio).
• Si ingresa una palabra que existe debe agregar un sinónimo.
• Mostrar las palabras que tienen 2 o mas sinónimos en ingles.
• Ingresar ”salir” para terminar de ingresar
Input : mirar , look
Input : perro , dog
Input : mirar , watch
Output :
mirar :[ look , watch ]
"""

dict = {}

while True:
    cadena = str(input("Input (llave,valor): "))
    if cadena == "salir":
        break
    llave, valor = cadena.split(",")
    if llave not in dict.keys():
        dict[llave] = [valor]
    else:
        dict[llave].append(valor)

for key, value in dict.items():
    if len(value) >= 2:
        print(key, value)
