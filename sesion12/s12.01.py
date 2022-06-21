
### INTRODUCCION ###

# archivos
# (.txt .json .csv)

# r
# w
# a
file = open('archivo.txt', 'r')

# manera 1:
# lineas = file.readlines()

# manera 2:
# for linea in file:
#    print(linea.rstrip())

# 'hola\n'.rstrip() -> 'hola'

# manera 3:
# linea = file.readline()
# while linea != '':
#    print(linea)
#    linea = file.readline()

file.close()
