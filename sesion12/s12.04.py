
### EJERCICIO ###

# archivos
# Escribir un programa que lea un archivo .txt e imprima solo las lineas pares, siendo la
# primera 1.
archivo = open('ej2.txt', 'r')

contador = 1
for linea in archivo:
    if contador % 2 == 0:
        print(linea.rstrip())
    contador += 1

archivo.close()
