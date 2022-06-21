
### INTRODUCCION ###

# archivos
file = open('archivo2.txt', 'w')

file.write('HOLA')

palabra = input("Ingrese palabra: ")

file.write(' ')
file.write(palabra)

file.close()

file = open('archivo2.txt', 'a')

file.write(' ')
file.write('quequitos')

file.close()
