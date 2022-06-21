
### EJERCICIO ###

# archivos
# Escribir un programa que permita al usuario ingresar palabras hasta poner “F” y
# se escriba en un archivo .txt
file = open('ej2.txt', 'w')

while True:
    palabra = str(input("Ingrese palabra: "))
    if palabra == 'F':
        break
    file.write(palabra)
    file.write('\n')

file.close()
